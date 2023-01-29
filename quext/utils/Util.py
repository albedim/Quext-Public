import base64
import datetime
import io
import os
import random

from PIL import Image
from flask import jsonify

from quext.utils.exceptions.IncorrectApiKeyException import IncorrectApiKeyException
from resources.rest_service import config

#
# @author: albedim <dimaio.albe@gmail.com>
# Created on: 22/01/23
# Created at: 02:35
# Version: 1.0.0
# Description: This is the class for the utils
#


class Util():

    USER_NOT_FOUND = 'This user was not found'
    IMAGE_ANGLE = 'No text was found in this image, it could be rotated'
    INCORRECT_API_KEY = 'Your api key is not correct'
    SERVER_ERROR = 'An error occurred while reading your request'
    INVALID_REQUEST = 'Invalid request'
    USER_PASSWORD_SUCCESSFULLY_CHANGED = "Your password has been changed"
    LINK_SUCCESSFULLY_CREATED = "Link successfully created"
    USER_SUCCESSFULLY_ADDED = 'This user was successfully added'
    USER_ALREADY_EXISTS = 'This user already exists'

    @classmethod
    def createList(cls, elements):
        response = []
        for element in elements:
            response.append(element.toJson())
        return jsonify(response)

    @classmethod
    def createSuccessResponse(cls, success, param):
        return jsonify({
            "date": str(datetime.datetime.now()),
            "success": success,
            "param": param,
            "code": 200,
        })

    @classmethod
    def createWrongResponse(cls, success, error, code):
        return jsonify({
            "date": str(datetime.datetime.now()),
            "success": success,
            "error": error,
            "code": code,
        })

    @classmethod
    def getURL(cls, controllerName):
        return '/api/v_' + config['version'].replace('.', '_') + '/' + controllerName

    @classmethod
    def hash(cls, password: str):
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        hashedPassword = ""
        encryptedChars = "C0yZEIipDF23djS5muGMfnV6HtcW4q9BJLXlPakrghNeK1AsU8xRwQbzYO7Tov"
        for i in range(len(password)):
            for j in range(len(chars)):
                if password[i] == chars[j]:
                    hashedPassword += encryptedChars[j]
                    break
        return hashedPassword

    @classmethod
    def unHash(cls, password: str):
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        unhashedPassword = ""
        encryptedChars = "C0yZEIipDF23djS5muGMfnV6HtcW4q9BJLXlPakrghNeK1AsU8xRwQbzYO7Tov"
        for i in range(len(password)):
            for j in range(len(encryptedChars)):
                if password[i] == encryptedChars[j]:
                    unhashedPassword += chars[j]
                    break
        return unhashedPassword

    @classmethod
    def createLink(cls, length):
        letters = "ABCDEFGHILMNOPQRSTUVZYJKXabcdefghilmnopqrstuvzyjkx0123456789"
        link = ""
        for i in range(length):
            link += letters[random.randint(0,59)]
        return link


    @classmethod
    def decodeImage(cls, encodedImage):
        decodedImage = base64.b64decode(str(encodedImage))
        file = Image.open(io.BytesIO(decodedImage))
        imageName = cls.createLink(10)
        file.save(f'quext/files/{imageName}.png', 'png')
        return imageName + '.png'

    @classmethod
    def deleteFile(cls, imageName):
        os.remove("quext/files/" + imageName)

    @classmethod
    def checkApiKey(cls, apiKey):
        if apiKey != config.get("owner_api_key"):
            raise IncorrectApiKeyException
