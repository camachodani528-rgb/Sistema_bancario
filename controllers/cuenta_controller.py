from models.cuenta import Cuenta
import json
import os


def crear_cuenta():

    print("\n--- CREACIÓN DE CUENTA ---")

    numero = input("Número de cuenta: ")
    documento = input("Documento del cliente: ")
    tipo = input("Tipo de cuenta: ")

    cuenta = Cuenta(
        numero,
        documento,
        tipo,
        0
    )

    ruta = "data/cuentas.json"

    cuentas = []

    if os.path.exists(ruta):
        with open(ruta, "r") as archivo:
            cuentas = json.load(archivo)

    cuentas.append(cuenta.to_dict())

    with open(ruta, "w") as archivo:
        json.dump(cuentas, archivo, indent=4)

    print("Cuenta creada correctamente")