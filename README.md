# MediControl - Sistema de Gestión de Citas Médicas

## Datos del Estudiante
- **Nombre:** ALEJANDRO CAPARICONA AVILE
- **ci** 13180270
- **Curso:** TEM-742 Tecnologías Emergentes II
- **Fecha:** 26 DE MAYO 2026

## Requerimientos Cumplidos

### Parte 1: Arquitectura y Configuración
- ✅ Flask Application Factory (create_app en app/__init__.py)
- ✅ Blueprints: bp_medicos, bp_pacientes, bp_citas
- ✅ Prefijos: /medicos, /pacientes, /citas
- ✅ SQLite como base de datos

### Parte 2: Modelos y Migraciones
- ✅ Modelo Medico (id, nombre, especialidad)
- ✅ Modelo Paciente (id, nombre, telefono)
- ✅ Modelo Cita (id, fecha, hora, medico_id, paciente_id)
- ✅ Relaciones: 1 médico → N citas, 1 paciente → N citas
- ✅ Flask-Migrate implementado

### Parte 3: CRUD y Plantillas
- ✅ CRUD completo para Médicos
- ✅ CRUD completo para Pacientes
- ✅ CRUD completo para Citas
- ✅ Bootstrap para estilos
- ✅ Plantilla base con herencia

## Tecnologías
- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Bootstrap 5
- SQLite

## Cómo Ejecutar

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Crear base de datos
flask db init
flask db migrate -m "Inicial"
flask db upgrade

# 3. Ejecutar
python run.py

# 4.URL
# https://github.com/AlejandroCapari-bit/MediControl
