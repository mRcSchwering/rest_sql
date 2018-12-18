# this python file uses the following encoding: utf-8
import json
import os

# Default Settings
# overwritten by appropriate files 'secrets/config.json',
# 'secrets/cert.pem' and 'secrets/key.pem'

TESTING = True  # if you dont provide SQLALCHEMY_DATABASE_URI in config.json

# Flask settings
FLASK_SERVER_NAME = '0.0.0.0:5000'  # 0.0.0.0 when dockerized
FLASK_DEBUG = True  # Do not use debug mode in production
FLASK_SSL = False  # needs 'secrets/cert.pem' and 'secrets/key.pem'

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'  # none, list, full
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False

# SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
SQLALCHEMY_TRACK_MODIFICATIONS = False


if os.path.isfile('secrets/config.json'):
    with open('secrets/config.json') as inf:
        config = json.load(inf)

    if config.get('SQLALCHEMY_DATABASE_URI', None) is not None:
        SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')
        TESTING = False


if os.path.isfile('secrets/cert.pem') and os.path.isfile('secrets/key.pem'):
    FLASK_SSL = True


if TESTING:
    FLASK_SSL = False
else:
    FLASK_DEBUG = False
