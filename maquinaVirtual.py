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
iLlamadaAFunción = 0

#Archivo a leer
compiledFile = open("codeobj.rs","r")

#Regresa el cuadruplo de la posición solicitada
def getCuadruplo(iPosicion):
	global iEjecutando
	if (iPosicion > 0):
		iEjecutando = iPosicion
	else:
		iEjecutando += 1

#Lleva a cabo el cuádruplo
def ejecutaCuadruplo():
	global iEjecutando
	global cuadruplos
	global memory
	memoria = memory.pop()
	currentCuad = cuadruplos[iEjecutando]
	#Brincos
	if currentCuad[0] == 'GoTo':
		getCuadruplo(currentCuad[3])
	if currentCuad[0] == 'GoToF':
		if currentCuad[1] == 'false':
			getCuadruplo(currentCuad[3])
		else:
			getCuadruplo(-1)
	#Adjuntar constantes
	if currentCuad[0] == 'addConstString':
		memoria.addValue(currentCuad[3],currentCuad[1])
		getCuadruplo(-1)
	if currentCuad[0] == 'addConstInt':
		memoria.addValue(currentCuad[3],currentCuad[1])
		getCuadruplo(-1)
	if currentCuad[0] == 'addConstFloat':
		memoria.addValue(currentCuad[3],currentCuad[1])
		getCuadruplo(-1)
	#Operadores
	if currentCuad[0] == '=':
		memoria.addValue(currentCuad[3],currentCuad[1])
		getCuadruplo(-1)
	if currentCuad[0] == '+':
		operadorUno = currentCuad[1]
		operadorDos = currentCuad[2]
		resultado = operadorUno + operadorDos
		memoria.addValue(currentCuad[3],resultado)
		getCuadruplo(-1)
	if currentCuad[0] == '-':
		operadorUno = currentCuad[1]
		operadorDos = currentCuad[2]
		resultado = operadorUno - operadorDos
		memoria.addValue(currentCuad[3],resultado)
		getCuadruplo(-1)
	if currentCuad[0] == '*':
		operadorUno = currentCuad[1]
		operadorDos = currentCuad[2]
		resultado = operadorUno * operadorDos
		memoria.addValue(currentCuad[3],resultado)
		getCuadruplo(-1)
	if currentCuad[0] == '/':
		operadorUno = currentCuad[1]
		operadorDos = currentCuad[2]
		if operadorDos == 0:
			print("Division by 0")
			sys.exit()
		resultado = operadorUno / operadorDos
		memoria.addValue(currentCuad[3],resultado)
		getCuadruplo(-1)

	#Operadores logicos
	###HAY QUE CHECAR TODAS LAS QUE REGRESAN UN BOOL
	if currentCuad[0] == '==':
		operadorUno = currentCuad[1]
		operadorDos = currentCuad[2]
		if operadorUno == operadorDos:
			resultado = 'true'
		else:
			resultado = 'false'
		memoria.addValue(currentCuad[3],resultado)
		getCuadruplo(-1)
	if currentCuad[0] == 'AND':
		operadorUno = currentCuad[1]
		operadorDos = currentCuad[2]
		if operadorUno and operadorDos:
			resultado = 'true'
		else:
			resultado = 'false'
		memoria.addValue(currentCuad[3],resultado)
		getCuadruplo(-1)
	if currentCuad[0] == 'OR':
		operadorUno = currentCuad[1]
		operadorDos = currentCuad[2]
		if operadorUno or operadorDos:
			resultado = 'true'
		else:
			resultado = 'false'
		memoria.addValue(currentCuad[3],resultado)
		getCuadruplo(-1)

	#Llamadas a funciones definidas por el usuario
	if currentCuad[0] == 'era':
		memAux = Memoria()
		memory.push(memAux)
	if currentCuad[0] == 'endProc':
		memoria = memory.pop()
		getCuadruplo(iLlamadaAFuncion)
	
	if currentCuad[0] == 'return':
		pass

	memory.push(memoria)
	ejecutaCuadruplo()

#Se leen los cuadruplos generados por el compilador y se modifican para que queden como estaban en el compilador
for cuad in compiledFile:
	cuad=cuad.replace('(','')
	cuad=cuad.replace(')','')
	cuad=cuad.replace('\n','')
	cuad=cuad.replace('\'','')
	tupla = tuple(cuad.split(', '))
	cuadruplos.append(tupla)



ejecutaCuadruplo()

