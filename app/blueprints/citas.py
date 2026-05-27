from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.extensions import db
from app.models import Cita, Medico, Paciente

bp_citas = Blueprint('citas', __name__)

@bp_citas.route('/')
def listar():
    citas = Cita.query.all()
    return render_template('citas/listar.html', citas=citas)

@bp_citas.route('/crear', methods=['GET', 'POST'])
def crear():
    medicos = Medico.query.all()
    pacientes = Paciente.query.all()
    
    if request.method == 'POST':
        nueva = Cita(
            fecha=request.form['fecha'],
            hora=request.form['hora'],
            medico_id=request.form['medico_id'],
            paciente_id=request.form['paciente_id']
        )
        db.session.add(nueva)
        db.session.commit()
        flash('Cita registrada exitosamente', 'success')
        return redirect(url_for('citas.listar'))
    
    return render_template('citas/crear.html', medicos=medicos, pacientes=pacientes)

@bp_citas.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    cita = Cita.query.get_or_404(id)
    medicos = Medico.query.all()
    pacientes = Paciente.query.all()
    
    if request.method == 'POST':
        cita.fecha = request.form['fecha']
        cita.hora = request.form['hora']
        cita.medico_id = request.form['medico_id']
        cita.paciente_id = request.form['paciente_id']
        db.session.commit()
        flash('Cita actualizada', 'success')
        return redirect(url_for('citas.listar'))
    
    return render_template('citas/editar.html', cita=cita, medicos=medicos, pacientes=pacientes)

@bp_citas.route('/eliminar/<int:id>')
def eliminar(id):
    cita = Cita.query.get_or_404(id)
    db.session.delete(cita)
    db.session.commit()
    flash('Cita eliminada', 'success')
    return redirect(url_for('citas.listar'))