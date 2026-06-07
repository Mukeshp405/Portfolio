from datetime import datetime
from flask_login import LoginManager, UserMixin
from app import db, login

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(UserMixin, db.Model):
    """Admin user model for authentication"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Project(db.Model):
    """Project/Creation model for portfolio items"""
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(500))
    tags = db.Column(db.String(200))  # Comma-separated tags
    github_url = db.Column(db.String(500))
    live_url = db.Column(db.String(500))
    featured = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Achievement(db.Model):
    """Achievement/Quest model"""
    __tablename__ = 'achievements'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    icon = db.Column(db.String(100), default='fa-trophy')
    category = db.Column(db.String(50))  # e.g., 'work', 'learning', 'personal'
    reward = db.Column(db.String(100))  # e.g., '500 Coins'
    completed = db.Column(db.Boolean, default=True)
    completed_date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Log(db.Model):
    """Developer log/journal entries"""
    __tablename__ = 'logs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    mood = db.Column(db.String(50))  # e.g., 'productive', 'challenging', 'exciting'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class ContactMessage(db.Model):
    """Messages from contact forms"""
    __tablename__ = 'contact_messages'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    form_type = db.Column(db.String(20))  # 'hire' or 'connect'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    read = db.Column(db.Boolean, default=False)
