from flask import Blueprint, request, jsonify
from app.models.date import Date
from app import db
from datetime import datetime

bp = Blueprint('date', __name__)

@bp.route('/date', methods=['GET'])
def getDates():
    date_str = request.args.get('date')

    query = Date.query

    if date_str:
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            query = query.filter(Date.date == date)
        except ValueError:
            return jsonify({'error': 'Invalid date format, should be YYYY-MM-DD'}), 400

    ddata = query.all()
    data = [date.to_json() for date in ddata]
    return jsonify(data), 200

@bp.route('/date', methods=['POST'])
def create():
    data = request.get_json()
    if not data or not all(key in data for key in ('date', 'patient', 'idDentist','date', 'hour', 'service')):
        return jsonify({'error': 'Missing data'}), 400
    
    try:
        date = datetime.strptime(data['date'], '%Y-%m-%d').date()
        hour = datetime.strptime(data['hour'], '%H:%M:%S').time()
    except ValueError:
        return jsonify({'error': 'Invalid date or hour format, should be YYYY-MM-DD and HH:MM:SS'}), 400

    new_date = Date(
        patient=data['patient'],
        idDentist=data['idDentist'],
        date=date,
        hour=hour,
        service=data['service']

    )

    db.session.add(new_date)
    db.session.commit()

    return jsonify(new_date.to_json()), 201


@bp.route('/date/<int:id>' , methods=['GET'])
def getDate(id):
    date = Date.query.get(id)
    if not date:
        return jsonify({'error': 'Date not found'}),404
    return jsonify(date.to_json()),200


@bp.route('/date/<int:id>', methods=['PUT'])
def updateDate(id):
    date = Date.query.get(id)
    if not date:
        return jsonify({'error': 'Date not found'}), 404

    data = request.get_json()
    if not data or not all(key in data for key in ('patient', 'idDentist','date', 'hour', 'service')):
        return jsonify({'error': 'Missing data'}), 400

    date.patient = data['patient']
    date.idDentist = data['idDentist']
    date.service = data['service']

    try:
        date.date = datetime.strptime(data['date'], '%Y-%m-%d').date()
        date.hour = datetime.strptime(data['hour'], '%H:%M:%S').time()
    except ValueError:
        return jsonify({'error': 'Invalid date or hour format, should be YYYY-MM-DD and HH:MM:SS'}), 400

    db.session.commit()
    return jsonify(date.to_json()), 200

@bp.route('/date/<int:id>', methods=['DELETE'])
def deleteDate(id):
    date = Date.query.get(id)
    if not date:
        return jsonify({'error': 'Date not found'}), 404
    
    date = db.session.merge(date)

    db.session.delete(date)
    db.session.commit()
    return jsonify(date.to_json()), 200
