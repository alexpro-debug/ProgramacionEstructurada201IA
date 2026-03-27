"""Diseñar un algoritmo que calcule la suma de
todos los numeros enteros del 1 al 100 que son
divisibles por 3 y, demas impares
"""

def es_divisible():
    suma=0
    i = 1
    while i<=100:
        if i % 3==0 and i%2!=0:
            suma+=1
        i+=1
    return suma

def main():
    suma = es_divisible()
    print(suma)

if __name__ == "__main__":
    main()