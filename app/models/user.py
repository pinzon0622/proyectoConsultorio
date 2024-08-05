from app import db

class User(db.Model):
    __tablename__ = 'user'
    idUser = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def to_json(self):
        return{
            "idUser": self.idUser,
            "username": self.username,
            "email": self.email,
            "password": self.password
        }