def convertir_romano():
    num = int(input("Ingrese un número entero positivo (máx 3000): "))
    
    if num > 3000 or num < 1:
        print("Número fuera de rango")
        return

    valores = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    resultado = ""
    temp_num = num
    
    for valor, letra in valores:
        while temp_num >= valor:
            resultado += letra
            temp_num -= valor
            
    print(f"El número {num} en notación romana es: {resultado}")

def main():
    convertir_romano()

if __name__ == "__main__":
    main()