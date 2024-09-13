from modelo.estudiante import Estudiante
from modelo.curso import Curso

class  EstudianteServicio:
    
    @staticmethod
    def mostrar_estudiante():
        return list(Estudiante.select())
    
    def crear_estudiante(nombre, DNI, gmail, telefono, fecha_nacimiento, curso_id):
        curso = curso.get(Curso.id == curso_id)
        estudiante = Estudiante.create(nombre=nombre, DNI=DNI, gmail=gmail, telefono=telefono, fecha_nacimiento=fecha_nacimiento, curso_id=curso_id)
        
        
        return estudiante
    
    def mostrar_estudiante():
        return list(Estudiante.select())
    
    def eliminar_estudiante(id):
        estudiante = Estudiante.get(Estudiante.id == id)
        estudiante.delete_instace()
        return estudiante
    