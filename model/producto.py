from abc import ABC, abstractmethod


class Producto(ABC):
    def __init__(self, precio: float):
        self.precio = precio

    @property
    def precio(self) -> float:
        return self.__precio

    @precio.setter
    def precio(self, valor: float):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.__precio = valor

    @abstractmethod
    def procesar_Entrega(self) -> str:
        pass  # Cada clase hija implementa este método, como tarifa_hora en Vehiculo.

    def verificar_Stock(self, cantidad: int) -> bool:
        return True  # Los digitales y servicios no usan stock físico.

    def descontar_Stock(self, cantidad: int):
        return None  # Los digitales y servicios no descuentan stock físico.
