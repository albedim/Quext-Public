from quext.configuration.config import sql

#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 23/01/23
# Created at: 00:16
# Version: 1.0.0
# Description: This is the class for the password's magic link entity
#


class PasswordMagicLink(sql.Model):
    id: int = sql.Column(sql.Integer, primary_key=True)
    link: str = sql.Column(sql.String(100), nullable=False)
    userId: str = sql.Column(sql.Integer, nullable=False)

    def __init__(self, link, userId):
        self.link = link
        self.userId = userId

    def toJson(self):
        return {
            'id': self.id,
            'link': self.link,
            'userId': self.userId
        }
