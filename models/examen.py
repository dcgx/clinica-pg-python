#Se crea la clase examen con sus respectivos atributos
#Se sugieren los siguientes metodos o funciones:
class Examen:
    def __init__(self,tipo='',resultado=''):
        self.__tipo = tipo
        self.__resultado = resultado


#Get se utiliza para obtener el valor de un atributo privado de una clase. Proporciona acceso de solo lectura a ese atributo. 
#Esto significa que puedes obtener su valor desde fuera de la clase, pero no puedes modificarlo directamente.        
    def GetTipo(self):
        return self.__tipo
    def GetResultado(self):
        return self.__resultado


#Set se utiliza para modificar el valor de un atributo privado de una clase. Proporciona acceso de solo escritura a ese atributo. 
#Esto significa que puedes establecer su valor desde fuera de la clase, pero no puedes acceder a él directamente.    
    
    def SetTipo(self,tipo):
        self.__tipo = tipo
    def SetResultado(self,resultado):
        self.__resultado = resultado   
