from app import db

class Process(db.Model):
    __tablename__ = 'process'
    idProcess = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    
    historys = db.relationship('DentalHistory', secondary='process_history', back_populates='processes')

    def to_json(self):
        return {
            'idProcess': self.idProcess,
            'name': self.name,
            'price': self.price,
            'duration': self.duration,
        }