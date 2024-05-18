#Se crea la clase enfermedad con sus respectivos atributos
#Se sugieren los siguientes metodos o funciones:
class Enfermedad:
    def __init__(self,nombre='',examenes=''):
        self.__nombre = nombre
        self.__examenes = examenes


#Get se utiliza para obtener el valor de un atributo privado de una clase. Proporciona acceso de solo lectura a ese atributo. 
#Esto significa que puedes obtener su valor desde fuera de la clase, pero no puedes modificarlo directamente.        
    def GetNombre(self):
        return self.__nombre
    def GetExamenes(self):
        return self.__examenes


#Set se utiliza para modificar el valor de un atributo privado de una clase. Proporciona acceso de solo escritura a ese atributo. 
#Esto significa que puedes establecer su valor desde fuera de la clase, pero no puedes acceder a él directamente.    
    
    def SetNombre(self,nombre):
        self.__nombre = nombre
    def SetExamenes(self,examenes):
        self.__examenes = examenes   
