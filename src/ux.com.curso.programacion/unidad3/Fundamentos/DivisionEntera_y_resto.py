def division_procedimiento():
    dividendo = int(input("Ingrese el dividendo: "))
    divisor = int(input("Ingrese el divisor: "))
    
    cociente = 0
    residuo = dividendo
    
    while residuo >= divisor:
        residuo = residuo - divisor
        cociente = cociente + 1
        
    print(f"El cociente es {cociente} y el resto es {residuo}")

def main():
    division_procedimiento()

if __name__ == "__main__":
    main()