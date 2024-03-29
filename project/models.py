from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import Column, ForeignKey, Integer, String, Time, Date

db = SQLAlchemy()


EspecialidadProfesional = db.Table('EspecialidadProfesional',
    db.Column('id_Profesional',db.Integer, db.ForeignKey('profesional.id'),primary_key=True),
    db.Column('id_Especialidad',db.Integer, db.ForeignKey('especialidad.id'),primary_key=True))

consultorioProfesional = db.Table('consultorioProfesional',
    db.Column('id_Profesional',db.Integer, db.ForeignKey('profesional.id'),primary_key=True),
    db.Column('id_Consultorio',db.Integer, db.ForeignKey('consultorio.id'),primary_key=True))
    

class Paciente(UserMixin, db.Model):
    __tablename__ = 'paciente'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    nombre = db.Column(db.String(30))
    apellido = db.Column(db.String(30))
    dni = db.Column(db.String(8))
    telefono = db.Column(db.String(10))
    password = db.Column(db.String(100))

    turnos = db.relationship('Turnos', backref='persona', lazy=True)


class Profesional(UserMixin, db.Model):
    __tablename__ = 'profesional'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    nombre = db.Column(db.String(30))
    apellido = db.Column(db.String(30))
    matricula = db.Column(db.String(8))
    password = db.Column(db.String(100))

    turnos = db.relationship('Turnos', backref='profesional', lazy=True)
    atencionProfesional = db.relationship('AtencionProfesional', backref='profesional', lazy=True)
    
    ConsultorioProfesional = db.relationship('Consultorio', secondary=consultorioProfesional, lazy='subquery', backref=db.backref('Profesional', lazy=True))
    especialidad=db.relationship('Especialidad', secondary=EspecialidadProfesional, lazy='subquery', backref=db.backref('Profesional', lazy=True))

class DiaAtencion(db.Model):
    __tablename__ = 'diaAtencion'
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(10))

    turnos = db.relationship('Turnos', backref='diaAtencion', lazy=True)
    atencionProfesional = db.relationship('AtencionProfesional', backref='diaAtencion', lazy=True)

class Especialidad(db.Model):
    __tablename__ = 'especialidad'
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(20))

    
class Consultorio(db.Model):
    __tablename__ = 'consultorio'
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(20))

class Horario(db.Model):
    __tablename__ = 'horario'
    id = db.Column(db.Integer, primary_key=True)
    hora_inicio = db.Column(db.Time())  
    hora_final = db.Column(db.Time())
    
    turnos = db.relationship('Turnos', backref='horario', lazy=True)
    atencionProfesional = db.relationship('AtencionProfesional', backref='horario', lazy=True)

class Turnos(db.Model):
    __tablename__ = 'turnos'
    id = db.Column(db.Integer, primary_key=True)
    id_Profesional = db.Column(db.Integer, ForeignKey('profesional.id'))
    id_Dia = db.Column(db.Integer, ForeignKey('diaAtencion.id'))
    id_Horario = db.Column(db.Integer, ForeignKey('horario.id'))
    id_Paciente = db.Column(db.Integer, ForeignKey('paciente.id'))
    descripcion = db.Column(db.String(20))

class AtencionProfesional(db.Model):
    __tablename__ = 'atencionProfesional'
    id = db.Column(db.Integer, primary_key=True)
    id_Profesional = db.Column(db.Integer, ForeignKey('profesional.id'))
    id_Dia = db.Column(db.Integer, ForeignKey('diaAtencion.id'))
    id_Horario = db.Column(db.Integer, ForeignKey('horario.id'))

    

