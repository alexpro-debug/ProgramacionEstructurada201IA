# ==========================================
# IMPORTACIÓN DE BIBLIOTECAS (Biblioteca Estándar)
# ==========================================
import sys

# ==========================================
# PEGA AQUÍ LAS 3 FUNCIONES GENERADAS POR IA
# ==========================================

def limpiar_lecturas(lista_datos):
    """
    Recibe una lista de distancias y filtra los valores atípicos 
    (menores a 0.0 o mayores a 100.0). Retorna una nueva lista limpia.
    """
    lista_limpia = []
    # Validamos con condicionales tradicionales
    for dato in lista_datos:
        if dato >= 0.0 and dato <= 100.0:
            lista_limpia.append(dato)
    return lista_limpia


def calcular_alertas(lista_filtrada, umbral_critico):
    """
    Cuenta cuántas lecturas válidas están por debajo del umbral crítico.
    Retorna el total de alertas como un entero.
    """
    total_alertas = 0
    for lectura in lista_filtrada:
        if lectura < umbral_critico:
            total_alertas += 1
    return total_alertas


def generar_log_sistema(total_alertas):
    """
    Genera una cadena de texto formateada indicando si la acción es 
    PERMITIDA o se debe ABORTAR dependiendo del número de alertas.
    """
    plataforma = sys.platform
    accion = "PERMITIDA"
    
    if total_alertas > 3:
        accion = "ABORTAR"
        
    return f"[SISTEMA {plataforma}] Alertas críticas encontradas: {total_alertas}. Acción: [{accion}]"


# ==========================================
# PROGRAMA PRINCIPAL (Orquestación Manual)
# ==========================================
if __name__ == "__main__":
    # 1. Datos simulados de telemetría (con algunos errores de sensor)
    lecturas_raw = [12.5, -5.0, 88.2, 120.1, 1.2, 0.0, 45.6, 2.5]
    UMBRAL = 3.0

    print("=== SISTEMA DE TELEMETRÍA DE AGENTE AUTÓNOMO ===\n")

    # RETO DEL ALUMNO: 
    # Invoca las tres funciones en el orden estructurado correcto
    datos_limpios = limpiar_lecturas(lecturas_raw)
    alertas_detectadas = calcular_alertas(datos_limpios, UMBRAL)
    log_final = generar_log_sistema(alertas_detectadas)

    # Imprime en pantalla el Log final del sistema generado.
    print(log_final)


"""
4. reto de evaluacion y entregable

1. el prompt utilizado:
actua como un programador experto en python estructurado. escribe el codigo 
de una funcion llamada limpiar_lecturas. recibe como parametro una lista de 
numeros flotantes (lista_datos) y debe retornar una nueva lista filtrada 
eliminando valores menores a 0.0 o mayores a 100.0. restricciones estrictas: 
> 1. no utilices programacion orientada a objetos (poo). 
2. no utilices manejo de excepciones (nada de bloques try-except). gestiona 
los errores de datos usando condicionales if/else tradicionales. 
3. incluye la documentacion de la funcion mediante un docstring descriptivo.

2. tabla de pruebas de escritorio manual (trace table): 
invente estos datos de prueba: [-2.0, 150.0, 1.5, 50.0] y umbral = 2.0

paso 1 (limpiar): el for revisa uno por uno. el -2.0 y 150.0 no cumplen el if 
(>= 0 y <= 100). el 1.5 y 50.0 si entran. lista_limpia queda como [1.5, 50.0].

paso 2 (alertas): revisa [1.5, 50.0]. el 1.5 es menor al umbral de 2.0, asi que 
suma 1 a la variable total_alertas. el 50.0 no. retorna 1.

paso 3 (log): recibe el 1. como el 1 no es mayor a 3, el if de la funcion 
generar_log se salta y la accion se queda en "permitida".

3. auditoria de codigo: 
pues la ia casi siempre quiere usar comprension de listas (list comprehensions) 
para filtrar cosas en una sola linea tipo `[x for x in lista if x >= 0]`, 
pero como en la plantilla del prompt le pusimos la restriccion estricta de usar 
programacion estructurada e ifs tradicionales, la ia respeto la regla y me dio 
el codigo con un ciclo for normal y el uso de .append(), que es justo como 
lo hemos estado viendo en las clases.
"""