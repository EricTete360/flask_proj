from datetime import datetime
from authproj import db, login_manager
from flask_login import UserMixin

# CRUD EXAMPLE POST
# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String(100))
#     email = db.Column(db.String(100))
#     phone = db.Column(db.String(100))


#     def __repr__(self):
#         return f"Post('{self.title}', '{self.date_posted}')"

#     def __init__(self,name,email,phone):
#         self.name = name
#         self.email = email
#         self.phone = phone


# AUTHENTICATION TABLE
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(150),nullable=False)
    mobile = db.Column(db.String(150),nullable=False)
    email = db.Column(db.String(120),nullable=False)
    password = db.Column(db.String(60),nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.mobile}')"

