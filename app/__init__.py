# ----------- Application Extensions ----------- #
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_ckeditor import CKEditor

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
ckeditor = CKEditor()


def register_extensions(app):
    """
    Register your flask extensions
    """
    db.init_app(app)
    login.init_app(app)
    migrate.init_app(app, db)
    ckeditor.init_app(app)

    # Login configurations
    login.login_view = 'dashboard.login'
    login.login_message = 'Please log in to access the admin panel.'


# ----------- Application Blueprints ----------- #
def register_blueprints(app):
    """
    Register your application blueprints
    """
    from app.dashboard.routes import dashboard

    app.register_blueprint(dashboard)


# ----------- Instantiate Application ----------- #
def create_app():
    from flask import Flask

    app = Flask(__name__)

    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    instance_path = os.path.join(BASE_DIR, "instance")

    if not os.path.exists(instance_path):
        os.makedirs(instance_path)

    db_path = os.path.join(instance_path, "portfolio.db")
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-key-change-in-production")

    register_extensions(app)

    with app.app_context():
        register_blueprints(app)

    return app
