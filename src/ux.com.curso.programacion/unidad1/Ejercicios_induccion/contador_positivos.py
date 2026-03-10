#desarrollo de algoritmo contador de positivos

def contador_positivos():
    contador=0
    while True:
        numero = int(input("ingrese un numero (-1 para terminar):"))
        if numero <0:
            break;
        contador += 1

    print("cantidad de numeros positivos ingresados: ", contador)

#definicion de la funcion main (controla el flujo del programa)
def main():
    print("Bienvenido al contador de positivos")
    contador_positivos()

#llamada a la funcion main para iniciar el programa
if __name__ == "__main__":
    main()