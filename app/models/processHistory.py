from app import db

class ProcessHistory(db.Model):
    __tablename__ = 'process_history'
    idProcessTreatment = db.Column(db.Integer, primary_key=True, autoincrement=True)
    processes = db.Column(db.Integer, db.ForeignKey('process.idProcess'))
    historys = db.Column(db.Integer, db.ForeignKey('dental_history.idDentalHistory'))

    

    def to_json(self):
        return {
            'idProcessTreatment': self.idProcessTreatment,
            'processes': self.processes,
            'historys': self.historys
        }