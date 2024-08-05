from flask import Blueprint, request, jsonify
from app.models.user import User
from app import db

bp = Blueprint('user', __name__)

@bp.route('/user', methods=['GET'])
def getUsers():
    udata = User.query.all()
    data = [user.to_json() for user in udata]
    return jsonify(data), 200

@bp.route('/user', methods=['POST'])
def create():
    data = request.get_json()  
    if not data or not all(key in data for key in ('username', 'email', 'password')):
        return jsonify({'error': 'Missing data'}), 400

    new_user = User(
        username=data['username'],
        email=data['email'],
        password=data['password']
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.to_json()), 201


@bp.route('/user/<int:id>', methods=['GET'])
def getUser(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user.to_json()), 200


@bp.route('/user/<int:id>', methods=['PUT'])
def updateUser(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    data = request.get_json()
    if not data or not all(key in data for key in ('username', 'email')):
        return jsonify({'error': 'Missing data'}), 400
    
    user.username = data['username']
    user.email = data['email']
    
    db.session.commit()

    return jsonify(user.to_json()), 200

@bp.route('/user/<int:id>', methods=['DELETE'])
def deleteUser(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify(user.to_json()), 200


@bp.route('/user/changePassword/<int:id>', methods=['PUT'])
def change_password(id):
    user = User.query.get(id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    data = request.get_json()
    if not data or not all(key in data for key in ( 'oldpassword', 'password')):
        return jsonify({'error': 'Missing data'}), 400

    if (user.password == data['oldpassword']):
        user.password = data['password']
    else:
        return jsonify({'error' : 'password no equals'}),400
    
    db.session.commit()

    return jsonify({
        "idUser": user.idUser,
        "username": user.username,
        "email": user.email,
    }), 200