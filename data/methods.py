# this python file uses the following encoding: utf-8
import logging
from data import db
from data.models import Post, Category

log = logging.getLogger(__name__)


def get_all_posts(id):
    if id is None:
        return Post.query.all()
    return 'hi'


def get_posts_by(id, cat_id=None, cat=None):
    if id is not None:
        return Post.query.filter(Post.id == id).one()
    if cat_id is not None:
        return Post.query.filter(Post.category_id == cat_id).all()
    if cat is not None:
        res = Post.query \
            .join(Post.category) \
            .filter(Category.name == cat) \
            .all()
        return res
    return Post.query.all()


def get_posts_from(year, month=None, day=None):
    start_month = 1 if month is None else month
    end_month = 12 if month is None else month
    start_day = 1 if day is None else day
    end_day = 31 if day is None else day + 1

    start_date = '{0:04d}-{1:02d}-{2:02d}'.format(year, start_month, start_day)
    end_date = '{0:04d}-{1:02d}-{2:02d}'.format(year, end_month, end_day)
    res = Post.query \
        .filter(Post.pub_date >= start_date) \
        .filter(Post.pub_date <= end_date) \
        .all()
    return res


def create_post(title, body, category_id):
    log.info('creating post "%s" with category id %d' % (title, category_id))
    category = Category.query.filter(Category.id == category_id).one()
    log.info('category found: %s' % category)
    post = Post(title=title, body=body, category=category)
    log.info('creating: %s' % post)
    db.session.add(post)
    db.session.commit()
