from app import db

class DentalHistory(db.Model):
    __tablename__ = 'dental_history'
    idDentalHistory = db.Column(db.Integer, primary_key=True)
    idPatient = db.Column(db.Integer, db.ForeignKey('patient.idPatient'), nullable=False)
    idDentist = db.Column(db.Integer, db.ForeignKey('dentist.idDentist'), nullable=False)
    idProcess = db.Column(db.Integer, db.ForeignKey('process.idProcess'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    diagnostic = db.Column(db.String(255), nullable=False)
    observations = db.Column(db.String(255), nullable=False)


    patient = db.relationship('Patient', back_populates='histories', lazy="joined")
    dentist = db.relationship('Dentist', 
    back_populates='histories', lazy="joined")
    process = db.relationship('Process', back_populates='dentalHistories', lazy="joined")

    def to_json(self):
        return {
            'idDentalHistory': self.idDentalHistory,
            'idPatient': self.idPatient,
            'idDentist': self.idDentist,
            'idProcess': self.idProcess,
            'date': self.date.isoformat(),
            'diagnostic': self.diagnostic,
            'observations': self.observations,
            'process': self.process.to_json(),
            'dentist': self.dentist.to_json()
        }