
from dotenv import load_dotenv

# 在加载flask应用之前加载.env文件
load_dotenv()

from flask import Flask, request, jsonify
from flask_cors import CORS

from config import Config
from models.models import db, User
from utils.util import Message

app = Flask(__name__)

app.config.from_object(Config)
# 启用 debug 模式
app.config['DEBUG'] = True

db.init_app(app)
       
# 路由：写数据到 MySQL 数据库
@app.route('/add', methods=['POST'])
def add_data():
    name = request.form.get('name')
    email = request.form.get('email')

    bool, message, code = Message.isExist(name, email)
    if not bool:
        return message, code

    try:
        new_user = User(name=name, email=email)
        new_user.save()

        return jsonify({"message": "Data added successfully!"}), 201

    except Exception as err:
        db.session.rollback()
        return jsonify({"error": f"Error: {err}"}), 500
    

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # 创建所有表
    app.run(debug=True)