# this python file uses the following encoding: utf-8
import logging
from apis.auth import auth

from flask_restplus import Namespace, Resource, reqparse

log = logging.getLogger(__name__)

api = Namespace('records', description='records related operations')
#utils = Utils()
#auth = utils.auth


@api.route('/')
class AllRecords(Resource):
    '''Look at all records'''

    @auth.login_required
    def get(self):
        '''Get all records'''
        log.info('hi')
        return 'hi'
