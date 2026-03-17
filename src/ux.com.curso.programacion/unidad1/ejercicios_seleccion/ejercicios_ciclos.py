#ejemplo de repeticion

def ejemplo_for():
    print("estructura FOR")

    frutas = ["manzana", "banana", "naranja"]
    #for frutas lista
    for fruta in frutas:
        print(fruta)
    # for para iterar rangos
    for i in range(1, 5):
        print(i)
    # for para iterar rangos con paso
    for i in range(1, 10, 2):
        print(i)

def ejemplo_while():
    contador = 0

    while contador < 5:
        print(contador)
        contador += 1

def ejemplo_do_while():
    print("estructura do while")

    secreto = "python12"
    intentos = 0

    while True:
        intentos_usuario = "python12" #simulamos la entrada de usuario
        intentos += 1

        if intentos_usuario == secreto:
            print("¡Acceso concedido!")
            break
        else:
            print("Acceso denegado! errg esta mal")
            break
        print("\n")

def main():
    ejemplo_for()
    print("\n")
    ejemplo_while()
    print("\n")
    ejemplo_do_while()

if __name__ == "__main__":
    main()

    



