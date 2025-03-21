from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_login import LoginManager





app = Flask(__name__)
app.config['SECRET_KEY'] = '842a6f0f8f9bd09dba31b0c77755bd255d62be36407719d643096087de8878ec'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['JWT_SECRET_KEY'] = 'supersecretkey'


db = SQLAlchemy(app)
jwt = JWTManager(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'




from fully import routes
