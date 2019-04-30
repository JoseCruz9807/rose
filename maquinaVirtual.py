
from Memoria import * 
import re

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

#Variable donde se almacenan los valores de retorno de las funciones 
returnValue=0

#Variable que almacena la posición en la que estaba la ejecución de los cuadruplos antes de hacer el llamado a una función.
iLlamadaAFuncion = []

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

#Valor que almacena el cuadruplo que se ejecuta actualmente
currentCuad = ()

#Valor que almacena la direccion de memoria del elemento del arreglo/matriz al que se le asignará un valor
dirMem = -1

#Valor que almacena si el parámetro que se recibe es un valor o una direccion de memoria
isMemAdd = False

#Archivo a leer
compiledFile = open("codeobj.rs","r")


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
	if memAddress >= iStringLocales and memAddress < iStringTemporales:
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
	global returnValue
	global currentCuad
	global dirMem
	global isMemAdd

	isMemAdd = False
	bEndProc = False
	memoria = memoryStack.pop()
	currentCuad = cuadruplos[iEjecutando]
	print(currentCuad)
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
		tempTipo = checkTipo(currentCuad[3])
		valueTemp=0
		try:
			int(currentCuad[1])
			valueTemp = getData(memoria, tempTipo, currentCuad[1])
		except:
			valueTemp = returnValue
		if esGlobalOTemporal(currentCuad[3]):
			memGlobal.addValue(tempTipo, currentCuad[3], valueTemp)
		else:
			memoria.addValue(tempTipo, currentCuad[3], valueTemp)
	if currentCuad[0] == '+':
		"""
		
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
		print(tempTipoUno)
		print(operadorUno)
		print(tempTipoDos)
		print(operadorDos)
		resultado = tempOperadorUno + tempOperadorDos
		
		Mi intento de solucionarlo, corre, y es aquí donde se nota que hay un error
		"""
		
		tempTipoUno = checkTipo(currentCuad[1])
		tempTipoDos = checkTipo(currentCuad[2])
		operadorUno = getData(memoria, tempTipoUno,currentCuad[1])
		operadorDos = getData(memoria, tempTipoDos,currentCuad[2])
		tempOperadorUno = operadorUno
		tempOperadorDos = operadorDos

		if tempTipoUno == 'string' and tempTipoDos == 'string':
			tempOperadorUno = operadorUno[0:len(operadorUno)-1]
			tempOperadorDos = operadorDos[1:len(operadorDos)]
		if tempTipoUno == 'float' and tempTipoDos == 'float':
			tempOperadorUno = float(operadorUno)
			tempOperadorDos = float(operadorDos)
		if tempTipoUno == 'int' and tempTipoDos == 'int':
			tempOperadorUno = int(operadorUno)
			tempOperadorDos = int(operadorDos)
		
		print(tempTipoUno)
		print(operadorUno)
		print(tempTipoDos)
		print(operadorDos)
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
	if currentCuad[0] == '=>':
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
		returnValue = getData(memoria, checkTipo(currentCuad[3]), currentCuad[3])


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
		factor=int(currentCuad[2])
		valueTemp=int(valor)+factor#getData(memoria,checkTipo(valor+factor), valor+factor)
		y=getData(memoria, checkTipo(currentCuad[2]), valueTemp)
		if esGlobalOTemporal(currentCuad[3]):
			memGlobal.addValue(checkTipo(currentCuad[3]), currentCuad[3], y)
		else:
			memoria.addValue(checkTipo(currentCuad[3]), currentCuad[3], y)

	if currentCuad[0]=='=*':
		isMemAdd = True
		direccionMemoriaTupla = str(getData(memoria,checkTipo(currentCuad[1]), getData(memoria, checkTipo(currentCuad[3]), currentCuad[3])))
		direccionMemoria = direccionMemoriaTupla[0]
		valor=getData(memoria, checkTipo(currentCuad[1]),currentCuad[1])
		if esGlobalOTemporal(direccionMemoria):
			memGlobal.addValue(checkTipo(currentCuad[1]), valor, direccionMemoria)
		else:
			memoria.addValue(checkTipo(currentCuad[1]), valor, direccionMemoria)


	if bEndProc == False:
		memoryStack.append(memoria)

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
