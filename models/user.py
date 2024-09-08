from flask_restx import Api, Resource, fields

from models import api

# 定义数据模型
item_model = api.model('Item', {
    'id': fields.Integer(readonly=True, description='The item unique identifier'),
    'name': fields.String(required=True, description='The item name')
})