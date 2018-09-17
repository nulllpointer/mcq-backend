from flask_json import json_response,jsonify
from sqlalchemy import exc

from jsonhandler import *
from model import *
from settings import db

from settings import db


class UserHandler(object):
    def create_user(self, data):
        u = User()
        u.username = data['user'][0]['username']
        u.password = data['user'][0]['password']

        user_details = data['user'][0]['user_details']
        ud = UserDetails()
        for userdata in user_details:
            ud.f_name = userdata['f_name']
            ud.email = userdata['email']
            ud.l_name = userdata['l_name']


        # u = User(username=data['user'][0]['username'], password=data['user'][0]['password'], userdetails=ud)
        ud.user=u
        # u.userdetails = [ud]
        users_schema = UserSchema()

        try:

            # serialize = users_schema.dump(user).data
            db.session.add(u)
            db.session.commit()
            u = users_schema.dump(u).data
            return json_response(status_=200, result='success', users=u)

            # return json_response(status_=400, result='user added', user=serialize)
        except exc.SQLAlchemyError as e:
            db.session.rollback()
            f = exc.SQLAlchemyError._message(e)
            # serialize = error_schema.dump(user).data
            u = users_schema.dump(u).data
            return json_response(status_=404, error=f, users=u)

    def getall(object):
        # query = db.session.query(User)
        # users = query.all()

        # u = User.query.all()
        u =User.query.first()
        users_schema = UserSchema()
        output = users_schema.dump(u).data
        # return jsonify({'user': output})
        return json_response(status_=200, result='success', users=output)
