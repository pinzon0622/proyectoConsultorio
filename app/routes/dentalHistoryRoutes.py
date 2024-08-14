from flask import Blueprint, request, jsonify
from app.models.dentalHistory import DentalHistory
from app.models.process import Process
from app import db
from datetime import datetime

bp = Blueprint('dentalHistory', __name__)

@bp.route('/dentalHistory', methods=['GET'])
# def getDentalHistories():
#     dhdata = DentalHistory.query.all()
#     data = [dentalHistory.to_json() for dentalHistory in dhdata]
#     return jsonify(data), 200
def getDentalHistories():
    patient_id = request.args.get('patient_id')

    query = DentalHistory.query

    if patient_id:
        query = query.filter(DentalHistory.idPatient == patient_id)

    dhdata = query.all()
    data = [dentalHistory.to_json() for dentalHistory in dhdata]
    return jsonify(data), 200

@bp.route('/dentalHistory', methods=['POST'])
def create():
    data = request.get_json()
    if not data or not all(key in data for key in ('idPatient', 'idDentist', 'date', 'diagnostic', 'observations', 'idProcess')):
        return jsonify({'error': 'Missing data'}), 400

    try:
        date = datetime.strptime(data['date'], '%Y-%m-%d').date()
    except ValueError:
        return jsonify({'error': 'Invalid date format, should be YYYY-MM-DD'}), 400

    new_dentalHistory = DentalHistory(
        idPatient=data['idPatient'],
        idDentist=data['idDentist'],
        idProcess=data['idProcess'],
        date=date,
        diagnostic=data['diagnostic'],
        observations=data['observations']
    )

            
    db.session.add(new_dentalHistory)
    db.session.commit()

    return jsonify(new_dentalHistory.to_json()), 201


@bp.route('/dentalHistory/<int:id>' , methods=['GET'])
def getDentalHistory(id):
    dentalHistory = DentalHistory.query.get(id)
    if not dentalHistory:
        return jsonify({'error': 'Dental History not found'}),404
    return jsonify(dentalHistory.to_json()),200


@bp.route('/dentalHistory/<int:id>', methods=['PUT'])
def updateDentalHistory(id):
    dentalHistory = DentalHistory.query.get(id)
    if not dentalHistory:
        return jsonify({'error': 'Dental History not found'}), 404

    data = request.get_json()
    if not data or not all(key in data for key in ('idPatient', 'idDentist', 'idProcess' , 'date', 'diagnostic', 'observations')):
        return jsonify({'error': 'Missing data'}), 400

    try:
        date = datetime.strptime(data['date'], '%Y-%m-%d').date()
    except ValueError:
        return jsonify({'error': 'Invalid date format, should be YYYY-MM-DD'}), 400

    dentalHistory.idPatient = data['idPatient']
    dentalHistory.idDentist = data['idDentist']
    dentalHistory.idProcess = data['idProcess']
    dentalHistory.date = date
    dentalHistory.diagnostic = data['diagnostic']
    dentalHistory.observations = data['observations']

    db.session.commit()

    return jsonify(dentalHistory.to_json()), 200

@bp.route('/dentalHistory/<int:id>', methods=['DELETE'])
def deleteDentalHistory(id):
    dentalHistory = DentalHistory.query.get(id)
    if not dentalHistory:
        return jsonify({'error': 'Dental History not found'}), 404

    db.session.delete(dentalHistory)
    db.session.commit()

    return jsonify(dentalHistory.to_json()), 200
