#Ejercicio 4: Estimación de Activación de Neurona Artificial (Modelo Lineal)
print("--- Cálculo de Activación de Neurona Simple ---")
#Solicitar datos al usuario
w = float(input("Ingresa el valor del 'Peso de entrada' (w): "))
x = float(input("Ingresa el valor del 'Dato de entrada' (x): "))
#calcular el valor de activación
z = w * x
#ostrar el resultado
print(f"\nEl valor de Activación (Z) es: {z}")