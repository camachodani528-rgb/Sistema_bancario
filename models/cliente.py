class Cliente:

    def __init__(self, nombre, documento, telefono, correo, direccion):
        self.nombre = nombre
        self.documento = documento
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "documento": self.documento,
            "telefono": self.telefono,
            "correo": self.correo,
            "direccion": self.direccion
        }