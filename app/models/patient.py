from app import db

class Patient(db.Model):
    idPatient = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    direction = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)   

    histories = db.relationship('DentalHistory', back_populates='patient')

    def to_json(self):
        return {
            "idPatient": self.idPatient,
            "name": self.name,
            "birthdate": self.birthdate.strftime('%d/%m/%Y'),            
            "direction": self.direction,
            "phone": self.phone,
            "email": self.email,
            "histories": [history.to_json() for history in self.histories]
        }