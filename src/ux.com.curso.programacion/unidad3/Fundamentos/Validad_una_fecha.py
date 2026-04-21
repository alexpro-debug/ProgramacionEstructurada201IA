def validar_fecha():
    d = int(input("Ingrese el día: "))
    m = int(input("Ingrese el mes: "))
    a = int(input("Ingrese el año: "))
    
    valida = True
    
    if a < 1 or m < 1 or m > 12 or d < 1:
        valida = False
    else:
        "Lógica de días por mes"
        dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        "Ajuste por año bisiesto"
        if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
            dias_mes[1] = 29
            
        if d > dias_mes[m-1]:
            valida = False
            
    if valida:
        print("La fecha ingresada es válida")
    else:
        print("La fecha ingresada NO es válida")

def main():
    validar_fecha()

if __name__ == "__main__":
    main()