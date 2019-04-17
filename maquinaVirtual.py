
from Memoria import * 

#Memoria virtual que almacena datos de manera global
memGlobal = Memoria()

#Pila de memorias
memory = [memGlobal]

#Lista que almacena los valores de los cuadruplos generados
cuadruplos = []

#Contador que apunta al cuadruplo que se va a ejecutar
iEjecutando = 0

#Variable que almacena la posición en la que estaba la ejecución de los cuadruplos antes de hacer el llamado a una función.
iLlamadaAFuncion = 0

# Se sincronizan los datos con los del compilador Rose
# Valor que habilita la cantidad de espacios disponibles para cada tipo de dato
espaciosDisponibles = 1000

#1 Valor que apunta al primer lugar disponible de los int locales
iIntLocales = espaciosDisponibles

#2 Valor que apunta al primer lugar disponible de los float locales
iFloatLocales = iIntLocales + espaciosDisponibles

#3 Valor que apunta al primer lugar disponible de los bool locales
iBoolLocales = iFloatLocales + espaciosDisponibles

#4 Valor que apunta al primer lugar disponible de los strings locales
iStringLocales = iBoolLocales + espaciosDisponibles

#5 Valor que apunta al primer lugar disponible de los int locales
iIntGlobales = iStringLocales + espaciosDisponibles

#6 Valor que apunta al primer lugar disponible de los float locales
iFloatGlobales = iIntGlobales + espaciosDisponibles

#7 Valor que apunta al primer lugar disponible de los bool locales
iBoolGlobales = iFloatGlobales + espaciosDisponibles

#8 Valor que apunta al primer lugar disponible de los strings locales
iStringGlobales = iBoolGlobales + espaciosDisponibles

#9 Valor que apunta al primer lugar disponible de los int temporales
iIntTemporales = iStringGlobales + espaciosDisponibles

#10 Valor que apunta al primer lugar disponible de los float temporales
iFloatTemporales = iIntTemporales + espaciosDisponibles

#11 Valor que apunta al primer lugar disponible de los bool temporales
iBoolTemporales = iFloatTemporales + espaciosDisponibles

#12 Valor que apunta al primer lugar disponible de los strings temporales
iStringTemporales = iBoolTemporales + espaciosDisponibles

#13 Valor que apunta al siguiente lugar disponible de los int
iIntConst = iStringTemporales + espaciosDisponibles

#14 Valor que apunta al siguiente lugar disponible de los float
iFloatConst = iIntConst + espaciosDisponibles

#15 Valor que apunta al siguiente lugar disponible de los bool
iBoolConst = iFloatConst + espaciosDisponibles

#16 Valor que apunta al siguiente lugar disponible de los strings
iStringConst = iBoolConst + espaciosDisponibles

#Archivo a leer
compiledFile = open("codeobj.rs","r")


#Regresa el tipo de dato al que pertenece la dirección de memoria proporcionada.
def checkTipo(iMemAdd1):
	tipo = 'none'
	iMemAdd = int(iMemAdd1)
	#print(iMemAdd)
	if (iMemAdd >= 0 and iMemAdd < iIntLocales) or (iMemAdd >= iStringLocales and iMemAdd < iIntGlobales) or (iMemAdd >= iStringGlobales and iMemAdd < iIntTemporales) or (iMemAdd >= iStringTemporales and iMemAdd < iIntConst):
		tipo = 'int'
	if (iMemAdd >= iIntLocales and iMemAdd < iFloatLocales) or (iMemAdd >= iIntGlobales and iMemAdd < iFloatGlobales) or (iMemAdd >= iIntTemporales and iMemAdd < iFloatTemporales) or (iMemAdd >= iIntConst and iMemAdd < iFloatConst):
		tipo = 'float'
	if (iMemAdd >= iFloatLocales and iMemAdd < iBoolLocales) or (iMemAdd >= iFloatGlobales and iMemAdd < iBoolGlobales) or (iMemAdd >= iFloatTemporales and iMemAdd < iBoolTemporales) or (iMemAdd >= iFloatConst and iMemAdd < iBoolConst):
		tipo = 'bool'
	if (iMemAdd >= iBoolLocales and iMemAdd < iStringLocales) or (iMemAdd >= iBoolGlobales and iMemAdd < iStringGlobales) or (iMemAdd >= iBoolTemporales and iMemAdd < iStringTemporales) or (iMemAdd >= iBoolConst and iMemAdd < iStringConst):
		tipo = 'string'
	return tipo

#Regresa el cuadruplo de la posición solicitada
def setCuadruplo(iPosicion):
	global iEjecutando
	if (iPosicion > 0):
		iEjecutando = iPosicion
	else:
		iEjecutando += 1

