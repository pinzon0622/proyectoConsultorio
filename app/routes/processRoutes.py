from flask import Blueprint, request, jsonify
from app.models.process import Process
from app import db

bp = Blueprint('process', __name__)

@bp.route('/process', methods=['GET'])
def getProcesses():
    pdata = Process.query.all()
    data = [process.to_json() for process in pdata]
    return jsonify(data), 200

@bp.route('/process', methods=['POST'])
def create():
    data = request.get_json()
    if not data or not all(key in data for key in ('name', 'price', 'duration')):
        return jsonify({'error': 'Missing data'}), 400

    new_process = Process(
        name=data['name'],
        price=data['price'],
        duration=data['duration']
    )

    db.session.add(new_process)
    db.session.commit()

    return jsonify(new_process.to_json()), 201


@bp.route('/process/<int:id>' , methods=['GET'])
def getProcess(id):
    process = Process.query.get(id)
    if not process:
        return jsonify({'error': 'Process not found'}),404
    return jsonify(process.to_json()),200


@bp.route('/process/<int:id>', methods=['PUT'])
def updateProcess(id):
    process = Process.query.get(id)
    if not process:
        return jsonify({'error': 'Process not found'}), 404

    data = request.get_json()
    if not data or not all(key in data for key in ('name', 'price', 'duration')):
        return jsonify({'error': 'Missing data'}), 400

    process.name = data['name']
    process.price = data['price']
    process.duration = data['duration']

    db.session.commit()

    return jsonify(process.to_json()), 200

@bp.route('/process/<int:id>', methods=['DELETE'])
def deleteProcess(id):
    process = Process.query.get(id)
    if not process:
        return jsonify({'error': 'Process not found'}), 404

    db.session.delete(process)
    db.session.commit()

    return jsonify({'message': 'Process deleted'}), 200


