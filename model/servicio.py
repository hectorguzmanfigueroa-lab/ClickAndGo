from model.producto import Producto


class Servicio(Producto):
    def __init__(self, precio: float, fechaAgendada: str):
        super().__init__(precio)
        self.__fechaAgendada = fechaAgendada

    def agendar(self, fecha: str):
        self.__fechaAgendada = fecha

    def procesar_Entrega(self) -> str:
        return "Servicio: atención agendada para el " + self.__fechaAgendada
