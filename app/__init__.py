from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager


db = SQLAlchemy()



def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.config['JWT_SECRET_KEY'] = '1234'
    jwt = JWTManager(app)
    
    CORS(app)

    db.init_app(app)

    from app.routes import patientRoutes,dentistRoutes,auth,userRoutes, dateRoutes,dentalHistoryRoutes, processRoutes,treatmentRoutes,processTeatmentRoutes
    app.register_blueprint(patientRoutes.bp)
    app.register_blueprint(dentistRoutes.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(userRoutes.bp)
    app.register_blueprint(dateRoutes.bp)
    app.register_blueprint(dentalHistoryRoutes.bp)
    app.register_blueprint(processRoutes.bp)
    app.register_blueprint(treatmentRoutes.bp)
    app.register_blueprint(processTeatmentRoutes.bp)

    return app