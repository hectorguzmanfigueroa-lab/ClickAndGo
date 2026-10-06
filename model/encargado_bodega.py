from model.pedido import Pedido


class EncargadoBodega:
    def __init__(self, nombre: str):
        self.__nombre = nombre

    def preparar_Pedido(self, pedido: Pedido) -> str:
        if not pedido.confirmado:
            raise ValueError("Debe confirmar el pedido antes de prepararlo.")
        return self.__nombre + " está preparando el pedido."

    def despachar_Pedido(self, pedido: Pedido) -> bool:
        return pedido.despachar()
