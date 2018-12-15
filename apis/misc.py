# this python file uses the following encoding: utf-8
import logging
from flask_restplus import Namespace, Resource, reqparse
from apis.auth import auth
import data.methods as methods

log = logging.getLogger(__name__)
api = Namespace('Miscellaneous',
                description="Endpoints for various things that didn't fit anywhere else")


# endpoints
@api.route('/reset_database')
class ResetDatabase(Resource):

    @auth.login_required
    def get(self):
        '''
        GET to reset database with testdata
        '''
        methods.reset_database()
        return 'data successfully resetted'
