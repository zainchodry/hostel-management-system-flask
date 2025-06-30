from flask import Flask
from config import Config
import os
from app.extensions import db,migrate
from flask_mail import Mail, Message

mail = Mail()

def create_app():
    app = Flask(__name__, template_folder=os.path.abspath('templates'))
    app.config.from_object(Config)
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'razzaqzain546@gmail.com'
    app.config['MAIL_PASSWORD'] = 'gbjw tzhg fqvq egrs'


    db.init_app(app)

    mail.init_app(app)


    

    from app.routes import main
    app.register_blueprint(main)

    with app.app_context():
        db.create_all()


    
    return app