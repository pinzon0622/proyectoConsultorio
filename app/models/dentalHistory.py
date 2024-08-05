from app import db

class DentalHistory(db.Model):
    __tablename__ = 'dental_history'
    idDentalHistory = db.Column(db.Integer, primary_key=True)
    idPatient = db.Column(db.Integer, db.ForeignKey('patient.idPatient'), nullable=False)
    idDentist = db.Column(db.Integer, db.ForeignKey('dentist.idDentist'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    diagnostic = db.Column(db.String(255), nullable=False)
    observations = db.Column(db.String(255), nullable=False)

    def to_json(self):
        return {
            'idDentalHistory': self.idDentalHistory,
            'idPatient': self.idPatient,
            'idDentist': self.idDentist,
            'date': self.date.isoformat(),
            'diagnostic': self.diagnostic,
            'observations': self.observations
        }