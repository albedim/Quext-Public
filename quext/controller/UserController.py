from flask import Blueprint, request
from flask_cors import cross_origin

from quext.service.UserService import signinUser, signupUser, changeUserPassword
from quext.utils.Util import Util

user: Blueprint = Blueprint('UserController', __name__, url_prefix=Util.getURL('user'))


@user.route("/signin", methods=['POST'])
@cross_origin()
def signinUserReq():
    return signinUser(request.json)


@user.route("/signup", methods=['POST'])
@cross_origin()
def signupUserReq():
    return signupUser(request.json)


@user.route("/change-password", methods=['PUT'])
@cross_origin()
def changeUserPasswordReq():
    return changeUserPassword(request.json)




