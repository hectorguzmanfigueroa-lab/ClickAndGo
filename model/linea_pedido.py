from model.producto import Producto


class LineaPedido:
    def __init__(self, producto: Producto, cantidad: int):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        self.__producto = producto  # Guarda el objeto que recibió.
        self.__cantidad = cantidad
        self.__precioUnitario = producto.precio

    @property
    def producto(self) -> Producto:
        return self.__producto

    @property
    def cantidad(self) -> int:
        return self.__cantidad

    @property
    def precioUnitario(self) -> float:
        return self.__precioUnitario

    def calcular_Subtotal(self) -> float:
        return self.__cantidad * self.__precioUnitario
