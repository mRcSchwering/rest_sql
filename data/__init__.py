from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def reset_database():
    import logging
    from data.models import User

    log = logging.getLogger(__name__)
    log.info('resetting database')

    db.drop_all()
    db.create_all()
    admin = User(username='admin', email='admin@example.com')
    guest = User(username='guest', email='guest@example.com')

    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()
