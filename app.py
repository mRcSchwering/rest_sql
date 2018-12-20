# this python file uses the following encoding: utf-8
import logging
from flask import Flask
import settings
from apis import api
from data import db
from data.methods import on_app_startup
import test.testdata as testdata

from apis.posts import api as posts_api
from apis.categories import api as cats_api

app = Flask(__name__)
api.add_namespace(posts_api, path='/posts')
api.add_namespace(cats_api, path='/categories')

if settings.TESTING:
    from apis.reset_testdata import api as reset_testdata_api
    api.add_namespace(reset_testdata_api, path='/reset_testdata')

log = logging.getLogger(__name__)


def configure_app(flask_app):
    logging.basicConfig(level=logging.DEBUG if settings.FLASK_DEBUG else logging.INFO)

    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


def initialize_app(flask_app):
    configure_app(flask_app)
    db.init_app(flask_app)
    api.init_app(flask_app)

    with app.app_context():
        on_app_startup()


if __name__ == '__main__':
    initialize_app(app)
    ssl = ('secrets/cert.pem', 'secrets/key.pem') if settings.FLASK_SSL else None
    connection = '%s://%s:5000' % ('https' if settings.FLASK_SSL else 'http', settings.FLASK_HOST)
    test = 'test ' if settings.TESTING else ''
    log.info('\n\n>>>>> Starting %sserver %s <<<<<\n' % (test, connection))

    app.run(debug=settings.FLASK_DEBUG, ssl_context=ssl, host=settings.FLASK_HOST)
