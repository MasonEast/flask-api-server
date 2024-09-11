
from flask_restx import Namespace, Resource, fields
from flask import request

from app.models import User
from utils import HashBcrypt, Times

user_ns = Namespace('user', description='用户')

register_model = user_ns.model('register_model', {
    'username': fields.String(required=True, description='账号'),
    'email': fields.String(required=True, description='邮箱'),
    'nickname': fields.String(required=True, description='名称'),
    'password_hash': fields.String(required=True, description='密码hash值'),

    'status': fields.Integer(required=False, description='状态'),
    'create_time': fields.String(required=False, description='创建时间'),
    'last_login_time': fields.String(required=False, description='最后登录时间'),

    'phone': fields.String(required=False, description='手机号'),
    'avatar_url': fields.String(required=False, description='头像'),
    'birthday': fields.Date(required=False, description='生日'),
    'gender': fields.String(required=False, description='性别'),
    'intro': fields.String(required=False, description='简介'),

})

@user_ns.route('/register')
class Register(Resource):

    @user_ns.expect(register_model, validate=True)
    def post(self):

        try:
            request.json['password_hash'] = HashBcrypt.hash(request.json['password_hash'])

            now = Times.now()
            request.json['create_time'] = now
            request.json['last_login_time'] = now
            request.json['status'] = 0

            new_user = User(**request.json)

            new_user.save()

            return {"success": True,
                "msg": "The user was successfully registered"}, 200
    
        except Exception as err:
            new_user.rollback()
            return {"error": f"Error: {err}"}, 500
