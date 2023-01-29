from quext.configuration.config import app
from quext.controller import SummaryController, LanguageController

# controllers init
app.register_blueprint(SummaryController.summary)
app.register_blueprint(LanguageController.language)


def create_app():
    with app.app_context():
        return app


if __name__ == '__main__':
    create_app()