# Limpieza de datos, normalización

umbral_bajo = 0.3
umbral_alto = 0.7
    
def clasificar_pixel (intensidad): 
    
    #Si la intensidad es menor a 0.0 o mayor a 1.0, es un valor inválido
    if intensidad < 0.0 or intensidad > 1.0:
        print("Error: Valor de pixel invalido")
        return None
    
    if 0.0 <= intensidad < umbral_bajo:
        print("Clasificacion (fondo Oscuro)")
        return "(fondo oscuro)"
    
    if umbral_bajo < intensidad < umbral_alto:
        print("Clasificacion (fondo GRIS)")
        return "gris (ruido)"
    
    if intensidad >= umbral_alto:
        print("Clasificacion (objeto brillante)")
        return "objeto (brillante)"

    print("Analisis de imagen finalizado")

import os

def cargar_y_procesar(nombre_archivo):
    datos_limpios = []
    ruido_detectado = 0
    fondo_oscuro = 0
    gris_ruido = 0
    objeto_brillante = 0

    #obtener la ruta del archivo
    ruta_script = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(ruta_script, nombre_archivo)

    try:
        with open(ruta_archivo, 'r') as archivo:
            for linea  in archivo:
                #convertir cada linea en numero flotante
                valor_crudo = float(linea.strip())

                #clasificar el valor del pixel
                clasificacion = clasificar_pixel(valor_crudo)

                #agregamos la logica de clasificacion
                if clasificacion is None:
                    ruido_detectado += 1
                else:
                    datos_limpios.append(clasificacion)
                    if clasificacion == "(fondo oscuro)":
                        fondo_oscuro+=1
                    elif clasificacion == "gris (ruido)":
                        gris_ruido+=1
                    elif clasificacion == "objeto (brillante)":
                        objeto_brillante+=1

        print("resultados de clasificacion")
        print(f"fondo oscuro: {fondo_oscuro}")
        print(f"gris (ruido): {gris_ruido}")
        print(f"objeto (brillante): {objeto_brillante}")
        print(f"ruido detectado: {ruido_detectado}")
    except FileNotFoundError:
        print(f"error: el archivo '{nombre_archivo}' no se encontro.")
                                        
def main():
    cargar_y_procesar("lecturas_sensores.txt")

if __name__ == "__main__":
    main()