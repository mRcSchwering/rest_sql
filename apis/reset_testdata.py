# this python file uses the following encoding: utf-8
import logging
from flask_restplus import Namespace, Resource, reqparse
import test.testdata as testdata

log = logging.getLogger(__name__)
api = Namespace('Reset Testdata', description='For testing only')


# endpoints
@api.route('/')
class ResetDatabase(Resource):

    def get(self):
        """
        GET to reset database with testdata during tests
        """
        testdata.reset_database()
        return 'data successfully resetted'
