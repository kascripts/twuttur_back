from http import HTTPStatus
import jwt
from functools import wraps
from flask import request, g
from models.user import UserModel
from config.environment import secret

def secure_route(route_func):
    @wraps(route_func)
    def decorated_function(*args, **kwargs):
        raw_token = request.headers.get("Authorization")
        
        if not raw_token:
            return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED
        clean_token = raw_token.replace("Bearer ", "")
        
        try:
            payload = jwt.decode(clean_token, secret, "HS256")
            user_id = payload["sub"]
            user = UserModel.query.get(user_id)
            
            if not user:
                return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED
            
            g.current_user = user
            
        except jwt.ExpiredSignatureError:
            return {"message": "Token has expired"}, HTTPStatus.UNAUTHORIZED
        
        except Exception as e:
            return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED
        
        return route_func(*args, **kwargs)
    
    return decorated_function