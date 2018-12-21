# this python file uses the following encoding: utf-8
import json
import os
import sys
import tempfile


# Default Settings
# overwritten by appropriate files 'secrets/config.json',
# 'secrets/cert.pem' and 'secrets/key.pem'

# Flask settings
FLASK_HOST = '0.0.0.0'  # all interfaces dockerized app
FLASK_DEBUG = True  # do not use in prodcution
FLASK_SSL = False  # existing 'secrets/cert.pem' and 'secrets/key.pem' will set it True

# SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = 'sqlite:///test/test.db'  # 'sqlite:///test/test.db' for testing
SQLALCHEMY_TRACK_MODIFICATIONS = False  # do not use in production


# check cert.pem and key.pem
if os.path.isfile('secrets/cert.pem') and os.path.isfile('secrets/key.pem'):
    FLASK_SSL = True


# check config.json
if os.path.isfile('secrets/config.json'):
    with open('secrets/config.json') as inf:
        config = json.load(inf)

    if config.get('FLASK_HOST') is not None:
        FLASK_HOST = config.get('FLASK_HOST')

    if config.get('FLASK_DEBUG') is not None:
        FLASK_DEBUG = config.get('FLASK_DEBUG')

    if config.get('FLASK_SSL') is not None:
        FLASK_SSL = config.get('FLASK_SSL')

    if config.get('SQLALCHEMY_DATABASE_URI') is not None:
        SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')

    if config.get('SQLALCHEMY_TRACK_MODIFICATIONS') is not None:
        SQLALCHEMY_TRACK_MODIFICATIONS = config.get('SQLALCHEMY_TRACK_MODIFICATIONS')


# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'  # none, list, full
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False
