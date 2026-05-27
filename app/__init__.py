from flask import Flask, render_template
from .extensions import db, migrate
from .models import Medico, Paciente, Cita

def create_app():
    app = Flask(__name__)
    
    # Configuración
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinica.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'clave_secreta_para_medicontrol'
    
    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Registrar blueprints
    from .blueprints.medicos import bp_medicos
    from .blueprints.pacientes import bp_pacientes
    from .blueprints.citas import bp_citas
    
    app.register_blueprint(bp_medicos, url_prefix='/medicos')
    app.register_blueprint(bp_pacientes, url_prefix='/pacientes')
    app.register_blueprint(bp_citas, url_prefix='/citas')
    
    # Ruta principal
    @app.route('/')
    def index():
        return render_template('index.html')
    
    return app  