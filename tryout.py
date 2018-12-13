# this python file uses the following encoding: utf-8
from app import db, User

db.create_all()

admin = User(username='admin', email='admin@example.com')
guest = User(username='guest', email='guest@example.com')

db.session.add(admin)
db.session.add(guest)
db.session.commit()


User.query.all()
