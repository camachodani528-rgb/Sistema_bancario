from models.cliente import Cliente
from utils.cliente_utils import guardar_cliente


def registrar_cliente():

    print("\n--- REGISTRO DE CLIENTE ---")

    nombre = input("Nombre: ")
    documento = input("Documento: ")
    telefono = input("Telefono: ")
    correo = input("Correo: ")
    direccion = input("Direccion: ")


    if nombre == "" or documento == "" or telefono == "" or correo == "" or direccion == "":
        print("Todos los campos son obligatorios")
        return


    cliente = Cliente(
        nombre,
        documento,
        telefono,
        correo,
        direccion
    )


    guardar_cliente(cliente.to_dict())


    print("Cliente registrado correctamente")