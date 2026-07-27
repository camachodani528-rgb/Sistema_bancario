print("El archivo main está funcionando")

from controllers.cliente_controller import registrar_cliente
from controllers.operaciones_controller import consultar_saldo


while True:

    print("\n--- SISTEMA BANCARIO ---")
    print("1. Registrar cliente")
    print("2. Crear cuenta")
    print("3. Consultar saldo")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_cliente()


    elif opcion == "3":
        consultar_saldo()

    elif opcion == "4":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")