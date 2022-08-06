from app import ma 
from models.status import StatusModel
from marshmallow import fields

class StatusSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = StatusModel
        load_instance = True
        
    comments = fields.Nested("CommentSchema", many=True)
    # likes = fields.Nested("LikeSchema", many=True)
    user = fields.Nested("UserSchema", many=False)
        

