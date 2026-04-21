def generar_cuadricula_multiplicar():
    limite = int(input("¿Hasta qué número desea la tabla? (Ej. 15): "))
    
    #Imprimir la fila del encabezado (los números de arriba)
    print("\t", end="") #Espacio inicial para la esquina superior izquierda
    for i in range(1, limite + 1):
        print(f"{i}\t", end="")
    print() #Salto de línea
    
    #Imprimir la línea decorativa de asteriscos
    print("**\t", end="")
    for i in range(1, limite + 1):
        print("**\t", end="")
    print()
    
    #Imprimir el cuerpo de la tabla
    for i in range(1, limite + 1):
        #Imprimir el número de la fila con un asterisco (ej. 1*)
        print(f"{i}*\t", end="")
        
        #Imprimir los resultados de las multiplicaciones
        for j in range(1, limite + 1):
            print(f"{i * j}\t", end="")
        print() #Salto de línea al terminar cada fila

def main():
    generar_cuadricula_multiplicar()

if __name__ == "__main__":
    main()