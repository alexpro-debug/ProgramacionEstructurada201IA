def calcular_calificacion():
    print("--- CONVERSOR DE CALIFICACIONES ---")
    
    # 1. Leer Calificación (El paralelogramo de arriba)
    # Usamos float() por si el profe te pone un 85.5, por ejemplo.
    calificacion = float(input("Ingresa la calificación numérica (0-100): "))
    
    # 2. Rombos de decisión en cascada
    if calificacion >= 90:
        letra = 'A'
    elif calificacion >= 80:
        letra = 'B'
    elif calificacion >= 70:
        letra = 'C'
    elif calificacion >= 69:
        letra = 'D'
    else:
        # Si no cumplió ninguna de las de arriba (El último "No")
        letra = 'F'
        
    # 3. Imprimir Letra (El paralelogramo de abajo)
    print(f"\nTu calificación en letra es: {letra}")

# Esto hace que el programa arranque
calcular_calificacion()