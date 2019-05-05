
from Memoria import * 
import re
import numpy as np
import math
import statistics

#Memoria virtual que almacena datos de manera global
memGlobal = Memoria("Global")

#Desfase entre los goto debido a las constantes usadas
desfase=0

#Memoria virtual de la función main()
memMain = Memoria("Main")

#Pila de memorias
memoryStack = [memMain]

#Pila de memorias temporal
tempMemoryStack = []

#Lista que almacena los valores de los cuadruplos generados
cuadruplos = []

#Contador que apunta al cuadruplo que se va a ejecutar
iEjecutando = 0

#Stack donde se almacenan los valores de retorno de las funciones 
returnValues = []

#Variable que almacena la posición en la que estaba la ejecución de los cuadruplos antes de hacer el llamado a una función.
iLlamadaAFuncion = []

# Se sincronizan los datos con los del compilador Rose
# Valor que habilita la cantidad de espacios disponibles para cada tipo de dato
espaciosDisponibles = 1000

#1 Valor que apunta al limite superior de los int locales
iIntLocales = espaciosDisponibles

#2 Valor que apunta al limite superior de los float locales
iFloatLocales = iIntLocales + espaciosDisponibles

#3 Valor que apunta al limite superior de los bool locales
iBoolLocales = iFloatLocales + espaciosDisponibles

#4 Valor que apunta al limite superior de los strings locales
iStringLocales = iBoolLocales + espaciosDisponibles

#5 Valor que apunta al limite superior de los int locales
iIntGlobales = iStringLocales + espaciosDisponibles

#6 Valor que apunta al limite superior de los float locales
iFloatGlobales = iIntGlobales + espaciosDisponibles

#7 Valor que apunta al limite superior de los bool locales
iBoolGlobales = iFloatGlobales + espaciosDisponibles

#8 Valor que apunta al limite superior de los strings locales
iStringGlobales = iBoolGlobales + espaciosDisponibles

#9 Valor que apunta al limite superior de los int temporales
iIntTemporales = iStringGlobales + espaciosDisponibles

#10 Valor que apunta al limite superior de los float temporales
iFloatTemporales = iIntTemporales + espaciosDisponibles

#11 Valor que apunta al limite superior de los bool temporales
iBoolTemporales = iFloatTemporales + espaciosDisponibles

#12 Valor que apunta al limite superior de los strings temporales
iStringTemporales = iBoolTemporales + espaciosDisponibles

#13 Valor que apunta al siguiente lugar disponible de los int
iIntConst = iStringTemporales + espaciosDisponibles

#14 Valor que apunta al siguiente lugar disponible de los float
iFloatConst = iIntConst + espaciosDisponibles

#15 Valor que apunta al siguiente lugar disponible de los bool
iBoolConst = iFloatConst + espaciosDisponibles

#16 Valor que apunta al siguiente lugar disponible de los strings
iStringConst = iBoolConst + espaciosDisponibles

#Valor que almacena el cuadruplo que se ejecuta actualmente
currentCuad = ()

#Valor que almacena la direccion de memoria del elemento del arreglo/matriz al que se le asignará un valor
dirMem = -1

#Valor que almacena si el parámetro que se recibe es un valor o una direccion de memoria
isMemAdd = False

#Archivo a leer
compiledFile = open("codeobj.rs","r")

#Variable que almacen el siguiente cuádruplo a ser ejecutado
nextCuad = -1

#Matriz para exportar a csv
exportData=[]


