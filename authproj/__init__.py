from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret12345'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flas.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/flasklog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
csrf = CSRFProtect(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


migrate = Migrate(app,db)
from authproj import routes