class Cama:
    def __init__(self,id='',paciente_id=None,habitacion_id=None,habilitada=False):
        self.__id = id
        self.__habilitada = habilitada
        self.__paciente_id = paciente_id
        self.__habitacion_id = habitacion_id

    def get_id(self):
        return self.__id
    def get_habilitada(self):
        return self.__habilitada
    def get_paciente_id(self):
        return self.__paciente_id
    def get_habitacion_id(self):
        return self.__habitacion_id

    def set_id(self,id):
        self.__id = id
    def set_habilitada(self,habilitada):
        self.__habilitada = habilitada
    def set_paciente_id(self,paciente_id):
        self.__paciente_id = paciente_id
    def set_habitacion_id(self,habitacion_id):
        self.__habitacion_id = habitacion_id

    def show(self):
        return f"Cama: {self.__id}, Habilitada: {self.__habilitada}, Paciente: {self.__paciente_id}, Habitación: {self.__habitacion_id}"