#Se crea la clase examen con sus respectivos atributos
#Se sugieren los siguientes metodos o funciones:
class Examen:
    def __init__(self,id='', tipo='',resultado='',paciente_id=''):
        self.__id = id
        self.__tipo = tipo
        self.__resultado = resultado
        self.__paciente_id = paciente_id

    def get_id(self):
        return self.__id
    def get_tipo(self):
        return self.__tipo
    def get_resultado(self):
        return self.__resultado
    def get_paciente_id(self):
        return self.__paciente_id

    def set_id(self,id):
        self.__id = id    
    def set_tipo(self,tipo):
        self.__tipo = tipo
    def set_resultado(self,resultado):
        self.__resultado = resultado
