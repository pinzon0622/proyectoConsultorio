from app import db

class Dentist(db.Model):
    __tablename__ = 'dentist'
    idDentist = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    specialty = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)

    histories = db.relationship('DentalHistory', back_populates='dentist')

    def to_json(self):
        return {
            'idDentist': self.idDentist,
            'name': self.name,
            'specialty': self.specialty,
            'phone': self.phone,
            'email': self.email
        }