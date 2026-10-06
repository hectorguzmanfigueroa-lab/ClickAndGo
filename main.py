from model.producto_fisico import ProductoFisico
from model.producto_digital import ProductoDigital
from model.servicio import Servicio
from model.producto_electronico import ProductoElectronico
from model.cliente import Cliente
from model.pedido import Pedido
from model.administrador import Administrador
from model.encargado_bodega import EncargadoBodega
from model.stock_insuficiente_error import StockInsuficienteError
from model.pedido_no_pagado_error import PedidoNoPagadoError


def main():
    print("--- CLICKANDGO ---")

    # Crea los tres tipos de producto.
    fisico = ProductoFisico(15000, 5)
    digital = ProductoDigital(8000, "https://example.com/descarga")
    servicio = Servicio(25000, "20-12-2026")

    print("\n1. Polimorfismo: procesar_Entrega()")
    productos = [fisico, digital, servicio]
    for producto in productos:
        print(producto.procesar_Entrega())
    print("Flete del producto físico:", fisico.calcular_Flete())

    print("\n2. Validación: setter de Cliente.correo")
    cliente = Cliente("cliente@example.com", "12345678-5")
    print("Correo válido:", cliente.correo)
    print("validar_Correo():", cliente.validar_Correo())
    print("validar_Rut():", cliente.validar_Rut())
    try:
        cliente.correo = "correo incorrecto"
    except ValueError as error:
        print("Error capturado:", error)
    print("Se conserva el correo anterior:", cliente.correo)

    print("\n3. ProductoElectronico.calcular_Precio()")
    
    electronico = ProductoElectronico(100, 2, 950)
    print("Precio con dólar de ejemplo:", electronico.calcular_Precio(950))

    print("\n4. Administrador y encargado de bodega")
    administrador = Administrador("Ana")
    bodega = EncargadoBodega("Luis")
    administrador.gestionar_Catalogo(digital)
    administrador.cambiar_Precio(digital, 7500)
    print("Precio digital cambiado por el administrador:", digital.precio)

    print("\n5. Pedido con sus líneas de detalle")
    pedido = Pedido(cliente)
    cliente.agregar_Pedido(pedido)  # Agregación: recibe el pedido ya creado.
    pedido.agregar_Linea(fisico, 2)  # Composición: el pedido crea la línea.
    pedido.agregar_Linea(digital, 1)
    pedido.agregar_Linea(servicio, 1)
    pedido.agregar_Linea(electronico, 1)
    numero = 1
    for linea in pedido.lineas:
        print("Línea:", numero)
        print("Cantidad:", linea.cantidad)
        print("Precio unitario:", linea.precioUnitario)
        print("Subtotal:", linea.calcular_Subtotal())
        numero += 1
    print("Total de productos, sin flete:", pedido.calcular_Total())
    print("Pedidos del cliente:", len(cliente.pedidos))
    pedido.confirmar()
    print("Pedido confirmado:", pedido.confirmado)
    print("Stock físico restante:", fisico.stock)
    print(bodega.preparar_Pedido(pedido))

    print("\n6. Regla de stock: Pedido.confirmar()")
    pedido_sin_stock = Pedido(cliente)
    cliente.agregar_Pedido(pedido_sin_stock)
    pedido_sin_stock.agregar_Linea(fisico, 99)
    try:
        pedido_sin_stock.confirmar()
    except StockInsuficienteError as error:
        print("StockInsuficienteError capturado:", error)
    print("El programa continúa.")

    print("\n7. Regla de pago: Pedido.despachar()")
    try:
        bodega.despachar_Pedido(pedido)
    except PedidoNoPagadoError as error:
        print("PedidoNoPagadoError capturado:", error)
    print("El programa continúa.")
    pedido.marcar_Pagado()
    bodega.despachar_Pedido(pedido)
    print("Pedido pagado:", pedido.pagado)
    print("Pedido despachado:", pedido.despachado)
    print("\nFin de la demostración.")


if __name__ == "__main__":
    main()
