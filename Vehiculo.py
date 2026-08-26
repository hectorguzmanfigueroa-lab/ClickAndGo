class Vehiculo:
    def __init__(self, patente: str, anio: int):
        self.patente = patente
        self.anio = anio
        self.__en_taller: bool = False

    def ingresar(self):
        self.__en_taller = True

    def entregar(self):
        self.__en_taller = False

    def tarifa_hora(self) -> int:
        return 0
