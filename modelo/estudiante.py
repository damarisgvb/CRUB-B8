from peewee import Model, AutoField, CharField, DateField, DateField, ForeignKeyField
from basedatos.db import db
from modelo.curso import Curso

class Estudiante (Model):
    id = AutoField()
    nombre = CharField(unique=True)
    dni = CharField()
    correo_electronico = CharField()
    numero_telefono = DateField ()
    fecha_nacimiento = DateField()
    curso = ForeignKeyField(Curso)
    
    
    class Meta :
        database = db
        table_name = 'estudiantes'
    

   
    