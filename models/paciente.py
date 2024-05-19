#Se crea la clase paciente con sus respectivos atributos
#Se sugieren los siguientes Métodos o funciones: cambiar_medico(nuevo_medico), solicitar_examen(examen, posible_diagnostico).
class Paciente:
    def __init__(self,nombre='',rut=''):
        self.__nombre = nombre
        self.__rut = rut

    def get_nombre(self):
        return self.__nombre
    def get_rut(self):
        return self.__rut
    
    def set_nombre(self,nombre):
        self.__nombre = nombre
    def set_rut(self,rut):
        self.__rut = rut   
            
    def show(self):
        print(f'Nombre:{self.__nombre}\nRut:{self.__rut}\n')