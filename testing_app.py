# this python file uses the following encoding: utf-8
import logging
from flask import Flask
from data import db
from data.models import Post, Category

log = logging.getLogger(__name__)
app = Flask(__name__)


# testdata
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


# endoint for resetting testdata
@app.route('/reset_testdata/')
def reset_testdata():
    """
    GET to reset database with testdata during tests
    """
    reset_database()
    return 'data successfully resetted'


if __name__ == '__main__':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test/test.db'
    db.init_app(app)
    app.run(host='0.0.0.0', port=5001)
