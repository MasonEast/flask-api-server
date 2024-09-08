from flask_restx import  Resource

from models.user import  item_model
from models import api
from flask import request

ns = api.namespace('items', description='Item operations')

db = []
@ns.route('/register')
class Register(Resource):

    @ns.expect(item_model, validate=True)

    def post(self):
        '''Create a new item'''
        new_item = {
            'id': len(db) + 1,
            'name': request.json['name']
        }
        db.append(new_item)
        return new_item, 201

# 将命名空间添加到API中
api.add_namespace(ns)


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}