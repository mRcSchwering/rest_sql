# this python file uses the following encoding: utf-8
import logging
from flask_restplus import Namespace, Resource, reqparse
from apis.auth import auth
from data.models import User

log = logging.getLogger(__name__)
api = Namespace('Users', description='Descriptions for endpoints under /users')


@api.route('/')
class AllRecords(Resource):
    '''Descriptions for /users/ without any parameters'''

    @auth.login_required
    def get(self):
        '''GET for /users/'''
        return [u.username for u in User.query.all()]
