from flask import Blueprint, request, jsonify
from flask_cors import cross_origin

from quext.utils.languages import LANGUAGES
from quext.utils.Util import Util

language: Blueprint = Blueprint('LanguageController', __name__, url_prefix=Util.getURL('language'))


@language.route("/get", methods=['GET'])
@cross_origin()
def get():
    return LANGUAGES




