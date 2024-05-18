#Se crea la clase habitacion con sus respectivos atributos
#Se sugieren los siguientes metodos o funciones: agregar_cama(cama), eliminar_cama(cama)
class Habitacion:
    def __init__(self,numero='',cama=''):
        self.__numero = numero
        self.__cama = cama


#Get se utiliza para obtener el valor de un atributo privado de una clase. Proporciona acceso de solo lectura a ese atributo. 
#Esto significa que puedes obtener su valor desde fuera de la clase, pero no puedes modificarlo directamente.        
    def GetNumero(self):
        return self.__numero
    def GetCama(self):
        return self.__cama


#Set se utiliza para modificar el valor de un atributo privado de una clase. Proporciona acceso de solo escritura a ese atributo. 
#Esto significa que puedes establecer su valor desde fuera de la clase, pero no puedes acceder a él directamente.    
    
    def SetNumero(self,numero):
        self.__numero = numero
    def SetCama(self,cama):
        self.__cama = cama