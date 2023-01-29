from googletrans import Translator

from quext.utils.Util import Util
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx
import nltk

from quext.utils.exceptions.IncorrectApiKeyException import IncorrectApiKeyException

nltk.download('stopwords')


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 27/01/23
# Created at: 23:14
# Version: 1.0.0
# Description: This is the class for the summary service
#


def getSummaryByText(request):
    """ Gets the request and works on it """
    try:
        Util.checkApiKey(request['API_KEY'])  # if not, raise exception
        return Util.createSuccessResponse(True, generateSummary(request['text'], 4, request['language']))
    except KeyError:
        return Util.createWrongResponse(False, Util.INVALID_REQUEST, 405)
    except IncorrectApiKeyException:
        return Util.createWrongResponse(False, Util.INCORRECT_API_KEY, 403)
    except IndexError:
        return Util.createWrongResponse(False, Util.IMAGE_ANGLE, 500)
    except Exception as e:
        print(e)
        return Util.createWrongResponse(False, Util.SERVER_ERROR, 500)


def readArticle(text):
    """ Reads the text and splits it """
    article = text.split(". ")
    sentences = []

    for sentence in article:
        sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
    sentences.pop()

    return sentences


def sentenceSimilarity(sent1, sent2, stopwords=None):
    """ Builds two vectors for both sentences """
    if stopwords is None:
        stopwords = []

    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]

    allWords = list(set(sent1 + sent2))

    vector1 = [0] * len(allWords)
    vector2 = [0] * len(allWords)

    # build the vector for the first sentence
    for w in sent1:
        if w in stopwords:
            continue
        vector1[allWords.index(w)] += 1

    # build the vector for the second sentence
    for w in sent2:
        if w in stopwords:
            continue
        vector2[allWords.index(w)] += 1

    return 1 - cosine_distance(vector1, vector2)


def buildSimilarityMatrix(sentences, stop_words):
    # Create an empty similarity matrix
    similarityMatrix = np.zeros((len(sentences), len(sentences)))

    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2:  # ignore if both are same sentences
                continue
            similarityMatrix[idx1][idx2] = sentenceSimilarity(sentences[idx1], sentences[idx2], stop_words)

    return similarityMatrix


def generateSummary(text, top_n, language):
    stopWords = stopwords.words('english')
    summarizeText = []

    # text splitter
    sentences = readArticle(text)

    # generates matrix which has to be similar to the original array
    sentenceSimilarityMartix = buildSimilarityMatrix(sentences, stopWords)

    # understands the important sentences
    sentence_similarity_graph = nx.from_numpy_array(sentenceSimilarityMartix)
    scores = nx.pagerank(sentence_similarity_graph)

    # mixes everything
    ranked_sentence = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
    for i in range(top_n):
        summarizeText.append(" ".join(ranked_sentence[i][1]))

    # translate and return summary
    translator = Translator()
    return translator.translate(". ".join(summarizeText), dest=language).text
