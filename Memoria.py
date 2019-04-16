#Memoria
class Memoria:
	def __init__(self):
	#Almacena la info en el orden de Int, float, bool, string
		self.memoria = ({},{},{},{})
	#Añade valor a la tupla de memoria
	def addValue(memAdd, value):
		memoria[memAdd] = value;
	#Busca el valor correspondiente al espacio de memoria solicitado
	def getValue(tipo, memAdd):
		try: 
			almacena = memoria[tipo][memAdd]
		except: 
			print("Variable declared but not initialized.")
			sys.exit()

		return almacena