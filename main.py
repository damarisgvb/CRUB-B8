from basedatos.db import db
from modelo.curso import Curso
from modelo.estudiante import Estudiante
from controlador.curso_contralador import CursoControlador
from controlador.estudiante_controlador import EstudianteControlador

def main ():
    db.connect()
    db.create_tables([Curso, Estudiante])
    CursoControlador.crear("Programcion II","es muy bueno, donde aprendera cosas de programar, desde lo mas basico a los mas dificil", "comienza el 12-03-25", "y termina el 01-01-26", "a las 09:00")
    cursos = CursoControlador.mostrar()
    for curso in cursos:
        print(f"{curso.id} {curso.nombre}")
    
    print ("Bienvenido al sistema de gestion de estudiantes")
    
  
