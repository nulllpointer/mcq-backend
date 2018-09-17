from settings import ma
from marshmallow import Schema, fields, pprint
from model import *
class UserSchema(ma.ModelSchema):
    class Meta:
        model = User

        # fields = ('username', 'password')

class UserDetailsSchema(ma.ModelSchema):
    user = fields.Nested(UserSchema)
    class Meta:
        model = UserDetails
        # fields = ('user_id', 'email', 'f_name', 'l_name')


class ErrorSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('email','username')


# userdetails_schema = UserDetailsSchema()
# userdetailss_schema = UserDetailsSchema(many=True)

# error_schema = ErrorSchema()
