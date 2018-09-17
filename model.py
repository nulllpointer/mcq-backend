from settings import db

class User(db.Model):
    # __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)

    # def __repr__(self):
    #     return '<User %r>' % self.username


class UserDetails(db.Model):
    # __tablename__ = 'userdetails'
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(120), unique=False, nullable=False)
    l_name = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='UserDetails')

    # def __repr__(self):
    #     return '<UserDetails %r>' % self.f_name
