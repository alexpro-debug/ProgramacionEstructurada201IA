#desarrollo de algoritmo contador de positivos

def contador_positivos():
    contador=0
    while True:
        numero = int(input("ingrese un numero (-1 para terminar):"))
        if numero <0:
            break;
        contador += 1

    print("cantidad de numeros positivos ingresados: ", contador)

"""definicion de la funcion main (controla el flujo del programa)
se encarga de darle vida a la interfaz donde luego se podran introducir los numeros"""
def main():
    print("Bienvenido al contador de positivos")
    contador_positivos()

"""esta son las lineas para la llamada a la funcion main para iniciar el programa
donde el name funciona como base para la funcion main y poder ingresar los numeros"""
if __name__ == "__main__":
    main()