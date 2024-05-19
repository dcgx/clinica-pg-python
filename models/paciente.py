class Paciente:
    def __init__(self,nombre='',rut='', medico_id=None):
        self.__nombre = nombre
        self.__rut = rut
        self.__medico_id = medico_id

    def get_nombre(self):
        return self.__nombre
    def get_rut(self):
        return self.__rut
    def get_medico_id(self):
        return self.__medico_id
    
    def set_nombre(self,nombre):
        self.__nombre = nombre
    def set_rut(self,rut):
        self.__rut = rut   
    def set_medico_id(self,medico_id):
        self.__medico_id = medico_id
            
    def show(self):
        print(f'Nombre:{self.__nombre}\nRut:{self.__rut}\n')