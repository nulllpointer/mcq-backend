from settings import api
from restapi import *


def routes(self):
    api.add_resource(add, '/add')
    api.add_resource(getall, '/get')
    api.add_resource(sayHi, '/hello')
