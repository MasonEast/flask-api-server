from flask import Flask
from flask_restx import Api
from app.routes import register_namespaces
from app.models import db

from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # 初始化数据库
    db.init_app(app)

    # 初始化 Flask-RESTx API
    api = Api(app, version='1.0', title='My API', description='A simple demonstration API')

    # 注册命名空间
    register_namespaces(api)

    with app.app_context():
        db.create_all()  # 创建所有表
    
    return app