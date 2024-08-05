from flask import Blueprint,  request, jsonify
from app.models.patient import Patient
from datetime import datetime
from app import db

bp = Blueprint('patient', __name__)

@bp.route('/patient', methods=['GET'])
def getPatients():
    pdata = Patient.query.all()
    data = [patient.to_json() for patient in pdata]
    return jsonify(data), 200

@bp.route('/patient', methods=['POST'])
def create():
    data = request.get_json()  
    if not data or not all(key in data for key in ('name', 'birthdate', 'direction', 'phone', 'email')):
        return jsonify({'error': 'Missing data'}), 400

    try:
        birthdate = datetime.strptime(data['birthdate'], '%Y-%m-%d').date()
    except ValueError:
        return jsonify({'error': 'Invalid birthdate format, should be YYYY-MM-DD'}), 400

    new_patient = Patient(
        name=data['name'],
        birthdate=birthdate,
        direction=data['direction'],
        phone=data['phone'],
        email=data['email']
    )

    db.session.add(new_patient)
    db.session.commit()

    return jsonify(new_patient.to_json()), 201

@bp.route('/patient/<int:id>', methods=['GET'])
def getPatient(id):
    patient = Patient.query.get(id)
    if not patient:
        return jsonify({'error': 'Patient not found'}), 404
    return jsonify(patient.to_json()), 200


@bp.route('/patient/<int:id>', methods=['PUT'])
def updatePatient(id):
    patient = Patient.query.get(id)
    if not patient:
        return jsonify({'error': 'Patient not found'}), 404

    data = request.get_json()
    if not data or not all(key in data for key in ('name', 'birthdate', 'direction', 'phone', 'email')):
        return jsonify({'error': 'Missing data'}), 400
    
    patient.name = data['name']
    patient.direction = data['direction']
    patient.phone = data['phone']
    patient.email = data['email']
    
    try:
        patient.birthdate = datetime.strptime(data['birthdate'], '%Y-%m-%d').date()
    except ValueError:
        return jsonify({'error': 'Invalid birthdate format, should be YYYY-MM-DD'}), 400
    
    db.session.add(patient)

    db.session.commit()

    return jsonify(patient.to_json()), 200


@bp.route('/patient/<int:id>', methods=['DELETE'])
def deletePatient(id):
    patient = Patient.query.get(id)
    if not patient:
        return jsonify({'error': 'Patient not found'}), 404

    db.session.delete(patient)
    db.session.commit()

    return jsonify({'message': 'Patient deleted'}), 200