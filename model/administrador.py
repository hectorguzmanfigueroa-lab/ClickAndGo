from model.producto import Producto


class Administrador:
    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.__catalogo = []

    def gestionar_Catalogo(self, producto: Producto):
        if producto not in self.__catalogo:
            self.__catalogo.append(producto)

    def cambiar_Precio(self, producto: Producto, nuevoPrecio: float):
        if producto not in self.__catalogo:
            raise ValueError("El producto no está en el catálogo.")
        producto.precio = nuevoPrecio