#Regresa el tipo de dato al que pertenece la dirección de memoria proporcionada.
def checkTipo(iMemAdd1):
	tipo = 'none'
	iMemAdd = int(iMemAdd1)
	#print(iMemAdd1)
	if (iMemAdd >= 0 and iMemAdd < iIntLocales) or (iMemAdd >= iStringLocales and iMemAdd < iIntGlobales) or (iMemAdd >= iStringGlobales and iMemAdd < iIntTemporales) or (iMemAdd >= iStringTemporales and iMemAdd < iIntConst):
		tipo = 'int'
	if (iMemAdd >= iIntLocales and iMemAdd < iFloatLocales) or (iMemAdd >= iIntGlobales and iMemAdd < iFloatGlobales) or (iMemAdd >= iIntTemporales and iMemAdd < iFloatTemporales) or (iMemAdd >= iIntConst and iMemAdd < iFloatConst):
		tipo = 'float'
	if (iMemAdd >= iFloatLocales and iMemAdd < iBoolLocales) or (iMemAdd >= iFloatGlobales and iMemAdd < iBoolGlobales) or (iMemAdd >= iFloatTemporales and iMemAdd < iBoolTemporales) or (iMemAdd >= iFloatConst and iMemAdd < iBoolConst):
		tipo = 'bool'
	if (iMemAdd >= iBoolLocales and iMemAdd < iStringLocales) or (iMemAdd >= iBoolGlobales and iMemAdd < iStringGlobales) or (iMemAdd >= iBoolTemporales and iMemAdd < iStringTemporales) or (iMemAdd >= iBoolConst and iMemAdd < iStringConst):
		tipo = 'string'
	return tipo


#Actualiza el valor del desfase en los cuadruplos
def setDesfase(des):
	global desfase
	desfase=int(des)
#Regresa el cuadruplo de la posición solicitada
def setCuadruplo(iPosicion):
	global iEjecutando
	if (iPosicion > 0):
		iEjecutando = iPosicion
	else:
		iEjecutando += 1

#Regresa la información almacenada en la dirección proporcionada
def getData(currentMemory, tipoDeDato, memAdd):	
	global memGlobal
	global currentCuad
	global isMemAdd
	#print("isMedAdd: " + str(isMemAdd))
	returnVal = 0
	memAdd=str(memAdd)
	try:
		returnVal = currentMemory.getValue(tipoDeDato,memAdd)
		
	except:
		try:
			returnVal = memGlobal.getValue(tipoDeDato,memAdd)
			
		except:
			if isMemAdd:
				return (memAdd)
			
			"""
			print(memAdd)
			print(tipoDeDato)
			currentMemory.printMem()
			memGlobal.printMem()
			"""
			

			print("Variable declared but not initialized.")
			sys.exit()
	return returnVal 
#Determina si la dirección proporcionada es de variables locales o no
def esGlobalOTemporal(memAddress1):
	memAddress = int(memAddress1)
	if memAddress >= iStringLocales and memAddress < iStringGlobales:
		tempVal = True
	else:
		tempVal = False
	return tempVal
