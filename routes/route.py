from flask_restx import  Resource, fields
from flask import jsonify, request

# from routes import api
from models import User
from flask_restx import Api

api = Api(version='1.0', title='Sample API')

register_model = api.model('register_model', {
   # 'id': fields.Integer(readonly=True, description='The item unique identifier'),
    'name': fields.String(required=True, description='The item name'),
    'email': fields.String(required=True, description='The item email'),
})

@api.route('/register')
class Register(Resource):

    @api.expect(register_model, validate=True)
    def post(self):

        try:
            new_user = User(name=request.json['name'], email=request.json['email'])

            new_user.save()

            return {"success": True,
                "msg": "The user was successfully registered"}, 200
    
        except Exception as err:
            new_user.rollback()
            return {"error": f"Error: {err}"}, 500

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
    
    
