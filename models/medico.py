class Medico:
    def __init__(self,id='',nombre='',especialidad=''):
        self.__id = id
        self.__nombre = nombre
        self.__especialidad = especialidad

    def get_id(self):
        return self.__id
    def get_nombre(self):
        return self.__nombre
    def get_especialidad(self):
        return self.__especialidad
    
    def set_nombre(self,nombre):
        self.__nombre = nombre
    def set_especialidad(self,especialidad):
        self.__especialidad = especialidad