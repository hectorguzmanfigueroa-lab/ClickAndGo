from model.cliente import Cliente
from model.producto import Producto
from model.linea_pedido import LineaPedido
from model.stock_insuficiente_error import StockInsuficienteError
from model.pedido_no_pagado_error import PedidoNoPagadoError


class Pedido:
    def __init__(self, cliente: Cliente):
        self.__cliente = cliente
        self.__lineas = []
        self.__pagado = False
        self.__confirmado = False
        self.__despachado = False

    @property
    def cliente(self) -> Cliente:
        return self.__cliente

    @property
    def lineas(self) -> list:
        return self.__lineas

    @property
    def pagado(self) -> bool:
        return self.__pagado

    @property
    def confirmado(self) -> bool:
        return self.__confirmado

    @property
    def despachado(self) -> bool:
        return self.__despachado

    def agregar_Linea(self, producto: Producto, cantidad: int):
        if self.__confirmado:
            raise ValueError("El pedido ya está confirmado.")
        # Igual que OrdenTrabajo.agregar_repuesto: crea la línea dentro.
        linea = LineaPedido(producto, cantidad)
        self.__lineas.append(linea)

    def confirmar(self) -> bool:
        if self.__confirmado:
            raise ValueError("El pedido ya está confirmado.")
        if len(self.__lineas) == 0:
            raise ValueError("Debe agregar al menos una línea.")

        # Primero revisa el stock. Si un producto se repite, suma sus cantidades.
        for linea in self.__lineas:
            cantidad_total = 0
            for otra_linea in self.__lineas:
                if otra_linea.producto == linea.producto:
                    cantidad_total += otra_linea.cantidad
            if not linea.producto.verificar_Stock(cantidad_total):
                raise StockInsuficienteError("No hay stock suficiente para confirmar.")

        # Descuenta solo después de comprobar todas las líneas.
        for linea in self.__lineas:
            linea.producto.descontar_Stock(linea.cantidad)
        self.__confirmado = True
        return True

    def marcar_Pagado(self):
        if not self.__confirmado:
            raise ValueError("Primero debe confirmar el pedido.")
        self.__pagado = True

    def despachar(self) -> bool:
        if not self.__pagado:
            raise PedidoNoPagadoError("No se puede despachar un pedido sin pagar.")
        if self.__despachado:
            raise ValueError("El pedido ya fue despachado.")
        self.__despachado = True
        return True

    def calcular_Total(self) -> float:
        total = 0
        for linea in self.__lineas:
            total += linea.calcular_Subtotal()
        return total
