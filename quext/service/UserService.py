from quext.model.entity.User import User
from quext.model.repository.UserRepository import signin, exists, changePassword, signup
from quext.service.PasswordMagicLinkService import deleteLink
from quext.utils.Util import Util
from quext.utils.exceptions.IncorrectApiKeyException import IncorrectApiKeyException


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 22/01/23
# Created at: 02:35
# Version: 1.0.0
# Description: This is the class for the user service
#


def signinUser(request: dict):
    try:
        Util.checkApiKey(request['API_KEY'])  # if not, raise exception
        user: User = signin(
            request['email'],
            Util.hash(request['password'])
        )
        if user is not None:
            return Util.createSuccessResponse(True, user.userId)
        else:
            return Util.createWrongResponse(False, Util.USER_NOT_FOUND, 404)
    except KeyError:
        return Util.createWrongResponse(False, Util.INVALID_REQUEST, 405)
    except IncorrectApiKeyException:
        return Util.createWrongResponse(False, Util.INCORRECT_API_KEY, 403)


def existsByEmail(email) -> bool:
    return exists(email) > 0


def changeUserPassword(request):
    try:
        Util.checkApiKey(request['API_KEY'])  # if not, raise exception
        changePassword(
            request['userId'],
            Util.hash(request['password'])
        )
        deleteLink(request['userId'])
        return Util.createSuccessResponse(True, Util.USER_PASSWORD_SUCCESSFULLY_CHANGED)
    except KeyError:
        return Util.createWrongResponse(False, Util.INVALID_REQUEST, 405)
    except IncorrectApiKeyException:
        return Util.createWrongResponse(False, Util.INCORRECT_API_KEY, 403)


def signupUser(request: dict):
    Util.checkApiKey(request['API_KEY'])  # if not, raise exception
    try:
        if not existsByEmail(request['email']):
            signup(
                request['name'],
                request['email'],
                Util.hash(request['password'])
            )
            return Util.createSuccessResponse(True, Util.USER_SUCCESSFULLY_ADDED)
        else:
            return Util.createWrongResponse(False, Util.USER_ALREADY_EXISTS, 403)
    except KeyError:
        return Util.createWrongResponse(False, Util.INVALID_REQUEST, 405)
    except IncorrectApiKeyException:
        return Util.createWrongResponse(False, Util.INCORRECT_API_KEY, 403)