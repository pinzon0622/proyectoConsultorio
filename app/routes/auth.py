from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from app.models import User

bp = Blueprint('auth',__name__)


@bp.route('/login', methods=['POST'])
def login():
   udata = User.query.all()

   data = request.get_json()
   usernameDto = data['username']
   passwordDto = data['password']

   for user_data in udata:
       user = user_data.username
       password = user_data.password

   if user == usernameDto and password == passwordDto :
      access_token = create_access_token(identity={'username': user})
      return jsonify(access_token=access_token), 200
   else:
      return jsonify({"error": "Bad username or password"}), 401
   

@bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200