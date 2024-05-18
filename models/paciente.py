#Se crea la clase paciente con sus respectivos atributos
#Se sugieren los siguientes Métodos o funciones: cambiar_medico(nuevo_medico), solicitar_examen(examen, posible_diagnostico).
class Paciente:
    def __init__(self,nombre='',rut='',diagnostico='',medico='',habitacion=''):
        self.__nombre = nombre
        self.__rut = rut
        self.__diagnostico = diagnostico
        self.__medico = medico
        self.__habitacion = habitacion

#Get se utiliza para obtener el valor de un atributo privado de una clase. Proporciona acceso de solo lectura a ese atributo. 
#Esto significa que puedes obtener su valor desde fuera de la clase, pero no puedes modificarlo directamente.        
    def GetNombre(self):
        return self.__nombre
    def GetRut(self):
        return self.__rut
    def GetDiagnostico(self):
        return self.__diagnostico
    def GetMedico(self):
        return self.__medico
    def GetHabitacion(self):
        return self.__habitacion

#Set se utiliza para modificar el valor de un atributo privado de una clase. Proporciona acceso de solo escritura a ese atributo. 
#Esto significa que puedes establecer su valor desde fuera de la clase, pero no puedes acceder a él directamente.    
    
    def SetNombre(self,nombre):
        self.__nombre = nombre
    def SetRut(self,rut):
        self.__rut = rut   
    def SetDiagnostico(self,diagnostico):
        self.__diagnostico = diagnostico  
    def SetMedico(self,medico):
        self.__medico = medico   
    def SetHabitacion(self,habitacion):
        self.__habitacion = habitacion
            
#Get & Set Estos métodos permiten mantener la encapsulación 
#y controlar el acceso a los atributos de una clase, lo que hace que el código sea más seguro y mantenible.            
    def ShowData(self):
        print(f'Nombre:{self.__nombre}\nRut:{self.__rut}\nDiagnostico:{self.__diagnostico}\nMedico:{self.__medico}\nHabitacion:{self.__habitacion}')