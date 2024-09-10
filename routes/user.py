from flask_restx import Namespace, Resource, fields
from flask import request

from models import User

user_ns = Namespace('user', description='Authentication related operations')


register_model = user_ns.model('register_model', {
   # 'id': fields.Integer(readonly=True, description='The item unique identifier'),
    'name': fields.String(required=True, description='The item name'),
    'email': fields.String(required=True, description='The item email'),
})

@user_ns.route('/register')
class Register(Resource):

    @user_ns.expect(register_model, validate=True)
    def post(self):

        try:
            new_user = User(name=request.json['name'], email=request.json['email'])

            new_user.save()

            return {"success": True,
                "msg": "The user was successfully registered"}, 200
    
        except Exception as err:
            new_user.rollback()
            return {"error": f"Error: {err}"}, 500
