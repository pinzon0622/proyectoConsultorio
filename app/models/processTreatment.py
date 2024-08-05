from app import db

class ProcessTreatment(db.Model):
    __tablename__ = 'process_treatment'
    idProcessTreatment = db.Column(db.Integer, primary_key=True, autoincrement=True)
    processes = db.Column(db.Integer, db.ForeignKey('process.idProcess'))
    treatments = db.Column(db.Integer, db.ForeignKey('treatment.idTreatment'))

    def to_json(self):
        return {
            'idProcessTreatment': self.idProcessTreatment,
            'processes': self.processes,
            'treatments': self.treatments
        }