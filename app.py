from quext.configuration.config import app, sql
from quext.controller import SummaryController, LanguageController, UserController

# controllers init
app.register_blueprint(SummaryController.summary)
app.register_blueprint(UserController.user)
app.register_blueprint(LanguageController.language)


def create_app():
    with app.app_context():
        sql.create_all()
        return app


if __name__ == '__main__':
    create_app().run()