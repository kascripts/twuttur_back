# from http import HTTPStatus

# from flask import Blueprint, request
# # from models.likes import LikeModel
# from marshmallow.exceptions import ValidationError
# # from serializers.like import LikeSchema

# like_schema = LikeSchema()

# router = Blueprint("likes", __name__)


# @router.route("/likes", methods=["POST"])
# def create_like():
#     like_dictionary = request.json

#     try:
#         like = like_schema.load(like_dictionary)
#     except ValidationError as e:
#         return {"errors": e.messages, "messages": "Something went wrong"}

#     like.save()

#     return like_schema.jsonify(like)


# @router.route("/likes/<int:like_id>", methods=["DELETE"])
# def remove_note(like_id):
#     like = LikeModel.query.get(like_id)

#     if not like:
#         return {"message": "Like not found"}, HTTPStatus.NOT_FOUND

#     like.remove()

#     return '', HTTPStatus.NO_CONTENT
