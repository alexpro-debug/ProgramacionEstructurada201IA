#ejercicio 3: Sincronización de Frecuencia en Agentes Multi-Agente
print("--- Comprobación de Sincronización Multi-Agente ---")
#solicitar frecuencias
freq_a = int(input("Ingresa la frecuencia de muestreo del Agente A (Hz): "))
freq_b = int(input("Ingresa la frecuencia de muestreo del Agente B (Hz): "))
#comprobar si uno es divisor exacto del otro usando el módulo (%)
#Si el residuo de la división es 0, es un divisor exacto
if (freq_a % freq_b == 0) or (freq_b % freq_a == 0):
    print("\nResultado: Existe una Relación de Sincronización de Ciclos perfecta.")
else:
    print("\nResultado: No existe sincronización perfecta entre los agentes.")