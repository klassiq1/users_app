from fully import db,app
from fully.models import User
from werkzeug.security import generate_password_hash

def create_admin():
    with app.app_context():
        username = "admin"
        password = generate_password_hash("admin123")
        level = 1  # Highest access level

        first_user = User(username=username, password=password, level=level)
        db.session.add(first_user)
        db.session.commit()
        print("Admin user created successfully!")

if __name__ == "__main__":
    create_admin()
