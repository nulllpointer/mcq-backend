from flask import request
from flask_json import json_response
from flask_restful import Resource

import restapihandler


class add(Resource):
    def post(self):
        json_object = request.get_json(force=True)
        # data = dict(json_object)
        return restapihandler.UserHandler.create_user(self, json_object)

class getall(Resource):
    def get(self):
        return restapihandler.UserHandler.getall(self)


class sayHi(Resource):
    def get(self):
        return json_response(status_=200)










# api.add_resource(add, '/add')
# api.add_resource(getall, '/get')
# api.add_resource(sayHi, '/hello')



# ud = UserDetails(f_name=userdata['f_name'], l_name=userdata['l_name'], email=userdata['email'])
# ud = UserDetails(id=1, f_name="hero", l_name="herohero", email="h@h.com")
# u = User(id=1, username="hitesh", password="testest", userdetails=[ud])
