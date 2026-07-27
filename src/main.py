print("El archivo main está funcionando")

from controllers.cliente_controller import registrar_cliente
from controllers.operaciones_controller import consultar_saldo


while True:

    print("\n--- SISTEMA BANCARIO ---")
    print("1. Registrar cliente")
    print("2. Consultar saldo")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_cliente()

    elif opcion == "2":
        consultar_saldo()

    elif opcion == "3":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")