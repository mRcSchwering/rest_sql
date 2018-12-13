# this python file uses the following encoding: utf-8
import logging
from flask_restplus import Namespace, Resource, reqparse
from data.models import User

log = logging.getLogger(__name__)

api = Namespace('user', description='records related operations')


@api.route('/')
class AllRecords(Resource):
    '''All users'''

    def get(self):
        '''Get all users'''
        users = User.query.all()
        log.info(users)
        return [u.username for u in users]
