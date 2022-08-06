from app import app, db

from models.status_data import status_list, comments_list
from models.user_data import user_list

with app.app_context():
    print("bye")
    try:
        print("Recreating Database ... ")
        db.drop_all()
        db.create_all()
        
        print("seeding our database..")
        
        db.session.add_all(user_list)
        db.session.commit()
        
        db.session.add_all(status_list)
        db.session.commit()
        
        db.session.add_all(comments_list)
        db.session.commit()
        
        print("bye")
    except Exception as e:
        print(e)