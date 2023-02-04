from quext.configuration.config import sql

#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 22/01/23
# Created at: 02:35
# Version: 1.0.0
# Description: This is the class for the user entity
#


class User(sql.Model):
    userId: int = sql.Column(sql.Integer, primary_key=True)
    name: str = sql.Column(sql.String(20), nullable=False)
    email: str = sql.Column(sql.String(40), nullable=False)
    password: str = sql.Column(sql.String(40), nullable=False)
    developerMode: bool = sql.Column(sql.Boolean, nullable=False)
    premium: bool = sql.Column(sql.Boolean, nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.developerMode = False
        self.premium = False

    def toJson(self):
        return {
            'userId': self.userId,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'developerMode': self.developerMode,
            'premium': self.premium
        }
