class Cuenta:

    def __init__(self, numero, documento_cliente, tipo, saldo=0):
        self.numero = numero
        self.documento_cliente = documento_cliente
        self.tipo = tipo
        self.saldo = saldo

    def to_dict(self):
        return {
            "numero": self.numero,
            "documento_cliente": self.documento_cliente,
            "tipo": self.tipo,
            "saldo": self.saldo
        }