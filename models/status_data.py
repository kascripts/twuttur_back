from models.status import StatusModel
from models.comment import CommentModel
# from models.likes import LikesModel


# upvote_like = LikesModel(name="upvote")
# unvote_like = LikesModel(name="unvote")


status_list = [
    StatusModel(user_id=1, text="Th3y sh0vldv3 c@st Z3nd@yA t0 pl@y M@r1lyn0101010101popopasdasd"), #!likes=[upvote_like]
    StatusModel(user_id=2, text="npm 1nst@ll brvnch")   #! likes=[upvote_like]
    ] 

comments_list = [CommentModel(content="npm 1nst@ll sn@cks", status_id=2, user_id=2)]

