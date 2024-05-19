class Habitacion:
    def __init__(self,numero='',cama=''):
        self.__numero = numero

    def get_numero(self):
        return self.__numero
    
    def set_numero(self,numero):
        self.__numero = numero