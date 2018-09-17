from flask import Flask
from flask_cors import CORS
from flask_json import FlaskJSON
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12qw12qw@localhost:3306/test'
db = SQLAlchemy(app)
json = FlaskJSON(app)
ma = Marshmallow(app)
CORS(app)