#Lleva a cabo el cuádruplo
def ejecutaCuadruplo():
	global iEjecutando
	global cuadruplos
	global memoryStack
	global memoria
	global iLlamadaAFuncion
	global tempMemoryStack
	global returnValues
	global currentCuad
	global dirMem
	global isMemAdd
	global nextCuad

	isMemAdd = False
	#bEndProc = False
	memoria = memoryStack.pop()
	currentCuad = cuadruplos[iEjecutando]
	#print("Current Cuad en ejecucion: " + str(currentCuad))
	nextCuad = -1
	#Brincos
	if currentCuad[0] == 'GoTo':
		nextCuad = int(currentCuad[3])+ desfase
	if currentCuad[0] == 'GoToF':
		memAddress = currentCuad[1]
		tipo = checkTipo(memAddress)
		if getData(memoria, tipo, memAddress) == 'false':
			nextCuad = int(currentCuad[3])+desfase
	if currentCuad[0] == 'addConstString':
		memGlobal.addValue(checkTipo(currentCuad[3]),currentCuad[3],currentCuad[1])
	if currentCuad[0] == 'addConstInt':
		memGlobal.addValue(checkTipo(currentCuad[3]),currentCuad[3],currentCuad[1])
	if currentCuad[0] == 'addConstFloat':
		memGlobal.addValue(checkTipo(currentCuad[3]),currentCuad[3],currentCuad[1])
	
	#Operadores
	if currentCuad[0] == '=':
		tempTipo = checkTipo(currentCuad[1])
		valueTemp=0
		try:
			int(currentCuad[1])
			valueTemp = getData(memoria, tempTipo, currentCuad[1])
		except:
			valueTemp = returnValues.pop()
		if esGlobalOTemporal(currentCuad[3]):
			memGlobal.addValue(tempTipo, currentCuad[3], valueTemp)
		else:
			memoria.addValue(tempTipo, currentCuad[3], valueTemp)
	
	if currentCuad[0] == '+':	
		tempTipoUno = checkTipo(currentCuad[1])
		tempTipoDos = checkTipo(currentCuad[2])
		operadorUno = getData(memoria, tempTipoUno,currentCuad[1])
		operadorDos = getData(memoria, tempTipoDos,currentCuad[2])
		if tempTipoUno == 'string':
			tempOperadorUno = operadorUno[0:len(operadorUno)-1]
		if tempTipoDos == 'string':
			tempOperadorDos = operadorDos[1:len(operadorDos)]
		if tempTipoUno == 'int':
			tempOperadorUno = int(operadorUno)
		if tempTipoDos == 'int':
			tempOperadorDos = int(operadorDos)
		if tempTipoUno == 'float':
			tempOperadorUno = float(operadorUno)
		if tempTipoDos == 'float':
			tempOperadorDos = float(operadorDos)
		resultado = tempOperadorUno + tempOperadorDos

		if esGlobalOTemporal(currentCuad[3]):
			memGlobal.addValue(checkTipo(currentCuad[3]),currentCuad[3],resultado)
		else:
			memoria.addValue(checkTipo(currentCuad[3]),currentCuad[3],resultado)
	if currentCuad[0] == '-':
		tempTipoUno = checkTipo(currentCuad[1])
		tempTipoDos = checkTipo(currentCuad[2])
		operadorUno = getData(memoria, tempTipoUno,currentCuad[1])
		operadorDos = getData(memoria, tempTipoDos,currentCuad[2])
		if tempTipoUno == 'int':
			operadorUno = int(operadorUno)
		if tempTipoDos == 'int':
			operadorDos = int(operadorDos)
		if tempTipoUno == 'float':
			operadorUno = float(operadorUno)
		if tempTipoDos == 'float':
			operadorDos = float(operadorDos)
		resultado = operadorUno - operadorDos
		if esGlobalOTemporal(currentCuad[3]):
			memGlobal.addValue(checkTipo(currentCuad[3]),currentCuad[3],resultado)
		else:
			memoria.addValue(checkTipo(currentCuad[3]),currentCuad[3],resultado)
	if currentCuad[0] == '*':
		tempTipoUno = checkTipo(currentCuad[1])
		tempTipoDos = checkTipo(currentCuad[2])
		operadorUno = getData(memoria, tempTipoUno,currentCuad[1])
		operadorDos = getData(memoria, tempTipoDos,currentCuad[2])
		if tempTipoUno == 'int':
			operadorUno = int(operadorUno)
		if tempTipoDos == 'int':
			operadorDos = int(operadorDos)
		if tempTipoUno == 'float':
			operadorUno = float(operadorUno)
		if tempTipoDos == 'float':
			operadorDos = float(operadorDos)
		resultado = operadorUno * operadorDos
		if esGlobalOTemporal(currentCuad[3]):
			memGlobal.addValue(checkTipo(currentCuad[3]),currentCuad[3],resultado)
		else:
			memoria.addValue(checkTipo(currentCuad[3]),currentCuad[3],resultado)
	if currentCuad[0] == '/':
		pattern = re.compile("[0|0\.0+]")
		tempTipoDos = checkTipo(currentCuad[2])
		operadorDos = getData(memoria, checkTipo(currentCuad[2]),currentCuad[2])
		if re.search(pattern, operadorDos):
			print("Division by 0")
			sys.exit()
		
		tempTipoUno = checkTipo(currentCuad[1])
		tempTipoDos = checkTipo(currentCuad[2])
		operadorUno = getData(memoria, tempTipoUno,currentCuad[1])
		if tempTipoUno == 'int':
			operadorUno = int(operadorUno)
		if tempTipoDos == 'int':
			operadorDos = int(operadorDos)
		if tempTipoUno == 'float':
			operadorUno = float(operadorUno)
		if tempTipoDos == 'float':
			operadorDos = float(operadorDos)
		
		resultado = operadorUno / operadorDos
		if esGlobalOTemporal(currentCuad[3]):
			memGlobal.addValue(checkTipo(currentCuad[3]),currentCuad[3],resultado)
		else:
			memoria.addValue(checkTipo(currentCuad[3]),currentCuad[3],resultado)

	#Operadores logicos
	if currentCuad[0] == '<':
		operadorUno = getData(memoria, checkTipo(currentCuad[1]),currentCuad[1])
		operadorDos = getData(memoria, checkTipo(currentCuad[2]),currentCuad[2])
		if operadorUno < operadorDos:
			resultado = 'true'
		else:
			resultado = 'false'
		if esGlobalOTemporal(currentCuad[3]):
			memGlobal.addValue(checkTipo(currentCuad[3]),currentCuad[3],resultado)
		else:
			memoria.addValue(checkTipo(currentCuad[3]),currentCuad[3],resultado)
	if currentCuad[0] == '<=':
		operadorUno = getData(memoria, checkTipo(currentCuad[1]),currentCuad[1])
		operadorDos = getData(memoria, checkTipo(currentCuad[2]),currentCuad[2])
		if operadorUno <= operadorDos:
			resultado = 'true'
		else:
			resultado = 'false'
		if esGlobalOTemporal(currentCuad[3]):
			memGlobal.addValue(checkTipo(currentCuad[3]),currentCuad[3],resultado)
		else:
			memoria.addValue(checkTipo(currentCuad[3]),currentCuad[3],resultado)
	
	if currentCuad[0] == '>':
		operadorUno = getData(memoria, checkTipo(currentCuad[1]),currentCuad[1])
		operadorDos = getData(memoria, checkTipo(currentCuad[2]),currentCuad[2])
		if operadorUno > operadorDos:
			resultado = 'true'
		else:
			resultado = 'false'
		if esGlobalOTemporal(currentCuad[3]):
			memGlobal.addValue(checkTipo(currentCuad[3]),currentCuad[3],resultado)
		else:
			memoria.addValue(checkTipo(currentCuad[3]),currentCuad[3],resultado)
	if currentCuad[0] == '>=':
		operadorUno = getData(memoria, checkTipo(currentCuad[1]),currentCuad[1])
		operadorDos = getData(memoria, checkTipo(currentCuad[2]),currentCuad[2])
		if operadorUno > operadorDos:
			resultado = 'true'
		else:
			resultado = 'false'
		if esGlobalOTemporal(currentCuad[3]):
			memGlobal.addValue(checkTipo(currentCuad[3]),currentCuad[3],resultado)
		else:
			memoria.addValue(checkTipo(currentCuad[3]),currentCuad[3],resultado)

	if currentCuad[0] == '==':
		operadorUno = getData(memoria, checkTipo(currentCuad[1]),currentCuad[1])
		operadorDos = getData(memoria, checkTipo(currentCuad[2]),currentCuad[2])
		if operadorUno == operadorDos:
			resultado = 'true'
		else:
			resultado = 'false'
		if esGlobalOTemporal(currentCuad[3]):
			memGlobal.addValue(checkTipo(currentCuad[3]),currentCuad[3],resultado)
		else:
			memoria.addValue(checkTipo(currentCuad[3]),currentCuad[3],resultado)
	
	if currentCuad[0] == '!=':
		operadorUno = getData(memoria, checkTipo(currentCuad[1]),currentCuad[1])
		operadorDos = getData(memoria, checkTipo(currentCuad[2]),currentCuad[2])
		if operadorUno != operadorDos:
			resultado = 'true'
		else:
			resultado = 'false'
		if esGlobalOTemporal(currentCuad[3]):
			memGlobal.addValue(checkTipo(currentCuad[3]),currentCuad[3],resultado)
		else:
			memoria.addValue(checkTipo(currentCuad[3]),currentCuad[3],resultado)
	
	if currentCuad[0] == 'AND':
		operadorUno = getData(memoria, checkTipo(currentCuad[1]),currentCuad[1])
		operadorDos = getData(memoria, checkTipo(currentCuad[2]),currentCuad[2])
		if operadorUno and operadorDos:
			resultado = 'true'
		else:
			resultado = 'false'
		if esGlobalOTemporal(currentCuad[3]):
			memGlobal.addValue(checkTipo(currentCuad[3]),currentCuad[3],resultado)
		else:
			memoria.addValue(checkTipo(currentCuad[3]),currentCuad[3],resultado)
	if currentCuad[0] == 'OR':
		operadorUno = getData(memoria, checkTipo(currentCuad[1]),int(currentCuad[1]))
		operadorDos = getData(memoria, checkTipo(currentCuad[2]),int(currentCuad[2]))
		if operadorUno or operadorDos:
			resultado = 'true'
		else:
			resultado = 'false'
		if esGlobalOTemporal(currentCuad[3]):
			memGlobal.addValue(checkTipo(currentCuad[3]),currentCuad[3],resultado)
		else:
			memoria.addValue(checkTipo(currentCuad[3]),currentCuad[3],resultado)

	#Llamadas a funciones definidas por el usuario
	if currentCuad[0] == 'era':
		memAux = Memoria(currentCuad[1])
		tempMemoryStack.append(memAux)
	if currentCuad[0] == 'parameter':
		if True:#len(memoryStack) > 0:
			memoriaFuncionSiguiente = memoria#memoryStack.pop()
			paramValue = getData(memoriaFuncionSiguiente, checkTipo(currentCuad[1]), currentCuad[1])
			#memoryStack.append(memoriaFuncionSiguiente)
			tipoTemp = checkTipo(currentCuad[1])
			baseAddress = 0
			if tipoTemp == 'int':
				baseAddress = 0
			if tipoTemp == 'float':
				baseAddress = iIntLocales
			if tipoTemp == 'bool':
				baseAddress = iFloatLocales
			if tipoTemp == 'string':
				baseAddress = iBoolLocales
			memoriaTemp=tempMemoryStack.pop()
			localAdd = baseAddress + memoriaTemp.getSizeMem(tipoTemp)
			memoriaTemp.addValue(tipoTemp, str(localAdd), paramValue)
			tempMemoryStack.append(memoriaTemp)
	if currentCuad[0] == 'endproc':
		#bEndProc = True
		memoria=memoryStack.pop()
		nextCuad = int(iLlamadaAFuncion.pop()) + desfase
	if currentCuad[0] == 'gosub':
		memoriaTemp=tempMemoryStack.pop()
		memoryStack.append(memoria)
		memoria=memoriaTemp
		iLlamadaAFuncion.append(int(currentCuad[2]))
		nextCuad = int(currentCuad[3]) + desfase
	
	if currentCuad[0] == 'return':
		#memoriaFuncionPrevia = memoryStack.pop()
		valorTemporal = getData(memoria, checkTipo(currentCuad[3]), currentCuad[3])
		returnValues.append(valorTemporal)
		
	if currentCuad[0] == 'end':
		print("Se terminó la ejecución del programa.")
		memoria.printMem()
		memGlobal.printMem()
		entrada = input()
		sys.exit()

	if currentCuad[0]=='offset':
		setDesfase(currentCuad[1])

	#Funciones Especiales
	if currentCuad[0] == 'print':
		operadorUno = getData(memoria, checkTipo(currentCuad[1]), currentCuad[1])
		print('console>' + str(operadorUno))
	
	if currentCuad[0] == 'read':
		valueTemp = ''
		typeTemp = ''
		valueTemp = input()
		memAddTemp = currentCuad[3]

		try:
			int(valueTemp)
			typeTemp = 'int'
		except:
			try: 
				float(valueTemp)
				typeTemp='float'
			except:
				str(valueTemp)
				if valueTemp == 'true' or valueTemp == 'false':
					typeTemp = 'bool'
				else:
					typeTemp = 'string'

		if typeTemp == checkTipo(memAddTemp):
			if esGlobalOTemporal(memAddTemp):
				memGlobal.addValue(checkTipo(memAddTemp), memAddTemp, valueTemp)
			else:
				memoria.addValue(checkTipo(memAddTemp), memAddTemp, valueTemp)
		else:
			print("Wrong input, expected {} received {} instead.".format(checkTipo(memAddTemp), typeTemp))
			sys.exit()
			return



	if currentCuad[0] == 'read*':
		isMemAdd = True
		valueLectura = ''
		typeTemp = ''
		valueLectura = input()
		posicionMemoria=getData(memoria,checkTipo(currentCuad[3]), currentCuad[3])
		tempTipo = checkTipo(posicionMemoria)
		valueTemp = 0
		try:
			int(currentCuad[1])
			valueTemp = getData(memoria, tempTipo, currentCuad[1])
		except:
			valueTemp = returnValues.pop()
		

		if esGlobalOTemporal(posicionMemoria):
			memGlobal.addValue(tempTipo, posicionMemoria, valueTemp)
		else:
			memoria.addValue(tempTipo, posicionMemoria, valueTemp)

		try:
			int(valueLectura)
			typeTemp = 'int'
		except:
			try: 
				float(valueLectura)
				typeTemp='float'
			except:
				str(valueLectura)
				if valueTemp == 'true' or valueTemp == 'false':
					typeTemp = 'bool'
				else:
					typeTemp = 'string'

		if typeTemp == tempTipo:
			if esGlobalOTemporal(posicionMemoria):
				memGlobal.addValue(tempTipo, posicionMemoria, valueLectura)
			else:
				memoria.addValue(tempTipo, posicionMemoria, valueLectura)
		else:
			print("Wrong input, expected {} received {} instead.".format(checkTipo(posicionMemoria), typeTemp))
			sys.exit()
			return
	
	if currentCuad[0]=='sqrt':
		parametro=getData(memoria, checkTipo(currentCuad[1]), currentCuad[1])
		if float(parametro)<0:
			print("Math error, negative squarte root")
			sys.exit()
			return
		parametro = np.sqrt(float(parametro))
		memoria.addValue(checkTipo(currentCuad[3]),currentCuad[3],parametro)

	if currentCuad[0]=='pow':
		parametro=getData(memoria, checkTipo(currentCuad[1]), currentCuad[1])
		parametro2=getData(memoria, checkTipo(currentCuad[2]), currentCuad[2])
		parametro=np.power(float(parametro),float(parametro2))
		memoria.addValue(checkTipo(currentCuad[3]),currentCuad[3],parametro)

	if currentCuad[0]=='abs':
		parametro=getData(memoria, checkTipo(currentCuad[1]), currentCuad[1])
		parametro = np.absolute(float(parametro))
		if checkTipo(currentCuad[3])=='int':
			memoria.addValue(checkTipo(currentCuad[3]),currentCuad[3],int(parametro))
		else:
			memoria.addValue(checkTipo(currentCuad[3]),currentCuad[3],float(parametro))

	if currentCuad[0]=='sin':
		parametro=getData(memoria, checkTipo(currentCuad[1]), currentCuad[1])
		parametro = np.sin(float(parametro))
		memoria.addValue(checkTipo(currentCuad[3]),currentCuad[3],parametro)

	if currentCuad[0]=='cos':
		parametro=getData(memoria, checkTipo(currentCuad[1]), currentCuad[1])
		parametro = np.sin(float(parametro))
		memoria.addValue(checkTipo(currentCuad[3]),currentCuad[3],parametro)

	if currentCuad[0]=='factorial':
		parametro=getData(memoria, checkTipo(currentCuad[1]), currentCuad[1])
		if int(parametro)<0:
			print("Math error, negative factorial")
			sys.exit()
			return
		parametro = math.factorial(int(parametro))
		memoria.addValue(checkTipo(currentCuad[3]),currentCuad[3],parametro)

	if currentCuad[0]=='stdev':
		space=0
		result=[]
		memoriaBase=int(currentCuad[1])
		for x in range (int(currentCuad[2])):
			result.append(float(getData(memoria, checkTipo(memoriaBase+x), memoriaBase+x)))
		memoria.addValue(checkTipo(currentCuad[3]),currentCuad[3], np.std(result))

	if currentCuad[0]=='mean':
		space=0
		result=[]
		memoriaBase=int(currentCuad[1])
		for x in range (int(currentCuad[2])):
			result.append(float(getData(memoria, checkTipo(memoriaBase+x), memoriaBase+x)))
		memoria.addValue(checkTipo(currentCuad[3]),currentCuad[3], np.mean(result))

	if currentCuad[0]=='median':
		space=0
		result=[]
		memoriaBase=int(currentCuad[1])
		for x in range (int(currentCuad[2])):
			result.append(float(getData(memoria, checkTipo(memoriaBase+x), memoriaBase+x)))
		memoria.addValue(checkTipo(currentCuad[3]),currentCuad[3], np.median(result))


	if currentCuad[0]=='mode':
		space=0
		result=[]
		memoriaBase=int(currentCuad[1])
		for x in range (int(currentCuad[2])):
			if checkTipo(memoriaBase+x)=='int':
				result.append(int(getData(memoria, checkTipo(memoriaBase+x), memoriaBase+x)))
			elif checkTipo(memoriaBase+x)=='float':
				result.append(float(getData(memoria, checkTipo(memoriaBase+x), memoriaBase+x)))
			elif checkTipo(memoriaBase+x)=='string':
				result.append(str(getData(memoria, checkTipo(memoriaBase+x), memoriaBase+x)))
		try:
			memoria.addValue(checkTipo(currentCuad[3]),currentCuad[3], statistics.mode(result))
		except:
			memoria.addValue(checkTipo(currentCuad[3]),currentCuad[3], getData(memoria, checkTipo(memoriaBase), memoriaBase))

	if currentCuad[0]=='sort':
		space=0
		result=[]
		memoriaBase=int(currentCuad[1])
		for x in range (int(currentCuad[2])):
			if checkTipo(memoriaBase+x)=='int':
				result.append(int(getData(memoria, checkTipo(memoriaBase+x), memoriaBase+x)))
			elif checkTipo(memoriaBase+x)=='float':
				result.append(float(getData(memoria, checkTipo(memoriaBase+x), memoriaBase+x)))
			elif checkTipo(memoriaBase+x)=='string':
				result.append(str(getData(memoria, checkTipo(memoriaBase+x), memoriaBase+x)))
		result.sort()
		for x in range (int(currentCuad[2])):
			memoria.addValue(checkTipo(memoriaBase+x),str(memoriaBase+x), result[x])


	if currentCuad[0]=='export1':
		memoriaBase=int(currentCuad[1])
		columnas=int(currentCuad[2])
		filas=int(currentCuad[3])
		arregloTemporal=[]
		for fila in range(filas):
			arregloTemporal=[]
			for columna in range(columnas):
				x=memoriaBase+columna+fila*columnas
				arregloTemporal.append(getData(memoria, checkTipo(x), x))
			exportData.append(arregloTemporal)

	if currentCuad[0]=='export2':
		titulo=getData(memoria, checkTipo(currentCuad[1]),currentCuad[1])
		titulo=titulo[:-1]
		titulo=titulo[1:]
		f= open(titulo+".csv","w+")
		for fila in exportData:
			renglon=''
			for valor in fila:
				renglon=renglon+","+valor
			renglon=renglon[1:]
			f.write(renglon+"\n")
		f.close() 

	#Procedimientos para arreglos y matrices
	if currentCuad[0]=='ver':
		isMemAdd = True
		
		valor=getData(memoria, checkTipo(currentCuad[3]),currentCuad[3])
		limite=int(currentCuad[1])
		if int(valor)<0 or int(valor)>=limite:
			print("Out of bounds")
			sys.exit()

	if currentCuad[0]=='**':
		isMemAdd = True
		valor=getData(memoria, checkTipo(currentCuad[1]),currentCuad[1])
		factor=int(currentCuad[2])
		valueTemp=int(valor)*factor#getData(memoria,checkTipo(valor*factor), valor*factor)
		if esGlobalOTemporal(currentCuad[3]):
			memGlobal.addValue(checkTipo(currentCuad[3]), currentCuad[3], valueTemp)
		else:
			memoria.addValue(checkTipo(currentCuad[3]), currentCuad[3], valueTemp)

	if currentCuad[0]=='+*':
		isMemAdd = True
		valorTupla=getData(memoria, checkTipo(currentCuad[1]),currentCuad[1])
		valor = valorTupla[0]
		dirBase=int(currentCuad[2])
		valueTemp=int(valor)+dirBase#getData(memoria,checkTipo(valor+factor), valor+factor)
		y=getData(memoria, checkTipo(currentCuad[2]), valueTemp)
		if esGlobalOTemporal(currentCuad[3]):
			memGlobal.addValue(checkTipo(currentCuad[2]), currentCuad[3], y)
		else:
			memoria.addValue(checkTipo(currentCuad[2]), currentCuad[3], y)

	if currentCuad[0]=='=*':
		isMemAdd = True
		posicionMemoria=getData(memoria,checkTipo(currentCuad[3]), currentCuad[3])
		tempTipo = checkTipo(posicionMemoria)
		valueTemp=0
		try:
			int(currentCuad[1])
			valueTemp = getData(memoria, tempTipo, currentCuad[1])
		except:
			valueTemp = returnValues.pop()
		if esGlobalOTemporal(posicionMemoria):
			memGlobal.addValue(tempTipo, posicionMemoria, valueTemp)
		else:
			memoria.addValue(tempTipo, posicionMemoria, valueTemp)
		


	if currentCuad[0]=='+**':
		isMemAdd = True
		valorTupla=getData(memoria, checkTipo(currentCuad[1]),currentCuad[1])
		valor = valorTupla[0]
		dirBase=int(currentCuad[2])
		valueTemp=int(valor)+dirBase#getData(memoria,checkTipo(valor+factor), valor+factor)
		#y=getData(memoria, checkTipo(currentCuad[2]), valueTemp)
		if esGlobalOTemporal(currentCuad[3]):
			memGlobal.addValue(checkTipo(currentCuad[3]), currentCuad[3], valueTemp)
		else:
			memoria.addValue(checkTipo(currentCuad[3]), currentCuad[3], valueTemp)

	#if bEndProc == False:
	memoryStack.append(memoria)

	

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
		pass
	try:
		temp[1] = int(float(tupla[1]))
	except:
		pass
	try:
		temp[2] = int(float(tupla[2]))
	except:
		pass
	try:
		temp[3] = int(float(tupla[3]))
	except:
		pass
	tupla = (tupla[0], tupla[1], tupla[2], tupla[3])
	cuadruplos.append(tupla)

ejecutaCuadruplo()
while True:
	setCuadruplo(nextCuad)
	ejecutaCuadruplo()