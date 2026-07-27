print("El archivo main está funcionando")

from controllers.cliente_controller import registrar_cliente


while True:

    print("\n--- SISTEMA BANCARIO ---")
    print("1. Registrar cliente")
    print("2. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_cliente()

    elif opcion == "2":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")