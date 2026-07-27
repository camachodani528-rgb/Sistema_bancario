import json

ARCHIVO = "data/clientes.json"


def guardar_cliente(cliente):

    with open(ARCHIVO, "r") as archivo:
        clientes = json.load(archivo)

    clientes.append(cliente)

    with open(ARCHIVO, "w") as archivo:
        json.dump(clientes, archivo, indent=4)