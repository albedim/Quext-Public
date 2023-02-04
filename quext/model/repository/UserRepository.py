from quext.configuration.config import sql
from quext.model.entity.User import User


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 22/01/23
# Created at: 02:35
# Version: 1.0.0
# Description: This is the class for the user repository
#


def signin(email, password) -> User:
    user: User = sql.session.query(User).filter(User.email == email).filter(User.password == password).first()
    return user


def signup(name, email, password) -> None:
    user: User = User(name, email, password)
    sql.session.add(user)
    sql.session.commit()


def exists(email):
    users: User = sql.session.query(User).filter(User.email == email).count()
    return users


def changePassword(userId, password):
    user: User = sql.session.query(User).filter(User.userId == userId).first()
    user.password = password
    sql.session.commit()
