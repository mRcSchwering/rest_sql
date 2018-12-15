# this python file uses the following encoding: utf-8

# Flask settings
FLASK_SERVER_NAME = '0.0.0.0:5000'
FLASK_DEBUG = True  # Do not use debug mode in production
FLASK_SSL = False  # needs 'certs/cert.pem' and 'certs/key.pem'

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'  # none, list, full
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False

# SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
