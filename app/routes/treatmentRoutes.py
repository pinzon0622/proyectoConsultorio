from flask import Blueprint, request, jsonify
from app.models.treatment import Treatment
from app import db
from datetime import datetime

bp = Blueprint('treatment', __name__)

@bp.route('/treatment', methods=['GET'])
def getTreatments():
    tdata = Treatment.query.all()
    data = [treatment.to_json() for treatment in tdata]
    return jsonify(data), 200

@bp.route('/treatment', methods=['POST'])
def create():
    data = request.get_json()
    if not data or not all(key in data for key in ('idPatient', 'idDentist', 'description', 'initDate', 'endDate')):
        return jsonify({'error': 'Missing data'}), 400

    try:
        initDate = datetime.strptime(data['initDate'], '%Y-%m-%d').date()
        endDate = datetime.strptime(data['endDate'], '%Y-%m-%d').date()
    except ValueError:
        return jsonify({'error': 'Invalid date format'}), 400
    
    new_treatment = Treatment(
        idPatient=data['idPatient'],
        idDentist=data['idDentist'],
        description=data['description'],
        initDate=initDate,
        endDate=endDate
    )

    db.session.add(new_treatment)
    db.session.commit()

    return jsonify(new_treatment.to_json()), 201


@bp.route('/treatment/<int:id>' , methods=['GET'])
def getTreatment(id):
    treatment = Treatment.query.get(id)
    if not treatment:
        return jsonify({'error': 'Treatment not found'}),404
    return jsonify(treatment.to_json()),200


@bp.route('/treatment/<int:id>', methods=['PUT'])
def updateTreatment(id):
    treatment = Treatment.query.get(id)
    if not treatment:
        return jsonify({'error': 'Treatment not found'}), 404
    
    data = request.get_json()
    if not data or not all(key in data for key in ('idPatient', 'idDentist', 'description', 'initDate', 'endDate')):
        return jsonify({'error': 'Missing data'}), 400
    
    try:
        initDate = datetime.strptime(data['initDate'], '%Y-%m-%d').date()
        endDate = datetime.strptime(data['endDate'], '%Y-%m-%d').date()
    except ValueError:
        return jsonify({'error': 'Invalid date format'}), 400
    
    treatment.idPatient = data['idPatient']
    treatment.idDentist = data['idDentist']
    treatment.description = data['description']
    treatment.initDate = initDate
    treatment.endDate = endDate

    db.session.commit()

    return jsonify(treatment.to_json()), 200

@bp.route('/treatment/<int:id>', methods=['DELETE'])
def deleteTreatment(id):
    treatment = Treatment.query.get(id)
    if not treatment:
        return jsonify({'error': 'Treatment not found'}), 404

    db.session.delete(treatment)
    db.session.commit()

    return jsonify(treatment.to_json()), 200