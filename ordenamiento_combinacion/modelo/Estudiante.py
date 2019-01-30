class Estudiante(object):						 # Creamos una clase estudiante
	def __init__(self, nombre,apellido,edad):	 # Costructor de la clase
		self.nombre = nombre 						# Atributos de la clase
		self.apellido = apellido
		self.edad = edad

	def setNombre(self,nombre):					# Metodos SET y GET de la clase 
		self.nombre = nombre

	def setApellido(self,apellido):
		self.apellido = apellido

	def setEdad(self,edad):
		self.edad = edad

	def getNombre(self):
		return self.nombre

	def getApellido(self):
		return self.apellido

	def getEdad(self):
		return self.edad
	

		