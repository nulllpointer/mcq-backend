# # # import fields as fields
# # # from flask_sqlalchemy import SQLAlchemy
# # #
# # # from flask import Flask, request, jsonify
# # # from flask_restful import reqparse, abort, Api, Resource
# # # from sqlalchemy import inspect
# # # import pandas as pd
# # # from flask_json import FlaskJSON, JsonError, json_response
# # # from flask_marshmallow import Marshmallow
# # # from marshmallow import Schema, fields, pprint
# # #
# # # from sqlalchemy import exc
# # #
# # # app = Flask(__name__)
# # # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12qw12qw@localhost:3306/testtest'
# # # db = SQLAlchemy(app)
# # # json = FlaskJSON(app)
# # # api = Api(app)
# # # ma = Marshmallow(app)
# # #
# # #
# # # class UserSchema(Schema):
# # #     class Meta:
# # #         # Fields to expose
# # #         fields = ('username', 'password')
# # #
# # #
# # # class UserDetailsSchema(Schema):
# # #     user = fields.Nested(UserSchema)
# # #     class Meta:
# # #         fields = ('email', 'f_name', 'l_name')
# # #
# # #
# # # class ErrorSchema(ma.Schema):
# # #     class Meta:
# # #         # Fields to expose
# # #         fields = ('email', 'f_name', 'l_name', 'username')
# # #
# # #
# # # user_schema = UserSchema()from flask_json import json_response
# # from sqlalchemy import exc
# #
# # from jsonhandler import *
# # from model import *
# # from settings import db
# #
# # from settings import db
# #
# # class UserHandler(object):
# #     def create_user(self, data):
# #         user= User()
# #         # user.id = data['user'][0]['id']
# #         user.username = data['user'][0]['username']
# #         user.password = data['user'][0]['password']
# #         user.userdetails.f_name = data['user'][0]['user_details'][0]['f_name']
# #         user.userdetails.email = data['user'][0]['user_details'][0]['email']
# #         user.userdetails.l_name = data['user'][0]['user_details'][0]['l_name']
# #
# #
# #         try:
# #             userdetails = UserDetails()
# #             userdetails.user_id = user.id
# #
# #             # serialize = users_schema.dump(user).data
# #             db.session.add(user)
# #             db.session.commit()
# #             u = users_schema.dump(user).data
# #             return json_response(status_=200, result='success', users=u)
# #
# #             # return json_response(status_=400, result='user added', user=serialize)
# #         except exc.SQLAlchemyError as e:
# #             db.session.rollback()
# #             f = exc.SQLAlchemyError._message(e)
# #             # serialize = error_schema.dump(user).data
# #             u = error_schema.dump(user).data
# #             return json_response(status_=404, error=f, users=u)
# #
# #     def getall(object):
# #         # query = db.session.query(User)
# #         # users = query.all()
# #
# #         u=User.query.all()
# #         users_schema = UserSchema()
# #
# #         print(users_schema.dump(u))
# #         t = users_schema.dump(u).data
# #         return json_response(status_=200, result='success', users=t)
# #
# # # userdetails_schema = UserDetailsSchema(many=True)
# # # # users_schema = UserSchema(many=True)
# # # error_schema = ErrorSchema()
# # #
# # #
# # # # errors_schema = ErrorSchema(many=True)
# # #
# # #
# # # class User(db.Model):
# # #     id = db.Column(db.Integer, primary_key=True)
# # #     username = db.Column(db.String(80), unique=True, nullable=False)
# # #     password = db.Column(db.String(120), unique=True, nullable=False)
# # #     userdetails = db.relationship('UserDetails', backref='user', uselist=False, lazy=True)
# # #
# # #     def __repr__(self):
# # #         return '<User %r>' % self.username
# # # 
# # #
# # # class UserDetails(db.Model):
# # #     id = db.Column(db.Integer, primary_key=True)
# # #     f_name = db.Column(db.String(120), unique=False, nullable=False)
# # #     l_name = db.Column(db.String(120), unique=False, nullable=False)
# # #     email = db.Column(db.String(120), unique=False, nullable=False)
# # #     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
# # #
# # #     def __repr__(self):
# # #         return '<UserDetails %r>' % self.f_name
# # #
# # #
# # # class adds(Resource):
# # #     def post(self):
# # #         json_object = request.get_json(force=True)
# # #         data = dict(json_object)
# # #
# # #         user = User()
# # #         user.username = data['user'][0]['username']
# # #         user.password = data['user'][0]['password']
# # #         user.email = data['user'][0]['user_details'][0]['email']
# # #         user.f_name = data['user'][0]['user_details'][0]['f_name']
# # #         user.l_name = data['user'][0]['user_details'][0]['l_name']
# # #         serialize = user_schema.dump(user).data
# # #
# # #         try:
# # #             db.session.add(user)
# # #             db.session.commit()
# # #             return json_response(status_=400, result='success', user=serialize)
# # #
# # #
# # #         except exc.SQLAlchemyError as e:
# # #             db.session.rollback()
# # #             f = exc.SQLAlchemyError._message(e)
# # #             return json_response(status_=404, result='failure', user=serialize, error=f)
# # #
# # #         # for itelating over list
# # #         # z= [key['email'] for key in b]
# # #
# # #
# # # class getall(Resource):
# # #     def get(self):
# # #         query = db.session.query(UserDetails).filter(UserDetails.user_id == User.id)
# # #         user_details = UserDetails()
# # #         user_details = query.all()
# # #         print(user_details)
# # #         return json_response(status_=400, result='success', user=userdetails_schema.dump(user_details))
# # #         # u = db.session.query(User).join(UserDetails). \
# # #         #     all()
# # #         # for c in User.__table__.constraints.:
# # #         #     print(c)
# # #
# # #         # # my_parent = db.session.query(User).all()
# # #         # # children = db.session.query(UserDetails).with_parent(my_parent).get(2)
# # #         # # print(my_parent)
# # #         # # print(children)
# # #         # # # return user_schema.dump(users).data
# # #         # print(u)
# # #
# # #         # id = [user.id for user in users]
# # #         # username = [user.username for user in users]
# # #         # password = [user.password for user in users]
# # #         # firstname = [user.userdetails.f_name for user in users]
# # #         # lastname = [user.userdetails.l_name for user in users]
# # #         # email = [user.userdetails.email for user in users]
# # #         #
# # #         # data_output = {
# # #         #     "id": id,
# # #         #     "username": username,
# # #         #     "password": password,
# # #         #     "firstname": firstname,
# # #         #     "lastname": lastname,
# # #         #     "email": email
# # #         #
# # #         # }
# # #         #
# # #         # df = pd.DataFrame(data_output, columns=["id", "username", "password", "user_details"])
# # #         # print(df)
# # #
# # #
# # # api.add_resource(adds, '/todos')
# # # api.add_resource(getall, '/todos1')
# # #
# # # if __name__ == '__main__':
# # #     db.create_all()
# # #     app.run(debug=True)
# # #
# # # # ud = UserDetails(f_name=userdata['f_name'], l_name=userdata['l_name'], email=userdata['email'])
# # # # ud = UserDetails(id=1, f_name="hero", l_name="herohero", email="h@h.com")
# # # # u = User(id=1, username="hitesh", password="testest", userdetails=[ud])
#
#
# class adds(Resource):
#     def post(self):
#         json_object = request.get_json(force=True)
#         data = dict(json_object)
#         print(data)
#
#         user_details = data['user_details']
#         for userdata in user_details:
#             ud = UserDetails()
#             ud.f_name = userdata['f_name']
#             ud.email = userdata['email']
#             ud.l_name = l_name = userdata['l_name']
#
#         u = User(username=data['username'], password=data['password'], userdetails=[ud])
#
#         u = User()
#         u.username = data['username']
#         u.password = data['password']
#         u.userdetails = [ud]
#
#         db.session.add(u)
#         db.session.commit()
#         return "user added"