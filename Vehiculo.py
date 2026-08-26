class Vehiculo:
    def __init__(self, patente: str, anio: int):
        self.patente = patente
        self.anio = anio
        self.__en_taller: bool = False
