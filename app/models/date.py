from app import db
import enum

from app.models.dentist import Dentist

class Service(enum.Enum):
    CLEANING = "Limpieza"
    FILLING = "Relleno"
    EXTRACTION = "Extracción"
    CHECKUP = "Revisión"

class Date(db.Model):
    __tablename__ = 'date'
    idDate = db.Column(db.Integer, primary_key=True)

    patient = db.Column(db.String(255), nullable=False)
    idDentist = db.Column(db.Integer, db.ForeignKey('dentist.idDentist'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    hour = db.Column(db.Time, nullable=False)
    service = db.Column(db.Enum(Service), nullable=False)

    dentist = db.relationship('Dentist', backref='dates' , lazy='joined')
    
    def to_json(self):
        return {
            'idDate': self.idDate,
            'patient': self.patient,
            'dentist': self.dentist.to_json() if self.dentist else None,
            'idDentist': self.idDentist,
            'date': self.date.strftime('%d/%m/%Y'),
            'hour': self.hour.strftime('%H:%M'),
            'service': self.service.value
        }