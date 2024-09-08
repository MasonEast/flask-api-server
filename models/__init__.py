from flask_sqlalchemy import SQLAlchemy

from flask_restx import Api, Resource, fields

db = SQLAlchemy()

api = Api(version='1.0', title='Sample API')

from flask_restx import  Resource

# from models.user import  item_model
from flask import request

item_model = api.model('Item', {
    'id': fields.Integer(readonly=True, description='The item unique identifier'),
    'name': fields.String(required=True, description='The item name')
})

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
    
db = []

@api.route('/register')
class Register(Resource):

    @api.expect(item_model, validate=True)

    def post(self):
        '''Create a new item'''
        new_item = {
            'id': len(db) + 1,
            'name': request.json['name']
        }
        db.append(new_item)
        return db, 201

# # 路由：写数据到 MySQL 数据库
# @app.route('/add', methods=['POST'])
# def add_data():
#     name = request.form.get('name')
#     email = request.form.get('email')

#     bool, message, code = Message.isExist(name, email)
#     if not bool:
#         return message, code

#     try:
#         new_user = User(name=name, email=email)
#         new_user.save()

#         return jsonify({"message": "Data added successfully!"}), 201

#     except Exception as err:
#         db.session.rollback()
#         return jsonify({"error": f"Error: {err}"}), 500
    