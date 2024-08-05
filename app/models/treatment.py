from app import db

class Treatment(db.Model):
    __tablename__ = 'treatment'
    idTreatment = db.Column(db.Integer, primary_key=True)
    idPatient = db.Column(db.Integer, db.ForeignKey('patient.idPatient'), nullable=False)
    idDentist = db.Column(db.Integer, db.ForeignKey('dentist.idDentist'), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    initDate = db.Column(db.Date, nullable=False)
    endDate = db.Column(db.Date, nullable=False)
    
    processes = db.relationship('Process', secondary='process_treatment', back_populates='treatments')

    def to_json(self):
        return {
            'idTreatment': self.idTreatment,
            'idPatient': self.idPatient,
            'idDentist': self.idDentist,
            'description': self.description,
            'initDate': self.initDate.isoformat(),
            'endDate': self.endDate.isoformat(),
            'processes': [process.to_json() for process in self.processes]
        }