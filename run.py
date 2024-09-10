
from dotenv import load_dotenv

# 在加载flask应用之前加载.env文件
load_dotenv()
       
from flask import Flask

from config import Config
from models import db
from routes import register_namespace

# from routes.route import api
from flask_restx import Api

app = Flask(__name__)

app.config.from_object(Config)


db.init_app(app)

api = Api(version='1.0', title='Sample API')
register_namespace(api)
# api.init_app(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # 创建所有表
    app.run(debug=True)