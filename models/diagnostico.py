class Diagnostico:
    def __init__(self,id='', enfermedad=''):
        self.__id = id
        self.__enfermedad = enfermedad

    def get_id(self):
        return self.__id
    def get_enfermedad(self):
        return self.__enfermedad

    def set_id(self,id):
        self.__id = id    
    def set_enfermedad(self,enfermedad):
        self.__enfermedad = enfermedad
