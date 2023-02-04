from quext.configuration.config import sql
from quext.model.entity.PasswordMagicLink import PasswordMagicLink
from quext.utils.Util import Util


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 22/01/23
# Created at: 02:35
# Version: 1.0.0
# Description: This is the class for the user repository
#

def create(userId):
    passwordMagicLink: PasswordMagicLink = PasswordMagicLink(Util.createLink(40), userId)
    sql.session.add(passwordMagicLink)
    sql.session.commit()


def get(link):
    passwordMagicLink = sql.session.query(PasswordMagicLink).filter(PasswordMagicLink.link == link).first()
    return passwordMagicLink


def delete(userId):
    sql.session.query(PasswordMagicLink).filter(PasswordMagicLink.userId == userId).delete()
    sql.session.commit()
