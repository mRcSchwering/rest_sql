# this python file uses the following encoding: utf-8
import json
import os
import sys

# testing
# adds '/reset_testdata/' ednpoint, enables flask debug mode, and turns off ssl
TESTING = True if 'test' in sys.argv else False


# Default Settings
# overwritten by appropriate files 'secrets/config.json',
# 'secrets/cert.pem' and 'secrets/key.pem'

# Flask settings
FLASK_HOST = '0.0.0.0'  # all interfaces for dockerized
FLASK_DEBUG = False  # will be set True if TESTING
FLASK_SSL = False  # existing 'secrets/cert.pem' and 'secrets/key.pem' will set it True

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'  # none, list, full
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False

# SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # existing SQLALCHEMY_DATABASE_URI in config.json will overwrite
SQLALCHEMY_TRACK_MODIFICATIONS = False  # True for large overhead


# check config.json
if os.path.isfile('secrets/config.json'):
    with open('secrets/config.json') as inf:
        config = json.load(inf)

    if config.get('SQLALCHEMY_DATABASE_URI') is not None:
        SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')


# check cert.pem and key.pem
if os.path.isfile('secrets/cert.pem') and os.path.isfile('secrets/key.pem'):
    FLASK_SSL = True


# final things for testing
if TESTING:
    FLASK_SSL = False
    FLASK_DEBUG = True
