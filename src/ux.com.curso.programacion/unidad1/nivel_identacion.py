#

def explicar_identacion():
    #nivel 1
    mensaje ="nivel 1 de identacion"
    print(mensaje)

    puntos =10
    
    if puntos >9:
        #Nivel 2
        print("entra al flujo de if")

        if puntos ==10:
            #nivel 3
            print("puntos es igual a 10")

#cierra nivel 1
def main():
    explicar_identacion()

if __name__ == "__main__":
    main()