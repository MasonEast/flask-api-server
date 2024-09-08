# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import logging, json

from flask import Flask, request, jsonify
from flask_cors import CORS

from config import Config
from models.models import db, User

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()  # 创建所有表
       

# 路由：写数据到 MySQL 数据库
@app.route('/add', methods=['POST'])
def add_data():
    name = request.form.get('name')
    email = request.form.get('email')

    if not name or not email:
        return jsonify({"error": "name and email are required!"}), 400

    try:
        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "Data added successfully!"}), 201

    except Exception as err:
        db.session.rollback()
        return jsonify({"error": f"Error: {err}"}), 500