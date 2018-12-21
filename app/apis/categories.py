# this python file uses the following encoding: utf-8
import logging
from flask import request
from flask_restplus import Namespace, Resource, reqparse, fields
import data.methods as methods
from apis.auth import auth

log = logging.getLogger(__name__)
api = Namespace('Categories', description='Categories description')


# serializers
cat_obj = api.model('Category object', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a category'),
    'name': fields.String(required=True, description='Category Title')
})

cat_payload = api.model('Payload for creating a category', {
    'name': fields.String(required=True, description='Category Title')
})


# endpoints
@api.route('/')
class AllCategories(Resource):

    @auth.login_required
    @api.marshal_with(cat_obj)
    def get(self):
        '''
        Description for '*/cats/' endpoint for just getting all categories
        '''
        return methods.get_all_cats()

    @auth.login_required
    @api.expect(cat_payload)
    def post(self):
        '''
        Creating a new category by POSTing json payload
        '''
        data = request.json
        methods.create_category(data.get('name'))
        return 'category created'
