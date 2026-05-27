from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.extensions import db
from app.models import Medico

bp_medicos = Blueprint('medicos', __name__)

@bp_medicos.route('/')
def listar():
    medicos = Medico.query.all()
    return render_template('medicos/listar.html', medicos=medicos)

@bp_medicos.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        nuevo = Medico(
            nombre=request.form['nombre'],
            especialidad=request.form['especialidad']
        )
        db.session.add(nuevo)
        db.session.commit()
        flash('Médico registrado exitosamente', 'success')
        return redirect(url_for('medicos.listar'))
    return render_template('medicos/crear.html')

@bp_medicos.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    medico = Medico.query.get_or_404(id)
    if request.method == 'POST':
        medico.nombre = request.form['nombre']
        medico.especialidad = request.form['especialidad']
        db.session.commit()
        flash('Médico actualizado', 'success')
        return redirect(url_for('medicos.listar'))
    return render_template('medicos/editar.html', medico=medico)

@bp_medicos.route('/eliminar/<int:id>')
def eliminar(id):
    medico = Medico.query.get_or_404(id)
    db.session.delete(medico)
    db.session.commit()
    flash('Médico eliminado', 'success')
    return redirect(url_for('medicos.listar'))