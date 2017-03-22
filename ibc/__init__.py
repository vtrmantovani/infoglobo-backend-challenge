import logging
import os
import sys

from flask import Flask
from flask_httpauth import HTTPBasicAuth

logger = logging.getLogger(__name__)

users = {
    "admin": "password",
}

auth = HTTPBasicAuth()


@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None


def create_app(config_var=os.getenv('DEPLOY_ENV', 'Development')):
    app = Flask(__name__)
    app.config.from_object('ibc.config.%sConfig' % config_var)
    app.config['DEPLOY_ENV'] = config_var

    configure_logger(app)

    register_blueprints_and_error_handling(app)

    return app


def configure_logger(app):
    if not logger.handlers:
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(app.config['LOGS_LEVEL'])
        logger.addHandler(ch)


def register_blueprints_and_error_handling(app):
    from ibc.views.common import common
    app.register_blueprint(common)
    from ibc.views.api import api
    app.register_blueprint(api)
