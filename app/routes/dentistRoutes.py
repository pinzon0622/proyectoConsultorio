from flask import Blueprint,  request, jsonify
from app.models.dentist import Dentist
from app import db

bp = Blueprint('dentist', __name__)

@bp.route('/dentist', methods=['GET'])
def getDentists():
    ddata = Dentist.query.all()
    data = [dentist.to_json() for dentist in ddata]
    return jsonify(data), 200

@bp.route('/dentist', methods=['POST'])
def create():
    data = request.get_json()  
    if not data or not all(key in data for key in ('name', 'specialty', 'phone', 'email')):
        return jsonify({'error': 'Missing data'}), 400

    new_dentist = Dentist(
        name=data['name'],
        specialty=data['specialty'],
        phone=data['phone'],
        email=data['email']
    )

    db.session.add(new_dentist)
    db.session.commit()

    return jsonify(new_dentist.to_json()), 201

@bp.route('/dentist/<int:id>', methods=['GET'])
def getDentist(id):
    dentist = Dentist.query.get(id)
    if not dentist:
        return jsonify({'error': 'Dentist not found'}), 404
    return jsonify(dentist.to_json()), 200


@bp.route('/dentist/<int:id>', methods=['PUT'])
def updateDentist(id):
    dentist = Dentist.query.get(id)
    if not dentist:
        return jsonify({'error': 'Dentist not found'}), 404

    data = request.get_json()
    if not data or not all(key in data for key in ('name', 'specialty', 'phone', 'email')):
        return jsonify({'error': 'Missing data'}), 400
    
    dentist.name = data['name']
    dentist.specialty = data['specialty']
    dentist.phone = data['phone']
    dentist.email = data['email']
    
    db.session.commit()
    return jsonify(dentist.to_json()), 200

@bp.route('/dentist/<int:id>', methods=['DELETE'])
def deleteDentist(id):
    dentist = Dentist.query.get(id)
    if not dentist:
        return jsonify({'error': 'Dentist not found'}), 404
    db.session.delete(dentist)
    db.session.commit()
    return jsonify({'message': 'Dentist deleted'}), 200

