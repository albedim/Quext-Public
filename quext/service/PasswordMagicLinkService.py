from quext.model.repository.PasswordMagicLinkRepository import create, get, delete
from quext.utils.Util import Util
from quext.utils.exceptions.IncorrectApiKeyException import IncorrectApiKeyException
from resources.config import config


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 22/01/23
# Created at: 02:35
# Version: 1.0.0
# Description: This is the class for the user service
#


def createLink(request):
    try:
        Util.checkApiKey(request['API_KEY'])  # if not, raise exception
        create(request['userId'])
        return Util.createSuccessResponse(True, Util.LINK_SUCCESSFULLY_CREATED)
    except KeyError:
        return Util.createWrongResponse(False, Util.INVALID_REQUEST, 405)
    except IncorrectApiKeyException:
        return Util.createWrongResponse(False, Util.INCORRECT_API_KEY, 403)


def getUserId(request):
    """ Get userId of this magic link """
    try:
        Util.checkApiKey(request['API_KEY'])  # if not, raise exception
        passwordMagicLink = get(request['link'])
        if passwordMagicLink is not None:
            return Util.createSuccessResponse(True, passwordMagicLink.userId)
        else:
            return Util.createWrongResponse(False, Util.USER_NOT_FOUND, 404)
    except KeyError:
        return Util.createWrongResponse(False, Util.INVALID_REQUEST, 405)
    except IncorrectApiKeyException:
        return Util.createWrongResponse(False, Util.INCORRECT_API_KEY, 403)


def deleteLink(userId, apiKey):
    try:
        Util.checkApiKey(apiKey)  # if not, raise exception
        delete(userId)
        return Util.createSuccessResponse(True, None)
    except KeyError:
        return Util.createWrongResponse(False, Util.INVALID_REQUEST, 405)
    except IncorrectApiKeyException:
        return Util.createWrongResponse(False, Util.INCORRECT_API_KEY, 403)
