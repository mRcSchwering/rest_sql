# this python file uses the following encoding: utf-8
import logging
from flask_restplus import Namespace, Resource, reqparse
import apis.serializers as serializers
from apis.auth import auth

from data.models import Post

log = logging.getLogger(__name__)
api = Namespace('Posts', description='Posts description')


@api.route('/')
class PostsRoot(Resource):
    '''Description for /posts/ endpoint without parameters'''

    @auth.login_required
    @api.marshal_with(serializers.post)
    def get(self):
        '''Description for GET on /posts/'''
        return Post.query.all()
