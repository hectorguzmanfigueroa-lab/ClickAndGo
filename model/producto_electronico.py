from model.producto_fisico import ProductoFisico


class ProductoElectronico(ProductoFisico):
    def __init__(self, precioUSD: float, stock: int, valorDolar: float):
        self.__precioUSD = precioUSD
        precio = self.calcular_Precio(valorDolar)
        super().__init__(precio, stock)

    def calcular_Precio(self, valorDolar: float) -> float:
        return self.__precioUSD * valorDolar
