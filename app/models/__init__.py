from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User, JWTTokenBlocklist
from .article import Article, Comment

