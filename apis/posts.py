# this python file uses the following encoding: utf-8
import logging
from flask_restplus import Namespace, Resource, reqparse, fields
import data.methods as methods
from apis.auth import auth


log = logging.getLogger(__name__)
api = Namespace('Posts', description='Posts description')


# serializers
post_marshal = api.model('Post object', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a blog post'),
    'title': fields.String(required=True, description='Article title'),
    'body': fields.String(required=True, description='Article content'),
    'pub_date': fields.DateTime,
    'category_id': fields.Integer(attribute='category.id'),
    'category': fields.String(attribute='category.name'),
})


# parsers
get_posts_args = reqparse.RequestParser()
get_posts_args.add_argument(
    'id', type=int, required=False, default=None, help='the unique post id')
get_posts_args.add_argument(
    'cat_id', type=int, required=False, default=None, help='unique id of category')
get_posts_args.add_argument(
    'cat', type=str, required=False, default=None, help='name of category')


# endpoints
@api.route('')
class PostsByParameters(Resource):

    @auth.login_required
    @api.expect(get_posts_args)
    @api.marshal_with(post_marshal)
    def get(self):
        '''
        GET with regular arguments - like /posts?id=5

        More flexible, makes sense with optional arguments
        Btw only all description lines after the first are only shown in swagger UI
        when you expand the description (by clicking on it)
        '''
        args = get_posts_args.parse_args()
        return methods.get_posts_by(id=args.id, cat_id=args.cat_id, cat=args.cat)


@api.route('/')
class AllPosts(Resource):

    @auth.login_required
    @api.marshal_with(post_marshal)
    def get(self):
        '''
        Description for '*/posts/' endpoint for just getting all posts

        GETs are chached and in browser history => convenient, but never use for sensitive stuff
        POSTs are neither cached nor in history, also body size is not limited
        '''
        return methods.get_all_posts(id=None)


@api.route('/<int:id>')
@api.response(404, 'Post not found.')
class PostsById(Resource):

    @auth.login_required
    @api.marshal_with(post_marshal)
    def get(self, id):
        '''
        GET with parameters from '/'- like /posts/5

        More rigid than the '?'-version, so here we can only filter by id
        but seems intuitive since */posts/ gave us all posts
        @api.response documents that there will be a 404 if we cant find the post
        (this is just for the user /in swagger)
        might be useful here because user might think that an empty array is returned
        if post id wasnt found
        This endpoint returns an error if nothing found because its queried with .one()
        '''
        return methods.get_posts_by(id=id)


@api.route('/archive/<int:year>/')
@api.route('/archive/<int:year>/<int:month>/')
@api.route('/archive/<int:year>/<int:month>/<int:day>/')
class PostsByTime(Resource):

    @api.marshal_with(post_marshal)
    def get(self, year, month=None, day=None):
        '''
        GET with optional '/'-separated parameters

        more rigid than with '?', but here it makes sense (year -> month -> day)
        but you couldn't e.g. search for all posts from March of any year
        '''
        return methods.get_posts_from(year, month, day)
