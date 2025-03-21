from fully import db,app
from fully.models import User

def create_admin():
    with app.app_context():
        users = User.query.all()
        for user in users:
            print(f"ID: {user.id}, Username: {user.username}, Level: {user.level}")

def delete_user(username):
    with app.app_context():
        user = User.query.filter_by(username=username).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            print(f"User '{username}' deleted successfully.")
        else:
            print(f"User '{username}' not found.")


if __name__ == "__main__":
    create_admin()
    #delete_user("alx203")