import jwt
from datetime import timedelta

from flask_restx import Namespace, Resource, fields
from flask import request

from app.models import User
from utils import HashBcrypt, Times, Valid
from config import Config

user_ns = Namespace('user', description='用户')

register_model = user_ns.model('register_model', {
    'username': fields.String(required=False, description='账号'),
    'email': fields.String(required=True, description='邮箱'),
    'nickname': fields.String(required=True, description='名称'),
    'password': fields.String(required=True, description='密码'),

    'status': fields.Integer(required=False, description='状态'),
    'create_time': fields.String(required=False, description='创建时间'),
    'last_login_time': fields.String(required=False, description='最后登录时间'),

    'phone': fields.String(required=False, description='手机号'),
    'avatar_url': fields.String(required=False, description='头像'),
    'birthday': fields.Date(required=False, description='生日'),
    'gender': fields.String(required=False, description='性别'),
    'intro': fields.String(required=False, description='简介'),
})

login_modal = user_ns.model('login_modal', {
    'username': fields.String(required=True, description='账号'), # 使用邮箱或手机号替代用户名做登录
    'password': fields.String(required=True, description='密码'),
})

@user_ns.route('/register')
class Register(Resource):

    @user_ns.expect(register_model, validate=True)
    def post(self):

        try:
            data = request.json
            data['password'] = HashBcrypt.hash(data['password'])

            now = Times.now()
            data['create_time'] = now
            data['last_login_time'] = now
            data['status'] = 0

            new_user = User(**data)

            new_user.save()

            return {"success": True,
                "msg": "注册成功"}, 200
    
        except Exception as err:
            new_user.rollback()
            return {"error": f"Error: {err}"}, 500

@user_ns.route('/login')
class Login(Resource):
    @user_ns.expect(login_modal, validate=True)
    def post(self):
        username = request.json['username']
        password = request.json['password']

        user = ''
        # 校验使用的是手机号还是邮箱
        if Valid.valid_email(username):
            user = User.get_by_email(username)

        elif Valid.valid_phone(username):
            user = User.get_by_phone(username)
        else:
            return {"success": False,
                "msg": "请输入正确格式的邮箱或手机号"}, 400
        
        # 校验账号是否存在
        if not user:
                return {"success": False,
                "msg": "您输入的邮箱或手机号不存在，请确认该账号是否注册"}, 400
        
        # 校验密码
        if not user.check_password(password):
                return {"success": False,
                "msg": "密码错误，请确认密码是否输入正确"}, 400
            
        # 使用jwt创建token
        token = jwt.encode({'username': username, 'exp': Times.nowUTC() + timedelta(minutes=Config.EXPIRE_MINUTES)}, Config.SECRET_KEY)

        user.set_status(1)
        user.save()

        return {"success": True,
                "token": token,
                "user": user.toJSON()}, 200
