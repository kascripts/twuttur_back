from http import HTTPStatus
import json
from flask import Blueprint, request, g
from marshmallow.exceptions import ValidationError
from middleware.secure_route import secure_route
from models.status import StatusModel
from serializers.user import UserSchema
from serializers.status import StatusSchema
from serializers.comment import CommentSchema
from models.comment import CommentModel
# from models.likes import LikesModel



status_schema = StatusSchema()
comment_schema = CommentSchema()


router = Blueprint("status", __name__)


@router.route("/status", methods=["GET"])
def get_status():
    status = StatusModel.query.all()
    
    return status_schema.jsonify(status, many=True), HTTPStatus.OK




@router.route("/status/<int:status_id>", methods=["GET"])
def get_single_status(status_id):
    status = StatusModel.query.get(status_id)
    
    if not status:
        return {"message": "Status not found"}, HTTPStatus.NOT_FOUND    
    
    return status_schema.jsonify(status), HTTPStatus.OK



@router.route("/status", methods=["POST"])
def create_status():
    status_dictionary = request.json
    
    try:
        status = status_schema.load(status_dictionary)
    except ValidationError as e:
        return {"errors": e.messages, "message": "Something went wrong"}
    
    
    
    status.user_id = g.current_user.id
    status.save()
    
    return status_schema.jsonify(status), HTTPStatus.CREATED


@router.route("/status/<int:status_id>", methods=["DELETE"])
@secure_route
def remove_status(status_id):
    status = StatusModel.query.get(status_id)
    
    if not status:
        return {"message": "Status not found"}, HTTPStatus.NOT_FOUND
    
    status.remove()
    
    return '', HTTPStatus.NO_CONTENT



@router.route("/status/<int:status_id>/comments", methods=["POST"])
@secure_route
def create_comment(status_id):
    
    comment_dictionary = request.json
    
    try:
        comment = comment_schema.load(comment_dictionary)

    except ValidationError as e:
        return {"errors": e.messages, "message": "Something went wrong"}

    comment.status_id = status_id
    comment.user_id = g.current_user.id
    comment.save()
    
    return comment_schema.jsonify(comment), HTTPStatus.CREATED


@router.route("/status/<int:status_id>/comments/<int:comment_id>", methods=["DELETE"])
@secure_route
def remove_comment(status_id, comment_id):

    comment = CommentModel.query.get(comment_id)
    
    if not comment:
        return {"message": "Comment not found"}, HTTPStatus.NOT_FOUND
    
    comment.remove()
    
    status = StatusModel.query.get(status_id)

    if not status:
        return {"message": "Status not found"}, HTTPStatus.NOT_FOUND
    
    return comment_schema.jsonify(status), HTTPStatus.OK



    
        
#     #! Likes route unresolved
# # @router.route("/status/<int:status_id>/likes/<int:like_id>", methods=["POST"])
# # @secure_route
# # def create_status_like(status_id, like_id):
    
# #     status = StatusModel.query.get(status_id)
    
# #     like = LikesModel.query.get(like_id)
    
# #     if not like or not status:
# #         return {"message": "Item not found"}, HTTPStatus.NOT_FOUND
    
    
# #     status.likes.append(like)
    
# #     status.save()
    
# #     return status_schema.jsonify(status), HTTPStatus.OK
    
    
    
# # @router.route("/status/<int:status_id>/likes/<int:like_id>/comments/<int:comment_id>", methods=["POST"])
# # @secure_route
# # def create_comment_like(status_id, like_id, comment_id): #! not sure if we need status/ID
    
# #     comment = StatusModel.query.get(comment_id)
    
# #     like = LikeModel.query.get(like_id)
    
# #     if not like or not comment:
# #         return {"message": "Item not found"}, HTTPStatus.NOT_FOUND
    
    
# #     comment.likes.append(like)
    
# #     comment.save()
    
# #     return status_schema.jsonify(comment), HTTPStatus.OK
        
    
    
    

