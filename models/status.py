from app import db 
from models.base import BaseModel
# from models.status_like import status_like
# from models.likes import LikesModel
from models.comment import CommentModel
from models.user import UserModel

class StatusModel(db.Model, BaseModel):
    
    __tablename__ = "status"

    text = db.Column(db.Text, nullable=False, unique=False)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    # comment = db.Column(db.Text, nullable=False, unique=False) // make a connection between comments and status = like the teas file

    user = db.relationship('UserModel', backref='users')
    
    comment = db.relationship('CommentModel', backref='comment', cascade="all, delete")
    
    # likes = db.relationship('LikesModel', backref='likes', secondary=status_like)
    
    # comments = db.relationship('CommentsModel', backref='comments', secondary="status_comments")