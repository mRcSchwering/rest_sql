# this python file uses the following encoding: utf-8
import logging
from flask_restplus import Namespace, Resource, reqparse
from apis.auth import auth
from data import db
from data.models import User, Post, Category

log = logging.getLogger(__name__)
api = Namespace('Miscellaneous',
                description="Endpoints for various things that didn't fit anywhere else")


# logic
def reset_database():
    log.info('Resetting database')
    db.drop_all()
    db.create_all()

    admin = User(username='admin', email='admin@example.com')
    guest = User(username='guest', email='guest@example.com')
    db.session.add(admin)
    db.session.add(guest)

    py = Category(name='Python')
    Post(title='Hello Python!', body='Python is pretty cool', category=py)
    p = Post(title='Snakes', body='Ssssssss')
    py.posts.append(p)
    db.session.add(py)

    db.session.commit()


# endpoints
@api.route('/reset_database/')
class ResetDatabase(Resource):
    '''Reset database with test data'''

    @auth.login_required
    def get(self):
        '''GET to reset database'''
        reset_database()
        return 'data successfully resetted'