'''
def getData(memAdd):
	global memoria
	tempTipo = checkTipo(memAdd)
	return memoria.getValue(tempTipo,memAdd)
'''
#Lleva a cabo el cuádruplo
def ejecutaCuadruplo():
	global iEjecutando
	global cuadruplos
	global memory
	global memoria
	
	memoria = memory.pop()
	currentCuad = cuadruplos[iEjecutando]
	#print(currentCuad)
	nextCuad = -1
	#Brincos
	if currentCuad[0] == 'GoTo':
		nextCuad = int(currentCuad[3])
	if currentCuad[0] == 'GoToF':
		memAddress = currentCuad[1]
		tipo = checkTipo(memAddress)
		if memoria.getValue(tipo,memAddress) == 15000:
			nextCuad = int(currentCuad[3])

	#Adjuntar constantes
	if currentCuad[0] == 'addConstString':
		memoria.addValue(checkTipo(currentCuad[3]),currentCuad[3],currentCuad[1])
	if currentCuad[0] == 'addConstInt':
		memoria.addValue(checkTipo(currentCuad[3]),currentCuad[3],currentCuad[1])
	if currentCuad[0] == 'addConstFloat':
		memoria.addValue(checkTipo(currentCuad[3]),currentCuad[3],currentCuad[1])
	
	#Operadores
	if currentCuad[0] == '=':
		memoria.addValue(checkTipo(currentCuad[3]), currentCuad[3],currentCuad[1])
	if currentCuad[0] == '+':
		#print("operadorUno")
		operadorUno = memoria.getValue(checkTipo(int(currentCuad[1])),currentCuad[1])
		#print("operadorDosUno")
		operadorDos = memoria.getValue(checkTipo(int(currentCuad[2])),currentCuad[2])
		resultado = operadorUno + operadorDos
		memoria.addValue(checkTipo(currentCuad[3]),currentCuad[3],resultado)
	if currentCuad[0] == '-':
		operadorUno = memoria.getValue(checkTipo(int(currentCuad[1])),currentCuad[1])
		operadorDos = memoria.getValue(checkTipo(int(currentCuad[2])),currentCuad[2])
		resultado = operadorUno - operadorDos
		memoria.addValue(checkTipo(currentCuad[3]),currentCuad[3],resultado)
	if currentCuad[0] == '*':
		operadorUno = memoria.getValue(checkTipo(int(currentCuad[1])),currentCuad[1])
		operadorDos = memoria.getValue(checkTipo(int(currentCuad[2])),currentCuad[2])
		resultado = operadorUno * operadorDos
		memoria.addValue(checkTipo(currentCuad[3]),currentCuad[3],resultado)
	if currentCuad[0] == '/':
		operadorUno = memoria.getValue(checkTipo(int(currentCuad[1])),currentCuad[1])
		operadorDos = memoria.getValue(checkTipo(int(currentCuad[2])),currentCuad[2])
		if operadorDos == 0:
			print("Division by 0")
			sys.exit()
		resultado = operadorUno / operadorDos
		memoria.addValue(checkTipo(currentCuad[3]),currentCuad[3],resultado)

	#Operadores logicos
	###HAY QUE CHECAR TODAS LAS QUE REGRESAN UN BOOL
	if currentCuad[0] == '==':
		operadorUno = memoria.getValue(checkTipo(int(currentCuad[1])),currentCuad[1])
		operadorDos = memoria.getValue(checkTipo(int(currentCuad[2])),currentCuad[2])
		if operadorUno == operadorDos:
			resultado = 'true'
		else:
			resultado = 'false'
		memoria.addValue(checkTipo(currentCuad[3]),currentCuad[3],resultado)
	if currentCuad[0] == 'AND':
		operadorUno = memoria.getValue(checkTipo(int(currentCuad[1])),currentCuad[1])
		operadorDos = memoria.getValue(checkTipo(int(currentCuad[2])),currentCuad[2])
		if operadorUno and operadorDos:
			resultado = 'true'
		else:
			resultado = 'false'
		memoria.addValue(checkTipo(currentCuad[3]),currentCuad[3],resultado)
	if currentCuad[0] == 'OR':
		operadorUno = memoria.getValue(checkTipo(int(currentCuad[1])),currentCuad[1])
		operadorDos = memoria.getValue(checkTipo(int(currentCuad[2])),currentCuad[2])
		if operadorUno or operadorDos:
			resultado = 'true'
		else:
			resultado = 'false'
		memoria.addValue(checkTipo(currentCuad[3]),currentCuad[3],resultado)

	#Llamadas a funciones definidas por el usuario
	if currentCuad[0] == 'era':
		memAux = Memoria()
		memory.push(memAux)
	if currentCuad[0] == 'endProc':
		memoria = memory.pop()
		nextCuad = int(iLlamadaAFuncion)
	if currentCuad[0] == 'gosub':
		iLlamadaAFuncion = currentCuad[2]
		nextCuad = int(currentCuad[3])

	if currentCuad[0] == 'return':
		pass

	if currentCuad[0] == 'end':
		print("Se terminó la ejecución del programa.")
		memoria.printMem()
		entrada = input()
		sys.exit()

	#Funciones Especiales
	if currentCuad[0] == 'print':
		operadorUno = memoria.getValue(checkTipo(int(currentCuad[1])),currentCuad[1])
		print(operadorUno)

	memory.append(memoria)
	setCuadruplo(nextCuad)
	ejecutaCuadruplo()

#Se leen los cuadruplos generados por el compilador y se modifican para que queden como estaban en el compilador
for cuad in compiledFile:
	cuad=cuad.replace('(','')
	cuad=cuad.replace(')','')
	cuad=cuad.replace('\n','')
	cuad=cuad.replace('\'','')
	tupla = tuple(cuad.split(', '))
	temp = (1,1,1,1)
	try:
		temp[0] = int(float(tupla[0]))
	except:
		#print(type(tupla[0]))
		#print("no se pudo hacer el cast de la cosa {}".format(tupla[0]))
		pass
	try:
		temp[1] = int(float(tupla[1]))
	except:
		#print(type(tupla[1]))
		#print("no se pudo hacer el cast de la cosa {}".format(tupla[1]))
		pass
	try:
		temp[2] = int(float(tupla[2]))
	except:
		#print(type(tupla[2]))
		#print("no se pudo hacer el cast de la cosa {}".format(tupla[2]))
		pass
	try:
		temp[3] = int(float(tupla[3]))
	except:
		#print(type(tupla[3]))
		#print("no se pudo hacer el cast de la cosa {}".format(tupla[3]))
		pass
	#print(temp)
	tupla = (tupla[0], tupla[1], tupla[2], tupla[3])
	cuadruplos.append(tupla)



ejecutaCuadruplo()

