from model import *
from settings import app,db
from routes import *
from restapi import *
from restapihandler import *
from jsonhandler import *




# def create_tables():
#     # Create table for each model if it does not exist.
#     # Use the underlying peewee database object instead of the
#     # flask-peewee database wrapper:
#     db.database.create_tables([User], safe=True)

if __name__ == '__main__':
    db.create_all()
    routes(self=None)
    app.run(debug=True)
    # app.run()
