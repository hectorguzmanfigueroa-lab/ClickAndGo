class Cliente:
    def __init__(self, correo: str, rut: str):
        self.correo = correo  # Usa el setter, igual que patente en Vehiculo.
        self.__rut = rut
        self.__pedidos = []

    @property
    def correo(self) -> str:
        return self.__correo

    @correo.setter
    def correo(self, valor: str):
        # Validación básica con el mismo estilo que Vehiculo.patente.
        if len(valor) < 5 or "@" not in valor or "." not in valor or " " in valor:
            raise ValueError("El correo debe tener arroba, punto y no tener espacios.")
        self.__correo = valor

    @property
    def rut(self) -> str:
        return self.__rut

    @property
    def pedidos(self) -> list:
        return self.__pedidos

    def validar_Correo(self) -> bool:
        return (len(self.__correo) >= 5 and "@" in self.__correo
                and "." in self.__correo and " " not in self.__correo)

    def validar_Rut(self) -> bool:
        # Revisión mínima: largo, guion y ausencia de espacios.
        # No comprueba que el RUT exista ni su dígito verificador.
        return (len(self.__rut) >= 9 and len(self.__rut) <= 10
                and "-" in self.__rut and " " not in self.__rut)

    def agregar_Pedido(self, pedido):
        if pedido.cliente != self:
            raise ValueError("El pedido pertenece a otro cliente.")
        if pedido not in self.__pedidos:
            self.__pedidos.append(pedido)  # Recibe un pedido que ya existe.
