# this python file uses the following encoding: utf-8
import logging
from data import db
from data.models import Post, Category

log = logging.getLogger(__name__)


def reset_database():
    log.info('Resetting test database')
    db.drop_all()
    db.create_all()

    py = Category(name='Python')
    Post(title='Hello Python!', body='Python is pretty cool', category=py)
    p = Post(title='Snakes', body='Ssssssss')
    py.posts.append(p)
    db.session.add(py)

    db.session.commit()
