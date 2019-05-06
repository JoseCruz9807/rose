
import sys

#Memoria
class Memoria:
	def __init__(self, nameMemory):
	#Almacena la info en el orden de Int, float, bool, string
		self.memoria = ({},{},{'14000': 'false', '14001':'true'},{})
		self.name = nameMemory
	def addValue(self, tipo, memAdd, value):
	""" Añade valor a la tupla de memoria
		Args:
		 tipo: Tipo del valor a añadir.
		 memAdd: Dirección de memoria que le fue asignada.
		 value: Valor que va almacenar.
	"""
		if tipo == 'int':
			dictInt = self.memoria[0]
			dictInt[memAdd] = str(value)
			self.memoria = (dictInt, self.memoria[1], self.memoria[2], self.memoria[3])
		if tipo == 'float':
			dictFloat = self.memoria[1]
			dictFloat[memAdd] = str(value)
			self.memoria = (self.memoria[0], dictFloat, self.memoria[2], self.memoria[3])
		if tipo == 'bool':
			dictBool = self.memoria[2]
			dictBool[memAdd] = str(value)
			self.memoria = (self.memoria[0], self.memoria[1], dictBool, self.memoria[3])
		if tipo == 'string':
			dictString = self.memoria[3]
			dictString[memAdd] = str(value)
			self.memoria = (self.memoria[0], self.memoria[1], self.memoria[2], dictString)
	def getValue(self, tipo, memAdd):
	""" Busca el valor correspondiente al espacio de memoria solicitado
		Args:
		 tipo: Tipo del valor a añadir.
		 memAdd: Dirección de memoria que le fue asignada.
	"""
		typeVal = -1
		if tipo == 'int':
			typeVal = 0
		if tipo == 'float':
			typeVal = 1
		if tipo == 'bool':
			typeVal = 2
		if tipo == 'string':
			typeVal = 3
		returnVal = self.memoria[typeVal][memAdd] 
		return returnVal
	def getSizeMem(self, tipo):
	""" Regresa la cantidad del diccionario del tipo especificado
		Args:
		 tipo: Tipo del valor a añadir.
	"""
		if tipo == 'int':
			size = len(self.memoria[0])
		if tipo == 'float':
			size = len(self.memoria[1])
		if tipo == 'bool':
			size = len(self.memoria[2])
		if tipo == 'string':
			size = len(self.memoria[3])
		return size
	def printMem(self):
	""" Imprime el contenido de lo que tenga almacenado.
		Args:
	"""
		print("nombre de memoria: " + self.name)
		print(self.memoria[0])
		print(self.memoria[1])
		print(self.memoria[2])
		print(self.memoria[3])