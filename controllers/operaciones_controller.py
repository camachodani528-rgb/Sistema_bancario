import json

ARCHIVO = "data/cuenta.json"

def consultar_saldo():

    numero = input("Ingrese el número de la cuenta: ")

    with open(ARCHIVO, "r") as archivo:
        cuentas = json.load(archivo)

    for cuenta in cuentas:

        if cuenta["numero"] == numero:

            print("\n===== CONSULTA DE SALDO =====")
            print("Número:", cuenta["numero"])
            print("Tipo:", cuenta["tipo"])
            print("Saldo: $", cuenta["saldo"])
            return

    print("La cuenta no existe.")