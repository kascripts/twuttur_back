from http import HTTPStatus
from flask import Blueprint, request
from models.user import UserModel
from serializers.user import UserSchema
from marshmallow.exceptions import ValidationError

user_schema = UserSchema()

router = Blueprint("users", __name__)

@router.route('/register', methods=["POST"])
def register():
    print(request.json)
    try:
        user_dictionary = request.json
        user = user_schema.load(user_dictionary)
        user.save()
        return user_schema.jsonify(user)
    except ValidationError as e:
        return {"errors": e.messages, "messages": "Something went wrong2"}
    except Exception as e:
        print(e)
        return { "messages": "Something went wrong7"}
    
    
@router.route('/login', methods=["POST"])
def login():
    try:
        credentials_dictionary = request.json

        
        user = UserModel.query.filter_by(email=credentials_dictionary["email"]).first()
        print(user)
        if not user:
            return {"message": "No user found for this email"}
        
        if not user.validate_password(credentials_dictionary["password"]):
            return {"message": "You are not authorized"}, HTTPStatus.UNAUTHORIZED
        
        token = user.generate_token()
        return {"token": token, "message": "Welcome back!"}
    
    except Exception as e:
        return { "messages": "Something went wrong" }
        