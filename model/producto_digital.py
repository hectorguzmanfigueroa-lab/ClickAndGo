from model.producto import Producto


class ProductoDigital(Producto):
    def __init__(self, precio: float, linkDescarga: str):
        super().__init__(precio)
        self.__linkDescarga = linkDescarga

    def procesar_Entrega(self) -> str:
        return "Producto digital: descarga en " + self.__linkDescarga
