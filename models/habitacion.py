class Habitacion:
    def __init__(self,id='',numero=''):
        self.__id = id
        self.__numero = numero

    def get_numero(self):
        return self.__numero
    
    def get_id(self):
        return self.__id
    def set_numero(self,numero):
        self.__numero = numero

    def show(self):
        return f"Habitación: {self.__numero}"