from marshmallow import fields

from app import ma 
from models.user import UserModel

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        load_instance = True
        exclude = ("password_hash",)
        load_only = ('email', 'password')
        
    password = fields.String(required=True)
    