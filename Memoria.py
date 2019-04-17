
import sys
#Memoria
class Memoria:
	def __init__(self):
	#Almacena la info en el orden de Int, float, bool, string
		self.memoria = ({},{},{},{})
	#Añade valor a la tupla de memoria
	def addValue(self, tipo, memAdd, value):
		print("tipo: {}, memAdd: {}, value: {}".format(tipo, memAdd, value))
		if tipo == 'int':
			dictInt = self.memoria[0]
			dictInt[memAdd] = value
			self.memoria = (dictInt, self.memoria[1], self.memoria[2], self.memoria[3])
		if tipo == 'float':
			dictFloat = self.memoria[1]
			dictFloat[memAdd] = value
			self.memoria = (self.memoria[0], dictFloat, self.memoria[2], self.memoria[3])
		if tipo == 'bool':
			dictBool = self.memoria[2]
			dictBool[memAdd] = value
			self.memoria = (self.memoria[0], self.memoria[1], dictBool, self.memoria[3])
		if tipo == 'string':
			dictString = self.memoria[3]
			dictString[memAdd] = value
			self.memoria = (self.memoria[0], self.memoria[1], self.memoria[2], dictString)
	#Busca el valor correspondiente al espacio de memoria solicitado
	def getValue(self, tipo, memAdd):
		typeVal = -1
		try: 
			if tipo == 'int':
				typeVal = 0
			if tipo == 'float':
				typeVal = 1
			if tipo == 'bool':
				typeVal = 2
			if tipo == 'string':
				typeVal = 3
			almacena = self.memoria[typeVal][memAdd]
		except: 
			print(self.memoria[typeVal][memAdd])
			
			print("Variable declared but not initialized.")
			sys.exit()
		print("El valor en la memAdd dada es: " + almacena)
		return almacena
	#Regresa la cantidad del diccionario del tipo especificado
	def getSizeMem(self, tipo):
		#Falta hacer que esto jale
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
		print(self.memoria[0])
		print(self.memoria[1])
		print(self.memoria[2])
		print(self.memoria[3])