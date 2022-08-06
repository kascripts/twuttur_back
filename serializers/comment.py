from app import ma 
from models.comment import CommentModel

from marshmallow import fields


class CommentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CommentModel
        load_instance = True
        
    
    user = fields.Nested("UserSchema", many=False)