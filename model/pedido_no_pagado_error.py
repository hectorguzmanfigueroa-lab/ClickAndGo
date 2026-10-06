class PedidoNoPagadoError(Exception):
    pass  # Se usa para impedir el despacho cuando falta el pago.
