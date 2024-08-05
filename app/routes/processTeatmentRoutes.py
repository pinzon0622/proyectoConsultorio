from flask import Blueprint, request, jsonify
from app.models.processTreatment import ProcessTreatment
from app.models.process import Process
from app.models.treatment import Treatment
from app import db

bp = Blueprint('processTreatment', __name__)

@bp.route('/processTreatment', methods=['GET'])
# def getProcessTreatments():
#     pdata = ProcessTreatment.query.all()
#     data = [processTreatment.to_json() for processTreatment in pdata]
#     return jsonify(data), 200
def getProcessTreatments():
    pdata = ProcessTreatment.query.all()
    data = [processTreatment.to_json() for processTreatment in pdata]
    return jsonify(data), 200

@bp.route('/processTreatment', methods=['POST'])
def create():
    data = request.get_json()
    if not data or not all(key in data for key in ('processes', 'treatments')):
        return jsonify({'error': 'Missing data'}), 400

    new_processTreatment = ProcessTreatment(
        processes=data['processes'],
        treatments=data['treatments']
    )

    db.session.add(new_processTreatment)
    db.session.commit()

    return jsonify(new_processTreatment.to_json()), 201
# def create():
#     data = request.get_json()
#     if not data or not all(key in data for key in ('processes', 'treatments')):
#         return jsonify({'error': 'Missing data'}), 400

#     process = Process.query.get(data['processes'])
#     treatment = Treatment.query.get(data['treatments'])

#     if not process or not treatment:
#         return jsonify({'error': 'Invalid processes or treatments'}), 400

#     new_processTreatment = ProcessTreatment(
#         process=process,
#         treatment=treatment
#     )

#     db.session.add(new_processTreatment)
#     db.session.commit()

#     return jsonify(new_processTreatment.to_json()), 201

@bp.route('/processTreatment/<int:id>' , methods=['GET'])
def getProcessTreatment(id):
    processTreatment = ProcessTreatment.query.get(id)
    if not processTreatment:
        return jsonify({'error': 'Process Treatment not found'}), 404
    return jsonify(processTreatment.to_json()), 200


@bp.route('/processTreatment/<int:id>', methods=['PUT'])
def updateProcessTreatment(id):
    processTreatment = ProcessTreatment.query.get(id)
    if not processTreatment:
        return jsonify({'error': 'Process Treatment not found'}), 404

    data = request.get_json()
    if not data or not all(key in data for key in ('process', 'treatment')):
        return jsonify({'error': 'Missing data'}), 400

    processTreatment.process = data['process']
    processTreatment.treatment = data['treatment']

    db.session.commit()

    return jsonify(processTreatment.to_json()), 200
# def updateProcessTreatment(id):
#     processTreatment = ProcessTreatment.query.get(id)
#     if not processTreatment:
#         return jsonify({'error': 'Process Treatment not found'}), 404

#     data = request.get_json()
#     if not data or not all(key in data for key in ('processes', 'treatments')):
#         return jsonify({'error': 'Missing data'}), 400

#     process = Process.query.get(data['processes'])
#     treatment = Treatment.query.get(data['treatments'])

#     if not process or not treatment:
#         return jsonify({'error': 'Invalid processes or treatments'}), 400

#     processTreatment.process = process
#     processTreatment.treatment = treatment

#     db.session.commit()

#     return jsonify(processTreatment.to_json()), 200


@bp.route('/processTreatment/<int:id>', methods=['DELETE'])
def deleteProcessTreatment(id):
    processTreatment = ProcessTreatment.query.get(id)
    if not processTreatment:
        return jsonify({'error': 'Process Treatment not found'}), 404

    db.session.delete(processTreatment)
    db.session.commit()

    return jsonify({'message': 'Process Treatment deleted'}), 200