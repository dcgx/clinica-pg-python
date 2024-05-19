class Diagnostico:
    def __init__(self,id='', enfermedad='', examen_id=''):
        self.__id = id
        self.__enfermedad = enfermedad
        self.__examen_id = examen_id

    def get_id(self):
        return self.__id
    def get_enfermedad(self):
        return self.__enfermedad
    def get_examen_id(self):
        return self.__examen_id

    def set_id(self,id):
        self.__id = id    
    def set_enfermedad(self,enfermedad):
        self.__enfermedad = enfermedad
    def set_examen_id(self,examen_id):
        self.__examen_id = examen_id


    def show(self):
        return f"Diagnóstico: {self.__enfermedad}"