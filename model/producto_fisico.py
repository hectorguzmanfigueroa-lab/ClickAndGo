from model.producto import Producto


class ProductoFisico(Producto):
    def __init__(self, precio: float, stock: int):
        super().__init__(precio)
        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")
        self.__stock = stock

    @property
    def stock(self) -> int:
        return self.__stock

    def verificar_Stock(self, cantidad: int) -> bool:
        return self.__stock >= cantidad

    def descontar_Stock(self, cantidad: int):
        if cantidad <= 0 or cantidad > self.__stock:
            raise ValueError("La cantidad a descontar no es válida.")
        self.__stock -= cantidad

    def calcular_Flete(self) -> int:
        return 3500  # Tarifa de ejemplo para la demostración.

    def procesar_Entrega(self) -> str:
        return "Producto físico: se entrega por despacho."
