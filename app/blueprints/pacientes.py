from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.extensions import db
from app.models import Paciente

bp_pacientes = Blueprint('pacientes', __name__)

@bp_pacientes.route('/')
def listar():
    pacientes = Paciente.query.all()
    return render_template('pacientes/listar.html', pacientes=pacientes)

@bp_pacientes.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        nuevo = Paciente(
            nombre=request.form['nombre'],
            telefono=request.form['telefono']
        )
        db.session.add(nuevo)
        db.session.commit()
        flash('Paciente registrado exitosamente', 'success')
        return redirect(url_for('pacientes.listar'))
    return render_template('pacientes/crear.html')

@bp_pacientes.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    paciente = Paciente.query.get_or_404(id)
    if request.method == 'POST':
        paciente.nombre = request.form['nombre']
        paciente.telefono = request.form['telefono']
        db.session.commit()
        flash('Paciente actualizado', 'success')
        return redirect(url_for('pacientes.listar'))
    return render_template('pacientes/editar.html', paciente=paciente)

@bp_pacientes.route('/eliminar/<int:id>')
def eliminar(id):
    paciente = Paciente.query.get_or_404(id)
    db.session.delete(paciente)
    db.session.commit()
    flash('Paciente eliminado', 'success')
    return redirect(url_for('pacientes.listar'))