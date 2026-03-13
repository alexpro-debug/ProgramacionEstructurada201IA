#implementacin de match en python

def demostracion():
    print("-- Ejemplo de match")
    opcion = input("ingrese una opcion (1-3): ")

    match opcion:
        case "1":
            print("opcion 1 seleccionada")
            nombre = input("ingrese su nombre: ")
            print(f"hola, {nombre}")
        case "2":
            print("opcion 2 seleccionada")
            matricula = input("ingrese su matricula: ")
            print(f"su matricula es: {matricula}")
        case "3":
            print("opcion 3 seleccionada")
            semestre = input("ingrese su semestre: ")
            print(f"usted esta en el semetre: {semestre}")
        case _:
            print("opcion no valida")

def main():
    demostracion()

if __name__ == "__main__":
    main()
