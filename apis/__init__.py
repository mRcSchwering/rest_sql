# this python file uses the following encoding: utf-8
from flask_restplus import Api

from .records import api as ns1
from .user import api as ns2

api = Api(
    title='Peace in REST - Title',
    version='1.0',
    description='Description for API'
)

api.add_namespace(ns1, path='/records')
api.add_namespace(ns2, path='/user')
