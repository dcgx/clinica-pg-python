#Se crea la clase medico con sus respectivos atributos
#Se sugieren los siguientes metodos o funciones: 
#asignar_paciente(paciente), diagnosticar_enfermedad(paciente, enfermedad, examenes)
class Medico:
    def __init__(self,nombre='',especialidad=''):
        self.__nombre = nombre
        self.__especialidad = especialidad
        self.__pacientesAsignados = []

    def asignar_paciente(self, paciente):
        self.pacientes_asignados.append(paciente)

#Get se utiliza para obtener el valor de un atributo privado de una clase. Proporciona acceso de solo lectura a ese atributo. 
#Esto significa que puedes obtener su valor desde fuera de la clase, pero no puedes modificarlo directamente.        
    def GetNombre(self):
        return self.__nombre
    def GetEspecialidad(self):
        return self.__especialidad
    def GetPacientesAsignados(self):
        return self.__pacientesAsignados

#Set se utiliza para modificar el valor de un atributo privado de una clase. Proporciona acceso de solo escritura a ese atributo. 
#Esto significa que puedes establecer su valor desde fuera de la clase, pero no puedes acceder a él directamente.    
    
    def SetNombre(self,nombre):
        self.__nombre = nombre
    def SetEspecialidad(self,especialidad):
        self.__especialidad = especialidad   
    def SetPacientesAsignados(self,pacientesAsignados):
        self.__pacientesAsignados = pacientesAsignados