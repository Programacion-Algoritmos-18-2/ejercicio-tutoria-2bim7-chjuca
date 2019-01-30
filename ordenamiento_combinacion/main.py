
from combinacion import *				#Iportamos los modulos necesarios
from paquete_archivos.miarchivo import *
from modelo.Estudiante import*

m = MiArchivo("data/data.txt")		# Abrimos el archivo txt

lista = m.obtener_informacion()		# Obtenemos informacion por las lineas

lista = [l.split(";") for l in lista]	# Dividimos la cadena por el caracter ";"
lista_estudiantes=[]					#creamos arrays vacios
lista_edades=[]

for i in lista:							# For que recorrera las lineas de texto extraidas del archivo txt 
	e=Estudiante(i[0],i[1],i[2])
	lista_estudiantes.append(e)			# Agregamos el objeto a la lista creada
	lista_edades.append(int(e.getEdad()))	# Obtenemos la edad del objeto

print(lista_edades)						# Imprimimos el arreglo desordenado
merge_sort_result = merge_sort(lista_edades)  	# llamamos a la funcion merge_sort y le enviamos lista_edades

print("Lista ORDENADA")				# Presentamos un mensaje
print(merge_sort_result)			# Presentacion 

