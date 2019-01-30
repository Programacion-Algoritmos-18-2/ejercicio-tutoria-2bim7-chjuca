import codecs               # Importamos las librerias necesarias
import sys


class MiArchivo:            # Creamos la clase MiArchivo 
    
    def __init__(self, nombre):             # Constructor de la clase 
        self.nombre_archivo = nombre    
        self.archivo = codecs.open(self.nombre_archivo, "r")        # Abrimos el archivo en modo lectura en la direccion recibida en el main


    def obtener_informacion(self):                     # Leemos las lineas de informacion que se encuentran en el Archivo
        return self.archivo.readlines()

    def cerrar_archivo(self):                   # Cerramos el Archivo
        self.archivo.close()