from db.operations import get_cama_by_paciente_id, get_habitacion_by_paciente_id


class Paciente:
    def __init__(self,id='',nombre='',rut='', medico_id=None):
        self.__id = id
        self.__nombre = nombre
        self.__rut = rut
        self.__medico_id = medico_id

    def get_id(self):
        return self.__id
    def get_nombre(self):
        return self.__nombre
    def get_rut(self):
        return self.__rut
    def get_medico_id(self):
        return self.__medico_id

    def get_habitacion(self):
        habitacion = get_habitacion_by_paciente_id(self.get_id())
        return habitacion.get_numero() if habitacion is not None else "Sin habitacion asignada"

    def get_cama(self):
        cama = get_cama_by_paciente_id(self.get_id())
        return cama.get_id() if cama is not None else "Sin cama asignada"
    
    def set_id(self,id):
        self.__id = id
    def set_nombre(self,nombre):
        self.__nombre = nombre
    def set_rut(self,rut):
        self.__rut = rut   
    def set_medico_id(self,medico_id):
        self.__medico_id = medico_id
            
    def show(self):
        print(f'Nombre:{self.__nombre}\nRut:{self.__rut}\n')