# в app/models.py
# теперь опишем простую таблицу
#from . import db
#from datetime import datetime


#class Post(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    title = db.Column(db.String(256), index=True, unique=True)
#    created = db.Column(db.DateTime(), default=datetime.utcnow)
#    text = db.Column(db.Text())

#    def __repr__(self):
#        return '<Post {}>'.format(self.title)



# обновленный models.py

from datetime import datetime

from app import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), index=True, unique=True)
    created = db.Column(db.DateTime(), default=datetime.utcnow)
    text = db.Column(db.Text())
    #sender = db.Column(db.String(100))
    comments = db.relationship('Comment', backref='post')

    def __repr__(self):
        return '<Post {}>'.format(self.title)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))