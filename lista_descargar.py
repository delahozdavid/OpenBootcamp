import os
import math

def obtener_tamano_formateado(tamano_bytes):
    # Obtener el tamaño en formato humano legible
    if tamano_bytes == 0:
        return '0B'
    unidades = ['B', 'KB', 'MB', 'GB', 'TB']
    exponente = math.floor(math.log2(tamano_bytes) / 10)
    tamano_formateado = tamano_bytes / (1024 ** exponente)
    return f'{tamano_formateado:.2f}{unidades[exponente]}'

# Ruta de la carpeta de Descargas
directorio_descargas = 'D:\David Stuff\Descargas'  # Reemplaza con la ruta a tu carpeta de Descargas

# Mostrar los archivos en la carpeta de Descargas
for raiz, directorios, archivos in os.walk(directorio_descargas):
    print(f'Directorio: {raiz}')
    
    for archivo in archivos:
        ruta_archivo = os.path.join(raiz, archivo)
        tamano = os.path.getsize(ruta_archivo)
        tamano_formateado = obtener_tamano_formateado(tamano)
        print(f'  Archivo: {archivo} - Tamaño: {tamano_formateado}')

