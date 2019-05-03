
import ply.lex as lex
import ply.yacc as yacc
import sys
from DirFunc import *
from CuboSemantico import *
###Declaracion de tokens
tokens = [
    'SEMICOLON',
    'COMMA',
    'PLUS',
    'MINUS',
    'DIVIDE',
    'MULTIPLY',
    'EQUALS',
    'GT',
    'LT',
    'DIFFERENT',
    'LEFTBRACKET',
    'RIGHTBRACKET',
    'LEFTPARENTHESIS',
    'RIGHTPARENTHESIS',
    'CTEI',
    'CTEF',
    'CTES',
    'CTEB',
    'IF',
    'ELSE',
    'PROGRAM',
    'INT',
    'FLOAT',
    'PRINT',
    'ID',
    'HISTOGRAMCHART',
    'FACTORIAL',
    'EXPORTCSV',
    'LINECHART',
    'TRANSPOSE',
    'FUNC',
    'VOID',
    'PIECHART',
    'BARCHART',
    'ARRANGE',
    'GRAPH3D',
    'GLOBALS',
    'STRING',
    'RETURNX',
    'MEDIAN',
    'LINREG',
    'WHILE',
    'POW',
    'STDEV',
    'GTEQ',
    'LTEQ',
    'EQUIVALENTE',
    'BOOL',
    'READ',
    'SQRT',
    'MEAN',
    'MODE',
    'SORT',
    'MAIN',
    'SIN',
    'COS',
    'AND',
    'ABS',
    'NOT',
    'OR' ,
	'LEFTKEY',
	'RIGHTKEY',
	'NEWLINE',
	'COMENTARIO'
]



t_SEMICOLON= r'\;'
t_COMMA= r'\,'
t_PLUS= r'\+'
t_MINUS= r'\-'
t_DIVIDE= r'\/'
t_MULTIPLY= r'\*'


t_DIFFERENT= r'\!\='
t_GTEQ= r'\>\='
t_LTEQ= r'\<\='
t_EQUIVALENTE= r'\=\='

t_EQUALS= r'\='
t_GT= r'\>'
t_LT= r'\<'
t_LEFTBRACKET= r'\['
t_RIGHTBRACKET= r'\]'
t_LEFTKEY= r'\{'
t_RIGHTKEY= r'\}'
t_LEFTPARENTHESIS= r'\('
t_RIGHTPARENTHESIS= r'\)'

###Definicion regex de constantes float###
def t_CTEF (t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t
###Definicion regex de constantes int###
def t_CTEI (t):
    r'\d+'
    t.value = int(t.value)
    return t

###Definicion regex de variables y otros tokens (while, if y funciones especificas del programa) ###
def t_ID (t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value=='if':
        t.type = 'IF'
    elif t.value=='globals':
        t.type='GLOBALS'
    elif t.value=='program':
        t.type='PROGRAM'
    elif t.value=='else':
        t.type='ELSE'
    elif t.value=='int':
        t.type='INT'
    elif t.value=='float':
        t.type='FLOAT'
    elif t.value=='print':
        t.type='PRINT'
    elif t.value=='OR':
        t.type='OR'
    elif t.value=='pieChart':
        t.type='PIECHART'
    elif t.value=='pow':
        t.type='POW'
    elif t.value=='read':
        t.type='READ'
    elif t.value=='return':
        t.type='RETURNX'
    elif t.value=='sin':
        t.type='SIN'
    elif t.value=='sort':
        t.type='SORT'
    elif t.value=='sqrt':
        t.type='SQRT'
    elif t.value=='stdev':
        t.type='STDEV'
    elif t.value=='string':
        t.type='STRING'
    elif t.value=='transpose':
        t.type='TRANSPOSE'
    elif t.value=='true':
        t.type='CTEB'
    elif t.value=='while':
        t.type='WHILE'
    elif t.value=='false':
        t.type='CTEB'
    elif t.value=='bool':
        t.type='BOOL'
    elif t.value=='cos':
        t.type='COS'
    elif t.value=='AND':
        t.type='AND'
    elif t.value=='abs':
        t.type='ABS'
    elif t.value=='mean':
        t.type='MEAN'
    elif t.value=='median':
        t.type='MEDIAN'
    elif t.value=='mode':
        t.type='MODE'
    elif t.value=='factorial':
        t.type='FACTORIAL'
    elif t.value=='linreg':
        t.type='LINREG'
    elif t.value=='func':
        t.type='FUNC'
    elif t.value=='void':
        t.type='VOID'
    elif t.value=='main':
        t.type='MAIN'
    elif t.value=='exportCSV':
        t.type='EXPORTCSV'
    elif t.value=='arrange':
        t.type='ARRANGE'
    elif t.value=='graph3d':
        t.type='GRAPH3D'
    elif t.value=='lineChart':
        t.type='LINECHART'
    elif t.value=='barChart':
        t.type='BARCHART'
    elif t.value=='histogramChart':
        t.type='HISTOGRAMCHART'
    elif t.value=='not':
        t.type='NOT'
    else:
        t.type = 'ID'
    return t

###Definicion regex de constantes tipo string###
def t_CTES (t):
    r'\"[a-zA-Z_ 0-9]+\"'
    t.type = 'CTES'
    return t

###Contador para nuevas lineas en el programa###
def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1
    return t

###Deteccion de comentarios tip "//"###
def t_COMENTARIO(t): 
    r'(\/\/.*)'
    return t

###Deteccion y eliminacion de tabs###
def t_tabulador(t):
    r'\t'
    pass

###Deteccion de caracteres no reconocidos###
def t_error(t):
    print("Caracteres no reconocidos " + str(t.type))
    t.lexer.skip(1)
    sys.exit()
    return

###Eliminacion de espacios en blanco###
t_ignore = r' '

lexer = lex.lex()

###Lectura de tokens para pruebas###
"""
lexer.input('program test; globals bool arrString[2]; func string funcion(string strUno;){ string variable = "HOLA CRAYOLA"; read(arrString[0]); print(strUno); return variable; } main (){ funcion("Porfa jala"); }')

while True:
    tok = lexer.token()
    if not tok:
        break
    print (tok)
"""

# Variable que almacena el nombre de la Funcion a aniadir al directorio de funciones, funcion actual en el programa
nombreFunc = 'globals'
# Variable que almacena el nombre de la variable a aniadir a la funcion especificada.
nombreVar = ''
# Variable que almacena el tipo de Funcion/variable a aniadir
tipoDato = 'void'
# Variable que almacena la cantidad de Filas que tiene la variable especificada
iVarFilas = 0
# Variable que almacena la cantidad de Columnas que tiene la variable especificada
iVarColumnas = 0
# Variable que almacena la cantidad de parametros de una funcion
numeroParametros=0

# Directorio donde se almacenan las funciones y sus variables
dirFunc = DirFunc(nombreFunc,tipoDato)

# Variable que se encarga de manejar el tipo de operaciones que se pueden realizar entre los diferentes tipos de datos validos en rose
semantica = CuboSemantico()

# Pila que almacena las direcciones de memoria de los Operandos
pilaOperando = []

# Pila que almacena los Tipos de los Operandos
pilaTipos = []

# Pila que almacena los Operadores de la expresion
pilaOperadores = []

# Pila que almacena los saltos para los ifs
pilaSaltos = []

# Pila que almacena los saltos a las funciones 
pilaFunciones = []

#Valor que almacen la cantidad de argumentos al llamar a un método.
pilaArgumentos = []

# Vector que almacena los Cuadruplos del programa
arrCuad = []

#Vector que almacena los cuadruplos de constantes
arrCuadTemp=[]

# Valor que apunta al siguiente espacio de memoria disponible
iMemoryAdd = 0

# Valor que apunta al siguiente espacio temporal disponible
iAvail = 1

# Valor que habilita la cantidad de espacios disponibles para cada tipo de dato
espaciosDisponibles = 1000

# Valor que apunta al primer lugar disponible de los int locales
iIntLocales = espaciosDisponibles

# Valor que apunta al primer lugar disponible de los float locales
iFloatLocales = iIntLocales + espaciosDisponibles

# Valor que apunta al primer lugar disponible de los bool locales
iBoolLocales = iFloatLocales + espaciosDisponibles

# Valor que apunta al primer lugar disponible de los strings locales
iStringLocales = iBoolLocales + espaciosDisponibles

# Valor que apunta al primer lugar disponible de los int locales
iIntGlobales = iStringLocales + espaciosDisponibles

# Valor que apunta al primer lugar disponible de los float locales
iFloatGlobales = iIntGlobales + espaciosDisponibles

# Valor que apunta al primer lugar disponible de los bool locales
iBoolGlobales = iFloatGlobales + espaciosDisponibles

# Valor que apunta al primer lugar disponible de los strings locales
iStringGlobales = iBoolGlobales + espaciosDisponibles

# Valor que apunta al primer lugar disponible de los int temporales
iIntTemporales = iStringGlobales + espaciosDisponibles

# Valor que apunta al primer lugar disponible de los float temporales
iFloatTemporales = iIntTemporales + espaciosDisponibles

# Valor que apunta al primer lugar disponible de los bool temporales
iBoolTemporales = iFloatTemporales + espaciosDisponibles

# Valor que apunta al primer lugar disponible de los strings temporales
iStringTemporales = iBoolTemporales + espaciosDisponibles

# Valor que apunta al siguiente lugar disponible de los int
iIntConst = iStringTemporales + espaciosDisponibles

# Valor que apunta al siguiente lugar disponible de los float
iFloatConst = iIntConst + espaciosDisponibles

# Valor que apunta al siguiente lugar disponible de los bool
iBoolConst = iFloatConst + espaciosDisponibles

# Valor que apunta al siguiente lugar disponible de los strings
iStringConst = iBoolConst + espaciosDisponibles

# Dictionary que almacena constantes int
dictInt = {}

# Dictionary que almacena constantes float
dictFloat = {}

# Dictionary que almacena constantes string
dictString = {}

# Contador de las variables temporales int
iContadorIntTemp = iStringGlobales

# Contador de las variables temporales float
iContadorFloatTemp = iIntTemporales

# Contador de las variables temporales bool
iContadorBoolTemp = iFloatTemporales

# Contador de las variables temporales string
iContadorStringTemp = iBoolTemporales

# Lista que almacena los valores actuales de las variables locales
memoriaLocalCantidad = [0, iIntLocales, iFloatLocales, iBoolLocales]

# Lista que almacena los valores actuales de las variables globales
memoriaGlobalCantidad = [iStringLocales, iIntGlobales, iFloatGlobales, iBoolGlobales]

# Lista que almacena los valores actuales de las constantes
memoriaConstantesCantidad = [iStringTemporales, iIntConst, iFloatConst, iBoolConst]

# Valor que almacena el valor de R para guardar arreglos
iR = 1

# Valor que almacen la dirección base del arreglo
dirBase = -1

# Valor que almacena la cantidad de columnas declaradas que han sido proporcionadas
iColumnasDeclaradas = 0

# Valor que almacena la cantidad de filas declaradas que han sido proporcionadas
iFilasDeclaradas = 0

#Valor que almacena la cantidad de columnas de la matriz llamada
iColumnasLlamadas=-1

#Valor que almacena la cantidad de filas en la matriz llamada
iFilasLlamadas=-1

#Booleano que determina si el valor a imprimir es unitario o arreglo/matriz
isArrayOrMatrix = False

#Guarda de manera temporal el valor de una matriz o de un arreglo, según corresponda
tempIdArrMat=[]

# Valor que almacena el nombre del ID
idName = ''

#Almacena la cantidad de constantes hasta el momento
contadorConstantes = 0

#Revisa si se puede o no declarar variables al comienzo del bloque 
declaracionVariables=True

#Revisa si se hizo ya o no un return, también si es posible hacerlo
habilitaReturn=False

#Variable de control para saber si se está realizando o no un return
returnInProcess = False

############################
### FUNCIONES AUXILIARES ###
############################
#Actualiza el primer goto
def solveGoMain():
    global arrCuad
    arrCuad[popSalto()]=('GoTo', '', '' , len(arrCuad))
#Retorna el siguiente espacio de memoria disponible
def getMemAdd():
    global iMemoryAdd
    iMemoryAdd += 1
    return iMemoryAdd
#Guarda el tipo de dato de la variable/funcion actual en la variable global
def setTipoDato(tipo):
    global tipoDato
    tipoDato = tipo
#Guarda el nombre de la funcion en la variable global
def setNombreFunc(name):
    global nombreFunc
    nombreFunc = name
#Guarda el nombre de la variable actual de manera global
def setNombreVar(nameVar):
    global nombreVar
    nombreVar = nameVar
#Guarda el numero de filas
def setIVarFilas(numFil):
    global iVarFilas
    iVarFilas = numFil
#Guarda el numero de columnas
def setIVarColumnas(numCol):
    global iVarColumnas
    iVarColumnas = numCol
#Regresa y actualiza el valor de la memoria local correspondiente
def getMemPosVars(dataType):
    global memoriaLocalCantidad
    memPos = -1
    if dataType == 'int':
        if memoriaLocalCantidad[0] < iIntLocales:
            memPos = memoriaLocalCantidad[0]
            memoriaLocalCantidad[0] += 1
        else:
            memoryOverflow('int local')
    if dataType == 'float':
        if memoriaLocalCantidad[1] < iFloatLocales:
            memPos = memoriaLocalCantidad[1]
            memoriaLocalCantidad[1] += 1
        else:
            memoryOverflow('float local')
    if dataType == 'bool':
        if memoriaLocalCantidad[2] < iBoolLocales:
            memPos = memoriaLocalCantidad[2]
            memoriaLocalCantidad[2] += 1
        else:
            memoryOverflow('bool local')
    if dataType == 'string':
        if memoriaLocalCantidad[3] < iStringLocales:
            memPos = memoriaLocalCantidad[3]
            memoriaLocalCantidad[3] += 1
        else:
            memoryOverflow('string local')
    return memPos

#Regresa y actualiza el valor de la memoria local correspondiente
def getMemPosGlobals(dataType):
    global memoriaGlobalCantidad
    memPos = -1
    ###if dataType == getTopTipos():
    if dataType == 'int':
        if memoriaGlobalCantidad[0] < iIntGlobales:
	        memPos = memoriaGlobalCantidad[0]
	        memoriaGlobalCantidad[0] += 1
        else:
            memoryOverflow('int global')
    if dataType == 'float':
        if memoriaGlobalCantidad[1] < iFloatGlobales:
            memPos = memoriaGlobalCantidad[1]
            memoriaGlobalCantidad[1] += 1
        else:
            memoryOverflow('float global')
    if dataType == 'bool':
	    if memoriaGlobalCantidad[2] < iBoolGlobales:
	        memPos = memoriaGlobalCantidad[2]
	        memoriaGlobalCantidad[2] += 1
	    else:
	        memoryOverflow('bool global')
    if dataType == 'string':
        if memoriaGlobalCantidad[3] < iStringGlobales:
            memPos = memoriaGlobalCantidad[3]
            memoriaGlobalCantidad[3] += 1
        else:
            memoryOverflow('string global')
    return memPos
#Guarda la variable actual en el directorio de variables de la funcion especificada
def anadirVar():
    global nombreFunc
    global nombreVar
    global tipoDato
    global iVarFilas
    global iVarColumnas
    if nombreFunc == 'globals':
    	posMemoria = getMemPosGlobals(tipoDato)
    else:
    	posMemoria = getMemPosVars(tipoDato)
    addOperandoToStack(posMemoria)
    addTipoToStack(tipoDato)
    dirFunc.addVariable(nombreFunc, nombreVar, tipoDato, iVarFilas, iVarColumnas, posMemoria)
#Modifica el apuntador de memoria con base al tipo de dato que es el arreglo y la cantidad especificada
def actualizaApuntadorMemoria(dataType, cantidadValores):
    global memoriaGlobalCantidad
    global memoriaLocalCantidad
    if nombreFunc == 'globals':
        if dataType == 'int':
            memoriaGlobalCantidad[0] += cantidadValores
            if memoriaGlobalCantidad[0] > iIntGlobales:
                memoryOverflow('int global')
        if dataType == 'float':
            memoriaGlobalCantidad[1] += cantidadValores
            if memoriaGlobalCantidad[1] > iFloatGlobales:
                memoryOverflow('float global')
        if dataType == 'bool':
            memoriaGlobalCantidad[2] += cantidadValores
            if memoriaGlobalCantidad[2] > iBoolGlobales:
                memoryOverflow('bool global')
        if dataType == 'string':
            memoriaGlobalCantidad[3] += cantidadValores
            if memoriaGlobalCantidad[3] > iStringGlobales:
                memoryOverflow('string global')
    else:
        if dataType == 'int':
            memoriaLocalCantidad[0] += cantidadValores
            if memoriaLocalCantidad[0] > iIntLocales:
                memoryOverflow('int local')
        if dataType == 'float':
            memoriaLocalCantidad[1] += cantidadValores
            if memoriaLocalCantidad[1] > iFloatLocales:
                memoryOverflow('float local')
        if dataType == 'bool':
            memoriaLocalCantidad[2] += cantidadValores
            if memoriaLocalCantidad[2] > iBoolLocales:
                memoryOverflow('bool local')
        if dataType == 'string':
            memoriaLocalCantidad[3] += cantidadValores
            if memoriaLocalCantidad[3] > iStringLocales:
                memoryOverflow('string local')


#Guarda la cantidad de parametros en la funcion
def aniadirParametros():
    global nombreFunc
    global numeroParametros
    dirFunc.updateParams(nombreFunc, numeroParametros)
#Guarda la funcion actual en el directorio de funciones
def anadirFunc():
    global nombreFunc
    global tipoDato
    global arrCuad
    dirFunc.addFunc(nombreFunc, tipoDato, len(arrCuad))
#Funcion que imprime el error al alcanzar el limite de memoria
def memoryOverflow(description):
    print("In line {}, {} has reached its memory limit.".format(lexer.lineno, description))
    sys.exit()
    return
#Regresa el temporal siguiente disponible
def getAvail(tipoDato):
    global iContadorIntTemp
    global iContadorFloatTemp
    global iContadorBoolTemp
    global iContadorStringTemp
    avail = -1
    if tipoDato == 'int':
        if iContadorIntTemp < iIntTemporales:
            avail = iContadorIntTemp
            iContadorIntTemp = iContadorIntTemp + 1
        else:
            memoryOverflow('int temporal')
    if tipoDato == 'float':
        if iContadorFloatTemp < iFloatTemporales:
            avail = iContadorFloatTemp
            iContadorFloatTemp+=1
        else:
            memoryOverflow('float temporal')
    if tipoDato == 'bool':
        if iContadorBoolTemp < iBoolTemporales:
            avail = iContadorBoolTemp
            iContadorBoolTemp+=1
        else:
            memoryOverflow('bool temporal')
    if tipoDato == 'string':
        if iContadorStringTemp < iStringTemporales:
            avail = iContadorStringTemp
            iContadorStringTemp+=1
        else:
            memoryOverflow('string temporal')
    return avail
#Guarda el cuadruplo especificado al arreglo de cuarduplos
def addQuad(operador, operandoUno, operandoDos, valorGuardar):
	global arrCuad
	tupla = (operador, operandoUno, operandoDos, valorGuardar)
	arrCuad.append(tupla)
	return getMemAdd()
def addQuadInicio(operador, operandoUno, operandoDos, valorGuardar):
    global arrCuadTemp
    tupla = (operador, operandoUno, operandoDos, valorGuardar)
    arrCuadTemp.append(tupla)
#Agrega el id especificado a la pila de operandos y a su tipo a la pila de tipos
def addIdToStack(nameId):
    global idName
    global nombreFunc
    global pilaOperando
    global pilaTipos
    idName = nameId
    if (idName in dirFunc.val[nombreFunc][1] or idName in dirFunc.val['globals'][1]):
        try:
            tipoTemp = dirFunc.val[nombreFunc][1][idName][0]      #Se da prioridad a buscar la variable en la funciones
            idName = dirFunc.val[nombreFunc][1][idName][3]
        except:
            tipoTemp = dirFunc.val['globals'][1][idName][0]       #Si no, se busca de manera global
            idName = dirFunc.val['globals'][1][idName][3]
        addOperandoToStack(idName)
        addTipoToStack(tipoTemp)
    else:
        print("In line {}, variable {} not declared.".format( lexer.lineno, idName))
        sys.exit()
        return
#Agrega el operando a la pila de operandos y su tipo a la pila de tipos 
def addValueToStack(value):
    global dictInt
    global dictFloat
    global dictString
    global memoriaConstantesCantidad
    global contadorConstantes
    #print(value)
    #print(type(value))
    #print(tipoDato)
    if type(value) == int:
        if value not in dictInt:
            if memoriaConstantesCantidad[0] < iIntConst:
                dictInt[value]=memoriaConstantesCantidad[0]
                memoriaConstantesCantidad[0] += 1
                addQuadInicio('addConstInt', value, '', dictInt[value])
                contadorConstantes += 1
            else:
                memoryOverflow('int const') 
        addOperandoToStack(dictInt[value])
        addTipoToStack('int')
    if type(value) == float:
        if value not in dictFloat:
            if memoriaConstantesCantidad[1] < iFloatConst:
                dictFloat[value]=memoriaConstantesCantidad[1]
                memoriaConstantesCantidad[1] += 1
                addQuadInicio('addConstFloat', value, '', dictFloat[value])
                contadorConstantes += 1
            else:
                memoryOverflow('float const')  
        addOperandoToStack(dictFloat[value])
        addTipoToStack('float')
    if type(value) == str:
        if (value == 'true' or value == 'false'):
            if(value=='true'):
                addOperandoToStack(iFloatConst+1)
            else:
                addOperandoToStack(iFloatConst)
            addTipoToStack('bool')
        else:
            if value not in dictString:
                if memoriaConstantesCantidad[3] < iStringConst:
                    dictString[value]=memoriaConstantesCantidad[3]
                    memoriaConstantesCantidad[3] += 1
                    addQuadInicio('addConstString', value, '', dictString[value])
                    contadorConstantes += 1
                else:
                    memoryOverflow('string const') 
            addOperandoToStack(dictString[value])
            addTipoToStack('string')
#Agrega el operador a la pila de operadores
def addOperadorToStack(operator):
	global pilaOperadores
	pilaOperadores.append(operator)
#Regresa el top de la pila de operadores
def getTopOperator():
    global pilaOperadores
    pilaSize = len(pilaOperadores)
    lastIndex = pilaSize-1
    if(lastIndex<0):
        return 'vacio'
    return pilaOperadores[lastIndex]
#Agrega el operador a la pila de operadores
def addOperandoToStack(operando):
    global pilaOperando
    pilaOperando.append(operando)
#Agrega el nuevo salto a la pila
def addSaltoToStack(salto):
    global pilaSaltos
    pilaSaltos.append(salto)
#Agrega el tipo a la pila de tipos
def addTipoToStack(tipoResult):
	global pilaTipos
	pilaTipos.append(tipoResult)
#Saca el top de la pila de operandos
def popOperando():
	global pilaOperando
	return pilaOperando.pop()
#Saca el top de la pila de operadores
def popOperadores():
	global pilaOperadores
	return pilaOperadores.pop()
#Saca en top de la pila de saltos
def popSalto():
    global pilaSaltos
    return pilaSaltos.pop()
#Saca el top de la pila de tipos
def popTipos():
	global pilaTipos
	return pilaTipos.pop()
#Muestra el top de la pila de tipos
def getTopTipos():
	global pilaTipos
	pilaSize = len(pilaTipos)
	lastIndex = pilaSize-1
	if(lastIndex<0):
		return 'vacio'
	return pilaTipos[lastIndex]
#Se hace la creacion del cuadruplo para la operacion aritmetica
def arithmeticOperator():
    rightOperand = popOperando()
    rightType = popTipos()
    checkIfTemporal(rightOperand)
    leftOperand = popOperando()
    leftType = popTipos()
    checkIfTemporal(leftOperand)
    tempOperator = popOperadores()
    resultType = semantica.resultType(leftType, rightType, tempOperator)
    if resultType != 'error':
        result = getAvail(resultType)
        addQuad(tempOperator, leftOperand, rightOperand, result)
        addOperandoToStack(result)
        addTipoToStack(resultType)
        ##Regresar el temp al AVAIL
    else:
        typeMismatch()
#Se hace la creacion del cuadruplo para la operacion de asignacion
def assignOperator():
	rightOperand = popOperando()
	rightType = popTipos()
	checkIfTemporal(rightOperand)
	leftOperand = popOperando()
	leftType = popTipos()    
	checkIfTemporal(leftOperand)
	tempOperator = popOperadores()
	resultType = semantica.resultType(leftType, rightType, tempOperator)
	if resultType != 'error':
		addQuad(tempOperator, rightOperand, '', leftOperand)
		##Regresar el temp al AVAIL
	else:
		typeMismatch()
#Creacion del cuadruplo de print
def printFun():
	global isArrayOrMatrix
	printOperand=popOperando()
	typeOperand=popTipos()
	checkIfTemporal(printOperand)
	tempOperator = popOperadores()
	resultType = semantica.resultType(tempOperator, typeOperand, '')
	if resultType != 'error':
		#arrMat = ''
		#if isArrayOrMatrix:
		arrMat = 'arr'
		addQuad(tempOperator, printOperand, arrMat, '')
	else:
		typeMismatch()
	isArrayOrMatrix = False
#Creacion del cuadruplo de print
def readFunc():
    readOperand=popOperando()
    typeOperand=popTipos()
    checkIfTemporal(readOperand)
    tempOperator = popOperadores()
    resultType = semantica.resultType(tempOperator, typeOperand, '')
    if resultType != 'error':
        addQuad(tempOperator, readOperand, '', readOperand)
        addOperandoToStack(readOperand)
        addTipoToStack(resultType)
        ##Regresar el temp al AVAIL
    else:
        typeMismatch()
#Función que genera el cuádruplo para la funcíon not()
def notFunc():
    notOperand = popOperando()
    typeOperand = popTipos()
    tempOperator = popOperadores()
    resultType = semantica.resultType(tempOperator, typeOperand, '')
    if resultType != 'error':
        result = getAvail(typeOperand)
        addQuad(tempOperator, notOperand, '', result)
        addOperandoToStack(result)
        addTipoToStack(resultType)
        ##Regresar el temp al AVAIL
    else:
        typeMismatch()
#Funcion que imprime el error de type missmatch
def typeMismatch():
    print("In line {}, type mismatch".format(lexer.lineno))
    sys.exit()
    return
#Función que elimina el páréntesis que esté en el top de la pila
def delParentesis():
    tempOperator = popOperadores()
    if  '('!= tempOperator and '['!=tempOperator:
        print("In line {}, unexpected token )".format(lexer.lineno))
        sys.exit()
        return

def durante1():
    global arrCuad
    addSaltoToStack(len(arrCuad))

def durante2():
    global arrCuad
    bResultado = popTipos()
    if bResultado == 'bool':
        operand = popOperando()
        checkIfTemporal(operand)
        addQuad('GoToF', operand, '', '')
        addSaltoToStack(len(arrCuad)-1)
    else:
        typeMismatch()

def durante3():
    global arrCuad
    falso = popSalto()
    retorno = popSalto()
    addQuad('GoTo', '','',retorno)
    tupla=(arrCuad[falso][0], arrCuad[falso][1],arrCuad[falso][2], len(arrCuad))
    arrCuad[falso]=tupla

def condicion1():
    bResultado = popTipos()
    if bResultado == 'bool':
        valor = popOperando()
        checkIfTemporal(valor)
        addQuad('GoToF', valor, '', '')
        addSaltoToStack(len(arrCuad)-1)
    else:
        typeMismatch()

def condicion2():
    global arrCuad
    addQuad('GoTo', '', '', '')
    falso = popSalto()
    addSaltoToStack(len(arrCuad)-1)
    tupla = (arrCuad[falso][0], arrCuad[falso][1], arrCuad[falso][2], len(arrCuad))
    arrCuad[falso] = tupla

def condicion3():
    global arrCuad
    end = popSalto()
    tupla = (arrCuad[end][0], arrCuad[end][1], arrCuad[end][2], len(arrCuad))
    arrCuad[end] = tupla

#Genera el cuádruplo para la asignación de los arreglos
def assignArray():
	global dirBase
	global iColumnasDeclaradas
	global iFilasDeclaradas
	rightOperand = popOperando()
	rightType = popTipos()
	checkIfTemporal(rightOperand)
	leftOperand = dirBase + (iVarColumnas*iFilasDeclaradas + iColumnasDeclaradas)
	leftType = popTipos()
	tempOperator = popOperadores()
	resultType = semantica.resultType(leftType, rightType, tempOperator)
	if resultType != 'error':
		addQuad(tempOperator, rightOperand, '', leftOperand)
		##Regresar el temp al AVAIL
	else:
		typeMismatch()

#Regresa la funcion que se debe usar en base a los operadores dados
def switchOperator(arg):
	switcher = {
		1: arithmeticOperator,
		2: assignOperator,
        3: readFunc,
        4: printFun,
        5: delParentesis,
        6: notFunc,
        7: assignArray
	}
	return switcher.get(arg)
#Determina el tipo de operador con el que se trabajara la operacion
def operacionesEnPilasId(operators, tipoFunc):
	if (getTopOperator() in operators):
		func = switchOperator(tipoFunc)
		func()
#Determina que tipo de funcion es la que se debe de ejecutar
def switchFuncion(arg):
    switcher = {
        1: durante1,
        2: durante2,
        3: durante3,
        4: condicion1,
        5: condicion2,
        6: condicion3
    }
    return switcher.get(arg)
#Manda ejecutar la funcion correspondiente en los brincos
def operacionesEnPilasBrincos(tipoFunc):
    func = switchFuncion(tipoFunc)
    func()
#Se valida si se libera o no el espacio usado por el temporal
def checkIfTemporal(memPos):
    global iContadorIntTemp
    global iContadorFloatTemp
    global iContadorBoolTemp
    global iContadorStringTemp
    global returnInProcess
    
    if not returnInProcess:
        if (memPos >= iStringGlobales and memPos < iIntTemporales):
            iContadorIntTemp -= 1
        if (memPos >= iIntTemporales and memPos < iFloatTemporales):
            iContadorFloatTemp -= 1
        if (memPos >= iFloatTemporales and memPos < iBoolTemporales):
            iContadorBoolTemp -= 1
        if (memPos >= iBoolTemporales and memPos < iStringTemporales):
            iContadorStringTemp -= 1
    else:
        pass


#################
### GRAMATICA ###
#################
def p_rose(p):
    '''
    rose : comments_nl PROGRAM comments_nl ID comments_nl SEMICOLON comments_nl roseauxvars np_agregar_goto_main roseauxfunc main
    '''
    file = open("codeobj.rs","w+")
    print(dirFunc.val)
    print(arrCuad)
    for cuad in arrCuad:
    	file.write(str(cuad) + "\n")
    file.close()
    print("Exito compilando")

def p_roseauxvars(p):
    '''
    roseauxvars : GLOBALS comments_nl vars roseauxvars comments_nl
            | empty
    '''

def p_roseauxfunc(p):
    '''
    roseauxfunc : np_habilitar_variables func roseauxfunc comments_nl
                | empty
    '''
def p_main(p):
    '''
    main : np_habilitar_variables MAIN np_main_func comments_nl LEFTPARENTHESIS comments_nl RIGHTPARENTHESIS comments_nl bloque np_end
    '''

def p_vars(p):
    '''
    vars : tipo ID np_obtener_nombre_var comments_nl LEFTBRACKET comments_nl CTEI np_obtener_columnas comments_nl RIGHTBRACKET comments_nl LEFTBRACKET comments_nl CTEI np_obtener_filas comments_nl RIGHTBRACKET comments_nl np_anadir_variable EQUALS np_asignacion_arreglo_quad1 comments_nl LEFTKEY comments_nl asignacionmatriz RIGHTKEY np_asignacion_matrix_quad2 comments_nl SEMICOLON np_calcular_k_matrix comments_nl
        | tipo ID np_obtener_nombre_var comments_nl LEFTBRACKET comments_nl CTEI np_obtener_columnas comments_nl RIGHTBRACKET comments_nl LEFTBRACKET comments_nl CTEI np_obtener_filas comments_nl RIGHTBRACKET comments_nl SEMICOLON np_anadir_variable np_calcular_k_matrix comments_nl
        | tipo ID np_obtener_nombre_var comments_nl LEFTBRACKET comments_nl CTEI np_obtener_columnas comments_nl RIGHTBRACKET comments_nl np_asignar_arreglo EQUALS np_asignacion_arreglo_quad1 comments_nl LEFTKEY comments_nl asignacionarreglo RIGHTKEY comments_nl SEMICOLON np_asignacion_arreglo_quad4 np_calcular_k_arreglo comments_nl
        | tipo ID np_obtener_nombre_var comments_nl LEFTBRACKET comments_nl CTEI np_obtener_columnas comments_nl RIGHTBRACKET comments_nl SEMICOLON np_asignar_arreglo np_calcular_k_arreglo comments_nl
        | tipo ID np_obtener_nombre_var np_asignar_fil_col np_asignacion_inicial_quad1 comments_nl EQUALS np_asignacion_quad2 comments_nl ctes SEMICOLON np_asignacion_quad4 comments_nl 
        | tipo ID np_obtener_nombre_var comments_nl SEMICOLON np_asignar_fil_col comments_nl
    '''	

def p_asignacionmatriz(p):
    '''
    asignacionmatriz : LEFTKEY comments_nl asignacionarreglo RIGHTKEY np_asignacion_matrix_quad1 comments_nl COMMA comments_nl asignacionmatriz comments_nl
                    | LEFTKEY comments_nl asignacionarreglo RIGHTKEY comments_nl
    '''

def p_asignacionarreglo(p):
    '''
    asignacionarreglo : ctes np_asignacion_arreglo_quad2 COMMA np_asignacion_arreglo_quad3 comments_nl asignacionarreglo comments_nl
                    | ctes np_asignacion_arreglo_quad2
    '''

def p_tipo(p):
    '''
    tipo : INT np_obtener_tipo comments_nl
        | FLOAT np_obtener_tipo comments_nl
        | STRING np_obtener_tipo comments_nl
        | BOOL np_obtener_tipo comments_nl
    '''

def p_durante(p):
    '''
    durante : WHILE np_durante_quad1 comments_nl LEFTPARENTHESIS comments_nl mega_exp RIGHTPARENTHESIS np_durante_quad2 comments_nl bloque np_durante_quad3
    '''

def p_condition(p):
    '''
    condition : IF comments_nl LEFTPARENTHESIS comments_nl mega_exp np_condition_quad1 RIGHTPARENTHESIS comments_nl bloque np_condition_quad2 else np_condition_quad3
    '''

def p_else(p):
    '''
    else : ELSE comments_nl bloque
        | empty
    '''

def p_mega_exp(p):
    '''
    mega_exp : expression_compare np_mega_exp_quad2 comments_nl mega_expaux
    '''

def p_mega_expaux(p):
    '''
    mega_expaux : OR np_mega_exp_quad1 mega_exp comments_nl
                | AND np_mega_exp_quad1 mega_exp comments_nl
                | empty
    '''

def p_expression_compare(p):
    '''
    expression_compare : exp DIFFERENT np_expression_compare_quad1 comments_nl exp np_expression_compare_quad2
                    | exp GTEQ np_expression_compare_quad1 comments_nl exp np_expression_compare_quad2
                    | exp LTEQ np_expression_compare_quad1 comments_nl exp np_expression_compare_quad2
                    | exp EQUIVALENTE np_expression_compare_quad1 comments_nl exp np_expression_compare_quad2
                    | exp GT np_expression_compare_quad1 comments_nl exp np_expression_compare_quad2
                    | exp LT np_expression_compare_quad1 comments_nl exp np_expression_compare_quad2
                    | exp np_expression_compare_quad2
    '''

def p_exp(p):
    '''
    exp : termino np_expaux_quad4 expaux comments_nl
    '''


def p_expaux(p):
    '''
    expaux : PLUS np_expaux_quad3 comments_nl exp
            | MINUS np_expaux_quad3 comments_nl exp
            | empty 
    '''

def p_termino(p):
    '''
    termino : factor np_terminoaux_quad5 terminoaux
    '''

def p_terminoaux(p):
    '''
    terminoaux : DIVIDE np_terminoaux_quad2 termino comments_nl
                | MULTIPLY np_terminoaux_quad2 termino comments_nl
                | empty
    '''

def p_factor(p):
    '''
    factor : vars_cte comments_nl
            | LEFTPARENTHESIS np_parentesis_quad1 comments_nl mega_exp comments_nl RIGHTPARENTHESIS np_parentesis_quad2 comments_nl
    '''

def p_func(p):
    '''
    func : FUNC comments_nl np_inicializar_parametros VOID np_obtener_tipo comments_nl restofuncion comments_nl
        | FUNC comments_nl np_inicializar_parametros tipo restofuncion comments_nl
    '''

def p_restofuncion(p):
    '''
    restofuncion : ID np_obtener_nombre_func comments_nl LEFTPARENTHESIS comments_nl argumentos comments_nl RIGHTPARENTHESIS np_agregar_parametros2 comments_nl bloque np_check_return2 np_endproc
    '''	

def p_argumentos(p):
    '''
    argumentos : tipo mismotipo comments_nl SEMICOLON comments_nl argumentos comments_nl
                | empty
    '''

def p_mismotipo(p):
    '''
    mismotipo : ID np_obtener_nombre_var np_agregar_parametros comments_nl LEFTBRACKET comments_nl CTEI np_obtener_columnas comments_nl RIGHTBRACKET comments_nl LEFTBRACKET comments_nl CTEI np_obtener_filas comments_nl RIGHTBRACKET comments_nl COMMA np_anadir_variable np_calcular_k_matrix comments_nl mismotipo comments_nl
                | ID np_obtener_nombre_var np_agregar_parametros comments_nl LEFTBRACKET comments_nl CTEI np_obtener_columnas comments_nl RIGHTBRACKET comments_nl COMMA np_asignar_arreglo np_calcular_k_arreglo comments_nl mismotipo comments_nl
                | ID np_obtener_nombre_var np_agregar_parametros comments_nl COMMA np_asignar_fil_col comments_nl mismotipo comments_nl
                | ID np_obtener_nombre_var np_agregar_parametros comments_nl LEFTBRACKET comments_nl CTEI np_obtener_columnas comments_nl RIGHTBRACKET comments_nl LEFTBRACKET comments_nl CTEI np_obtener_filas comments_nl RIGHTBRACKET comments_nl np_anadir_variable
                | ID np_obtener_nombre_var np_agregar_parametros comments_nl LEFTBRACKET comments_nl CTEI np_obtener_columnas comments_nl RIGHTBRACKET comments_nl np_asignar_arreglo
                | ID np_obtener_nombre_var np_agregar_parametros comments_nl np_asignar_fil_col
    '''

def p_bloque(p):
    '''
    bloque : LEFTKEY comments_nl estatuto RIGHTKEY comments_nl
    '''

def p_estatuto(p):
    '''
    estatuto : declaracionvariables np_flag_variables comments_nl aplicaciones comments_nl
    '''

def p_declaracionvariables(p):
    '''
    declaracionvariables : np_verificar_variables vars declaracionvariables comments_nl
                        | empty
    '''
def p_aplicaciones(p):
    '''
    aplicaciones : condition comments_nl aplicaciones comments_nl
                | escritura comments_nl aplicaciones comments_nl
                | lectura comments_nl aplicaciones comments_nl
                | llama_spec_func comments_nl aplicaciones comments_nl
                | asignacion comments_nl aplicaciones comments_nl
                | durante comments_nl aplicaciones comments_nl
                | llama_func aplicaciones comments_nl
                | returnx np_check_return np_cuadruplo_retorno np_endproc comments_nl aplicaciones comments_nl 
                | empty
    '''

def p_vars_cte(p):
    '''
    vars_cte : spec_func
            | ID np_factor_quad2 comments_nl LEFTBRACKET np_parentesis_quad1 comments_nl mega_exp np_valor_columnas RIGHTBRACKET np_parentesis_quad2 comments_nl LEFTBRACKET np_parentesis_quad1 comments_nl mega_exp np_valor_filas RIGHTBRACKET np_parentesis_quad2 np_factor_quad3 comments_nl
            | ID np_factor_quad2 comments_nl LEFTBRACKET np_parentesis_quad1 comments_nl mega_exp np_valor_columnas RIGHTBRACKET np_parentesis_quad2 np_factor_quad4 comments_nl
            | ID np_crea_era comments_nl LEFTPARENTHESIS comments_nl params RIGHTPARENTHESIS np_genera_gosub comments_nl
            | ID np_factor_quad1 comments_nl
            | ctes
    '''

def p_params(p):
    '''
    params : paramsaux
            | empty
    '''
def p_paramsaux(p):
    '''
    paramsaux : mega_exp COMMA np_add_parametro comments_nl paramsaux comments_nl
                | mega_exp np_add_parametro
    '''

def p_asignacion(p):
    '''
    asignacion : ID np_factor_quad2 comments_nl LEFTBRACKET np_parentesis_quad1 comments_nl mega_exp np_valor_columnas RIGHTBRACKET np_parentesis_quad2 comments_nl LEFTBRACKET np_parentesis_quad1 comments_nl mega_exp np_valor_filas RIGHTBRACKET np_parentesis_quad2 np_solo_asignar_matrix_quad1 comments_nl EQUALS np_asignacion_de_arreglo_quad1 comments_nl mega_exp SEMICOLON np_asignacion_quad4 comments_nl
               | ID np_factor_quad2 comments_nl LEFTBRACKET np_parentesis_quad1 comments_nl mega_exp np_valor_columnas RIGHTBRACKET np_parentesis_quad2 comments_nl EQUALS np_asignacion_de_arreglo_quad1 np_solo_asignar_arreglo_quad1 comments_nl mega_exp SEMICOLON np_asignacion_quad4 comments_nl
               | ID np_asignacion_quad1 comments_nl EQUALS np_asignacion_quad2 comments_nl mega_exp SEMICOLON np_asignacion_quad4 comments_nl
    '''	

def p_escritura(p):
    '''
    escritura : PRINT np_print_quad1 comments_nl LEFTPARENTHESIS comments_nl mega_exp RIGHTPARENTHESIS comments_nl SEMICOLON np_print_quad2 comments_nl
    '''

def p_lectura1(p):
    '''
    lectura : READ np_read_quad1 comments_nl LEFTPARENTHESIS comments_nl ID np_read_quad3 lectura2 comments_nl RIGHTPARENTHESIS comments_nl SEMICOLON np_read_quad2 comments_nl
    '''

def p_lectura2(p):
	'''
	lectura2 : LEFTBRACKET np_parentesis_quad1 np_read_arr_quad2 comments_nl mega_exp np_valor_columnas RIGHTBRACKET np_parentesis_quad2 comments_nl LEFTBRACKET np_parentesis_quad1 comments_nl mega_exp np_valor_filas RIGHTBRACKET np_parentesis_quad2 np_solo_asignar_matrix_quad1 comments_nl 
			| LEFTBRACKET np_parentesis_quad1 np_read_arr_quad2 comments_nl mega_exp np_valor_columnas RIGHTBRACKET np_parentesis_quad2 np_solo_asignar_arreglo_quad1 comments_nl
			| empty
	'''



def p_llama_spec_func(p):
    '''
    llama_spec_func : spec_func SEMICOLON comments_nl
    '''

def p_spec_func(p):
    '''
    spec_func : SQRT comments_nl LEFTPARENTHESIS comments_nl mega_exp RIGHTPARENTHESIS comments_nl 
                | POW comments_nl LEFTPARENTHESIS comments_nl mega_exp COMMA comments_nl mega_exp RIGHTPARENTHESIS comments_nl 
                | ABS comments_nl LEFTPARENTHESIS comments_nl mega_exp RIGHTPARENTHESIS comments_nl 
                | STDEV comments_nl LEFTPARENTHESIS comments_nl mega_exp RIGHTPARENTHESIS comments_nl 
                | MEAN comments_nl LEFTPARENTHESIS comments_nl mega_exp RIGHTPARENTHESIS comments_nl 
                | MEDIAN comments_nl LEFTPARENTHESIS comments_nl mega_exp RIGHTPARENTHESIS comments_nl 
                | MODE comments_nl LEFTPARENTHESIS comments_nl mega_exp RIGHTPARENTHESIS comments_nl 
                | FACTORIAL comments_nl LEFTPARENTHESIS comments_nl mega_exp RIGHTPARENTHESIS comments_nl 
                | SORT comments_nl LEFTPARENTHESIS comments_nl mega_exp RIGHTPARENTHESIS comments_nl 
                | SIN comments_nl LEFTPARENTHESIS comments_nl mega_exp RIGHTPARENTHESIS comments_nl 
                | COS comments_nl LEFTPARENTHESIS comments_nl mega_exp RIGHTPARENTHESIS comments_nl 
                | TRANSPOSE comments_nl LEFTPARENTHESIS comments_nl mega_exp RIGHTPARENTHESIS comments_nl 
                | EXPORTCSV comments_nl LEFTPARENTHESIS comments_nl mega_exp COMMA comments_nl mega_exp RIGHTPARENTHESIS comments_nl 
                | ARRANGE comments_nl LEFTPARENTHESIS comments_nl mega_exp COMMA comments_nl mega_exp COMMA comments_nl mega_exp RIGHTPARENTHESIS comments_nl 
                | GRAPH3D comments_nl LEFTPARENTHESIS comments_nl mega_exp COMMA comments_nl mega_exp COMMA comments_nl mega_exp RIGHTPARENTHESIS comments_nl 
                | PIECHART comments_nl LEFTPARENTHESIS comments_nl mega_exp RIGHTPARENTHESIS comments_nl
                | HISTOGRAMCHART comments_nl LEFTPARENTHESIS comments_nl mega_exp COMMA comments_nl mega_exp RIGHTPARENTHESIS comments_nl
                | LINECHART comments_nl LEFTPARENTHESIS comments_nl mega_exp COMMA comments_nl mega_exp RIGHTPARENTHESIS comments_nl
                | BARCHART comments_nl LEFTPARENTHESIS comments_nl mega_exp COMMA comments_nl mega_exp RIGHTPARENTHESIS comments_nl
                | LINREG comments_nl LEFTPARENTHESIS comments_nl mega_exp COMMA comments_nl mega_exp RIGHTPARENTHESIS comments_nl
                | NOT np_not_quad1 comments_nl LEFTPARENTHESIS comments_nl mega_exp RIGHTPARENTHESIS np_not_quad2 comments_nl
    '''

def p_returnx(p):
    '''
    returnx : RETURNX comments_nl mega_exp SEMICOLON comments_nl
    '''
    

def p_ctes(p):
    '''
    ctes : floatPostNeg comments_nl
        | intPostNeg comments_nl
        | CTES np_ctes_quad1 comments_nl
        | CTEB np_ctes_quad1 comments_nl
    '''	

def p_intPostNeg(p):
    '''
    intPostNeg : MINUS CTEI np_ctes_quad2
                | CTEI np_ctes_quad1
    '''

def p_floatPostNeg(p):
    '''
    floatPostNeg : MINUS CTEF np_ctes_quad2
                | CTEF np_ctes_quad1
    '''

def p_llama_func(p):
    '''
    llama_func : ID np_crea_era2 comments_nl LEFTPARENTHESIS comments_nl params RIGHTPARENTHESIS np_genera_gosub2 comments_nl SEMICOLON comments_nl
    '''

def p_comments_nl(p):
	'''
	comments_nl : NEWLINE comments_nl
				| COMENTARIO comments_nl
				| empty
	'''
"""
def p_comentarioaux(p):
    '''
    comentarioaux 	: NEWLINE comentarioaux comments_nl
    				| empty
        
    '''
"""
def p_empty(p):
	'''
    empty :
    ''' 

def p_error(p):
    print ("Syntax error in line " + str(lexer.lineno))
    tok = lexer.token()
    print("lo que truena es el: " + str(tok))
    sys.exit()
    return


def p_np_obtener_tipo(p):

    '''
    np_obtener_tipo : empty
    '''
    dataType = str(p[-1])
    setTipoDato(dataType)
    
def p_np_obtener_nombre_func(p):
    '''
    np_obtener_nombre_func : empty
    '''
    funName = str(p[-1])
    setNombreFunc(funName)
    anadirFunc()

def p_np_obtener_nombre_var(p):
    '''
    np_obtener_nombre_var : empty
    '''
    varName = str(p[-1])
    setNombreVar(varName)

def p_np_agregar_parametros(p):
    '''
    np_agregar_parametros : empty
    '''
    global numeroParametros
    numeroParametros+=1

def p_np_inicializar_parametros(p):
    '''
    np_inicializar_parametros : empty
    '''
    global numeroParametros
    numeroParametros=0

def p_np_agregar_parametros2(p):
    '''
    np_agregar_parametros2 : empty
    '''
    aniadirParametros()

def p_np_obtener_filas(p):
    '''
    np_obtener_filas : empty
    '''
    global iR
    numFilas = int(p[-1])
    if numFilas > 0:
        iR = (numFilas) * iR
        setIVarFilas(numFilas)
    else:
        print("In line {}, invalid index.".format(lexer.lineno))
        sys.exit()
        return

def p_np_obtener_columnas(p):
    '''
    np_obtener_columnas : empty
    '''
    global iR
    numCol = int(p[-1])
    if numCol > 0:
        iR = (numCol) * iR
        setIVarColumnas(numCol)
    else:
        print("In line {}, negative index.".format(lexer.lineno))
        sys.exit()
        return


def p_np_anadir_variable(p):
	'''
	np_anadir_variable : empty
	'''
	anadirVar()

def p_np_asignar_fil_col(p):
    '''
    np_asignar_fil_col : empty
    '''
    setIVarFilas(0)
    setIVarColumnas(0)
    anadirVar()

def p_np_asignar_arreglo(p):
	'''
	np_asignar_arreglo : empty
	'''
	setIVarFilas(0)
	anadirVar()

def p_np_main_func(p):
    '''
    np_main_func : empty
    '''
    funName = str(p[-1])
    setNombreFunc(funName)
    setTipoDato('void')
    anadirFunc()
    solveGoMain()

def p_np_factor_quad1(p):
    '''
    np_factor_quad1 : 
    '''
    tempIdName = str(p[-1])
    if tempIdName in dirFunc.val[nombreFunc][1]:
        if dirFunc.getColumnasVar(nombreFunc,tempIdName)!=0:
            print("In line {}, expected [".format(lexer.lineno))
            sys.exit()
            return
    elif tempIdName in dirFunc.val['globals'][1]:
        if dirFunc.getColumnasVar('globals',tempIdName)!=0:
            print("In line {}, expected [".format(lexer.lineno))
            sys.exit()
            return
    addIdToStack(tempIdName)

def p_np_factor_quad2(p):
    '''
    np_factor_quad2 :
    '''
    global tempIdArrMat
    global isArrayOrMatrix
    isArrayOrMatrix = True
    tempIdArrMat.append(str(p[-1]))

def p_np_factor_quad3(p):
    '''
    np_factor_quad3 :
    '''
    global tempIdArrMat
    global nombreFunc
    global iColumnasLlamadas
    global iFilasLlamadas
    global dirFunc
    idName = tempIdArrMat.pop()
    if (idName in dirFunc.val[nombreFunc][1] or idName in dirFunc.val['globals'][1]):
        if idName in dirFunc.val[nombreFunc][1]:
            tipoTemp = dirFunc.val[nombreFunc][1][idName][0]      #Se da prioridad a buscar la variable en la funciones
            if dirFunc.getFilasVar(nombreFunc,idName)==0:           #Verificar el llamado a filas
                if iFilasLlamadas>=0:
                    print("In line {}, unexpected matrix call".format(lexer.lineno))
                    sys.exit()
                    return
            addQuad('ver',dirFunc.getFilasVar(nombreFunc,idName), dirFunc.getVarMemPos(nombreFunc, idName), iFilasLlamadas)
            if dirFunc.getColumnasVar(nombreFunc,idName)==0:            #Verificar el llamado a columas
                if iColumnasLlamadas>=0:
                    print("In line {}, unexpected array call".format(lexer.lineno))
                    sys.exit()
                    return
            addQuad('ver', dirFunc.getColumnasVar(nombreFunc, idName),dirFunc.getVarMemPos(nombreFunc, idName), iColumnasLlamadas)
            temporalSiguiente2=getAvail('int')
            temporalSiguiente=getAvail(tipoTemp)
            addQuad("**", iColumnasLlamadas, dirFunc.getColumnasVar(nombreFunc, idName), temporalSiguiente2)
            addQuad("+", temporalSiguiente2, iFilasLlamadas, temporalSiguiente2)
            addQuad("+*", temporalSiguiente2, dirFunc.getVarMemPos(nombreFunc,idName),temporalSiguiente)
            addOperandoToStack(temporalSiguiente)
        else:
            tipoTemp = dirFunc.val['globals'][1][idName][0]       #Si no, se busca de manera global
            if dirFunc.getFilasVar('globals',idName)==0:           #Verificar el llamado a filas
                if iFilasLlamadas>=0:
                    print("In line {}, unexpected matrix call".format(lexer.lineno))
                    sys.exit()
                    return
            addQuad('ver',dirFunc.getFilasVar('globals',idName), dirFunc.getVarMemPos('globals', idName), iFilasLlamadas)
            if dirFunc.getColumnasVar('globals',idName)==0:            #Verificar el llamado a columas
                if iColumnasLlamadas>=0:
                    print("In line {}, unexpected array call".format(lexer.lineno))
                    sys.exit()
                    return
            addQuad('ver', dirFunc.getColumnasVar('globals', idName), dirFunc.getVarMemPos('globals', idName), iColumnasLlamadas)
            temporalSiguiente2=getAvail('int')
            temporalSiguiente=getAvail(tipoTemp)
            addQuad("**", iColumnasLlamadas, dirFunc.getColumnasVar('globals', idName), temporalSiguiente2)
            addQuad("+", temporalSiguiente2, iFilasLlamadas, temporalSiguiente2)
            addQuad("+*", temporalSiguiente2, dirFunc.getVarMemPos('globals',idName),temporalSiguiente)
            addOperandoToStack(temporalSiguiente)
        addTipoToStack(tipoTemp)
        checkIfTemporal(iColumnasLlamadas)
        checkIfTemporal(iFilasLlamadas)
        iFilasLlamadas=-1
        iColumnasLlamadas=-1
    else:
        print("In line {}, variable {} not declared.".format( lexer.lineno, idName))
        sys.exit()
        return


def p_np_factor_quad4(p):
    '''
    np_factor_quad4 : 
    '''
    global tempIdArrMat
    global nombreFunc
    global iColumnasLlamadas
    global iFilasLlamadas
    global dirFunc
    idName = tempIdArrMat.pop()
    if (idName in dirFunc.val[nombreFunc][1] or idName in dirFunc.val['globals'][1]):
        if idName in dirFunc.val[nombreFunc][1]:
            tipoTemp = dirFunc.val[nombreFunc][1][idName][0]      #Se da prioridad a buscar la variable en la funciones
            if dirFunc.getFilasVar(nombreFunc,idName)>0:           #Verificar el llamado a filas
                if iFilasLlamadas<0:
                    print("In line {}, unexpected array call".format(lexer.lineno))
                    sys.exit()
                    return
            if dirFunc.getColumnasVar(nombreFunc,idName)==0:            #Verificar el llamado a columas
                if iColumnasLlamadas>=0:
                    print("In line {}, unexpected array call".format(lexer.lineno))
                    sys.exit()
                    return
            addQuad('ver', dirFunc.getColumnasVar(nombreFunc, idName),dirFunc.getVarMemPos(nombreFunc, idName), iColumnasLlamadas)
            temporalSiguiente=getAvail(tipoTemp)
            addQuad("+*", iColumnasLlamadas, dirFunc.getVarMemPos(nombreFunc, idName), temporalSiguiente)
            addOperandoToStack(temporalSiguiente)
        else:
            tipoTemp = dirFunc.val['globals'][1][idName][0]       #Si no, se busca de manera global
            if dirFunc.getFilasVar('globals',idName)>0:           #Verificar el llamado a filas
                if iFilasLlamadas<0:
                    print("In line {}, unexpected matrix call".format(lexer.lineno))
                    sys.exit()
                    return
            if dirFunc.getColumnasVar('globals',idName)==0:            #Verificar el llamado a columas
                if iColumnasLlamadas>=0:
                    print("In line {}, unexpected array call".format(lexer.lineno))
                    sys.exit()
                    return
            addQuad('ver', dirFunc.getColumnasVar('globals', idName),dirFunc.getVarMemPos('globals', idName), iColumnasLlamadas)
            temporalSiguiente=getAvail(tipoTemp)
            addQuad("+*", iColumnasLlamadas, dirFunc.getVarMemPos('globals', idName), temporalSiguiente)
            addOperandoToStack(temporalSiguiente)
        addTipoToStack(tipoTemp)
        checkIfTemporal(iColumnasLlamadas)
        iFilasLlamadas=-1
        iColumnasLlamadas=-1
        
    else:
        print("In line {}, variable {} not declared.".format( lexer.lineno, idName))
        sys.exit()
        return

def p_np_valor_columnas(p):
    '''
    np_valor_columnas :
    '''
    global iColumnasLlamadas
    global iFilasLlamadas
    columnas=popOperando()
    tipo=popTipos()
    if tipo!='int':
        print("In line {} expected int, instead {}.".format( lexer.lineno, tipo))
        sys.exit()
        return
    else:
        iColumnasLlamadas=columnas
        iFilasLlamadas=-1

def p_np_valor_filas(p):
    '''
    np_valor_filas :
    '''
    global iFilasLlamadas
    filas = popOperando()
    tipo=popTipos()
    if tipo!='int':
        print("In line {} expected int, instead {}.".format( lexer.lineno, tipo))
    else:
        iFilasLlamadas=filas

def p_np_asignacion_inicial_quad1(p):
    '''
    np_asignacion_inicial_quad1 : empty
    '''
    global nombreVar
    addIdToStack(nombreVar)

def p_np_asignacion_quad1(p):
	'''
	np_asignacion_quad1 : 
	'''
	tempIdName = str(p[-1])
	addIdToStack(tempIdName)

def p_np_ctes_quad1(p):
	'''
	np_ctes_quad1 : empty
	'''
	#print(getTopTipos())
	tempIdName = p[-1]
	addValueToStack(tempIdName)

def p_np_ctes_quad2(p):
	'''
	np_ctes_quad2 : empty
	'''
	tempIdName = p[-1]
	addValueToStack(tempIdName*-1)


def p_np_terminoaux_quad2(p):
	'''
	np_terminoaux_quad2 : empty
	'''
	tempOperator = str(p[-1])
	addOperadorToStack(tempOperator)

def p_np_asignacion_quad2(p):
	'''
	np_asignacion_quad2 : empty
	'''
	tempOperator = str(p[-1])
	addOperadorToStack(tempOperator)


def p_np_expaux_quad3(p):
	'''
	np_expaux_quad3 : empty
	'''
	tempOperator = str(p[-1])
	addOperadorToStack(tempOperator)

def p_np_expaux_quad4(p):
    '''
    np_expaux_quad4 : empty
    '''
    tuplaOperadores = ('+','-')
    operacionesEnPilasId(tuplaOperadores, 1)

def p_np_asignacion_quad4(p):
	'''
	np_asignacion_quad4 : empty
	'''
	tuplaOperadores = ('=','=*')
	operacionesEnPilasId(tuplaOperadores, 2)

def p_np_terminoaux_quad5(p):
	'''
	np_terminoaux_quad5 : empty
	'''
	tuplaOperadores = ('*','/')
	operacionesEnPilasId(tuplaOperadores, 1)

def p_np_expression_compare_quad1(p):
    '''
    np_expression_compare_quad1 : empty
    '''
    tempOperator = str(p[-1])
    addOperadorToStack(tempOperator)

def p_np_expression_compare_quad2(p):
    '''
    np_expression_compare_quad2 : empty
    '''
    tuplaOperadores=('>','<','!=','<=','>=','==')
    operacionesEnPilasId(tuplaOperadores,1)

def p_np_mega_exp_quad1(p):
    '''
    np_mega_exp_quad1 : empty
    '''
    tempOperator = str(p[-1])
    addOperadorToStack(tempOperator)

def p_np_mega_exp_quad2(p):
    '''
    np_mega_exp_quad2 : empty
    '''
    tuplaOperadores=('OR', 'AND')
    operacionesEnPilasId(tuplaOperadores,1)

def p_np_print_quad1(p):
    '''
    np_print_quad1 : empty
    '''
    tempOperator = str(p[-1])
    addOperadorToStack(tempOperator)

def p_np_print_quad2(p):
    '''
    np_print_quad2 : empty
    '''
    tuplaOperadores=('print')
    operacionesEnPilasId(tuplaOperadores,4)


def p_np_read_arr_quad2(p):
	'''
	np_read_arr_quad2 : 
	'''
	global tempIdArrMat
	global isArrayOrMatrix
	global nombreFunc
	global pilaTipos
	isArrayOrMatrix = True
	popOperadores()
	addOperadorToStack('read*')
	memAdd = popOperando()
	nombreDeVar = dirFunc.getVarName(nombreFunc,memAdd)
	tempIdArrMat.append(nombreDeVar)
	

def p_np_read_quad1(p):
    '''
    np_read_quad1 : empty
    '''
    tempOperator = str(p[-1])
    addOperadorToStack(tempOperator)

def p_np_read_quad2(p):
    '''
    np_read_quad2 : empty
    '''
    tuplaOperadores=('read','read*')
    operacionesEnPilasId(tuplaOperadores,3)

def p_np_read_quad3(p):
    '''
    np_read_quad3 : empty
    '''
    tempIdName = str(p[-1])
    addIdToStack(tempIdName)

def p_np_not_quad1(p):
    '''
    np_not_quad1 : 
    '''
    temporal = p[-1]
    addOperadorToStack(temporal)

def p_np_not_quad2(p):
    '''
    np_not_quad2 : 
    '''
    tuplaOperadores = ('not')
    operacionesEnPilasId(tuplaOperadores,6)


def p_np_parentesis_quad1(p):
    '''
    np_parentesis_quad1 : 
    '''
    tempOperator = str(p[-1])
    addOperadorToStack(tempOperator)

def p_np_parentesis_quad2(p):
    '''
    np_parentesis_quad2 : 
    '''
    tuplaOperadores=('(','[')
    operacionesEnPilasId(tuplaOperadores,5)

def p_np_durante_quad1(p):
    '''
    np_durante_quad1 : empty
    '''
    operacionesEnPilasBrincos(1)


def p_np_durante_quad2(p):
    '''
    np_durante_quad2 : empty
    '''
    operacionesEnPilasBrincos(2)

def p_np_durante_quad3(p):
    '''
    np_durante_quad3 : empty
    '''
    operacionesEnPilasBrincos(3)

def p_np_condition_quad1(p):
	'''
	np_condition_quad1 : empty
	'''
	operacionesEnPilasBrincos(4)

def p_np_condition_quad2(p):
	'''
	np_condition_quad2 : empty
	'''
	operacionesEnPilasBrincos(5)

def p_np_condition_quad3(p):
	'''
	np_condition_quad3 : empty
	'''
	operacionesEnPilasBrincos(6)

def p_np_agregar_goto_main(p):
    '''
    np_agregar_goto_main : empty
    '''
    addQuad('GoTo','','','')
    addSaltoToStack(len(arrCuad)-1)
    
def p_np_cuadruplo_retorno(p):
    '''
    np_cuadruplo_retorno : empty
    '''
    operand=popOperando()
    tipo=popTipos()
    checkIfTemporal(operand)
    if(dirFunc.val[nombreFunc][0]==tipo):
        addQuad('return','','',operand)
    else:
        print("In line {} expected return value: {}, instead {}.".format( lexer.lineno, dirFunc.val[nombreFunc][0], tipo))
        sys.exit()
        return

def p_np_endproc(p):
    '''
    np_endproc : empty
    '''
    global memoriaLocalCantidad
    memoriaLocalCantidad = [0, iIntLocales, iFloatLocales, iBoolLocales]
    addQuad('endproc','','','')

    
def p_np_crea_era(p):
    '''
    np_crea_era : empty
    '''
    global pilaArgumentos
    global pilaFunciones
    global returnInProcess
    
    nameFunc = p[-1]
    if nameFunc in dirFunc.val:
        valueFunc = dirFunc.val[nameFunc][0]
        result = getAvail(valueFunc)
        addOperandoToStack(result)
        addTipoToStack(dirFunc.val[nameFunc][0])
        pilaFunciones.append(nameFunc)
        addQuad('era', nameFunc, '', '')
        pilaArgumentos.append(0)
    else:
        print("In line {}, function {} not previously declared.".format( lexer.lineno, nameFunc))
        sys.exit()
        return
    returnInProcess = True
    

def p_np_add_parametro(p):
    '''
    np_add_parametro : empty
    '''
    global pilaArgumentos
    argumentoValor = popOperando()
    tipoArgumento = popTipos()
    checkIfTemporal(argumentoValor)
    nameFunc = pilaFunciones.pop()
    iArgumentos = pilaArgumentos.pop() + 1
    pilaArgumentos.append(iArgumentos)
    paramName = 'param' + str(iArgumentos)
    iArgumentosDeFunc = dirFunc.val[nameFunc][2]
    listaDirFunc = list(dirFunc.val[nameFunc][1].values()) 
    if iArgumentosDeFunc >= iArgumentos:
        if listaDirFunc[iArgumentos-1][0] == tipoArgumento:
            addQuad('parameter', argumentoValor, '', paramName)
        else:
            print("In line {}, argument {} type mismatch with function declaration.".format( lexer.lineno, nameFunc))
            sys.exit()
            return
    else:
        print("In line {}, argument count in function {} does not match.".format( lexer.lineno, nameFunc))
        sys.exit()
        return
    pilaFunciones.append(nameFunc)
	
def p_np_genera_gosub(p):
    '''
    np_genera_gosub : empty
    '''
    global pilaArgumentos
    global pilaFunciones
    global returnInProcess
    
    returnInProcess = False
    operando=popOperando()
    iArgumentos = pilaArgumentos.pop()
    checkIfTemporal(operando)
    nameFunc = pilaFunciones.pop()
    if iArgumentos == dirFunc.val[nameFunc][2]:
        addQuad('gosub', nameFunc, len(arrCuad)+1, dirFunc.val[nameFunc][3])
        addQuad('=',nameFunc,'',operando)
        addOperandoToStack(operando)
    else:
        print("In line {}, argument count in function {} does not match.".format( lexer.lineno, nameFunc))
        sys.exit()
        return

    
    
def p_np_genera_gosub2(p):
    '''
    np_genera_gosub2 : empty
    '''
    global pilaArgumentos
    global pilaFunciones
    iArgumentos = pilaArgumentos.pop()
    nameFunc = pilaFunciones.pop()
    if iArgumentos == dirFunc.val[nameFunc][2]:
        addQuad('gosub', nameFunc, len(arrCuad)+1, dirFunc.val[nameFunc][3])
    else:
        print("In line {}, argument count in function {} does not match.".format( lexer.lineno, nameFunc))
        sys.exit()
        return

def p_np_crea_era2(p):
    '''
    np_crea_era2 : 
    '''
    global pilaArgumentos
    global pilaFunciones
    nameFunc = p[-1]
    if nameFunc in dirFunc.val:
        pilaFunciones.append(nameFunc)
        addQuad('era', nameFunc, '', '')
        pilaArgumentos.append(0)
    else:
        print("In line {}, function {} not previously declared.".format( lexer.lineno, nameFunc))
        sys.exit()
        return

def p_np_end(p):
    '''
    np_end : empty
    '''
    global arrCuad
    global arrCuadTemp
    lengthConst=len(arrCuadTemp)+1
    offset=('offset', lengthConst, '','')
    arrCuadTemp.insert(0,offset)
    addQuad('end','','','')
    arrCuadTemp.extend(arrCuad)
    arrCuad=arrCuadTemp

def p_np_calcular_k_arreglo(p):
    '''
    np_calcular_k_arreglo : 
    '''
    global dirFunc
    global nombreVar
    global nombreFunc
    global iR
    mDim = iR-1
    iR=1
    typeTemp = dirFunc.getVarType(nombreFunc, nombreVar)
    actualizaApuntadorMemoria(typeTemp, mDim)
    
def p_np_calcular_k_matrix(p):
    '''
    np_calcular_k_matrix : 
    '''
    global dirFunc
    global nombreVar
    global iR
    global nombreFunc
    mDim = iR-1
    iR=1
    typeTemp = dirFunc.getVarType(nombreFunc, nombreVar)
    actualizaApuntadorMemoria(typeTemp, mDim)

def p_np_asignacion_arreglo_quad1(p):
	'''
	np_asignacion_arreglo_quad1 : 
	'''
	global dirBase
	global nombreFunc
	global nombreVar
	dirBase = dirFunc.getVarMemPos(nombreFunc, nombreVar)
	tempOperator = '='
	addOperadorToStack(tempOperator)

def p_np_asignacion_arreglo_quad2(p):
	'''
	np_asignacion_arreglo_quad2 : 
	'''
	tuplaOperadores = ('=')
	operacionesEnPilasId(tuplaOperadores, 7)

def p_np_asignacion_arreglo_quad3(p):
    '''
    np_asignacion_arreglo_quad3 : empty
    '''
    global iVarColumnas
    global iColumnasDeclaradas
    global tipoDato
    if iColumnasDeclaradas < iVarColumnas-1:
        tempOperator = '='
        addOperadorToStack(tempOperator)
        iColumnasDeclaradas += 1
        addTipoToStack(tipoDato)
    else:
        print("In line {}, number of arguments provided doesn't match the amount specified.".format(lexer.lineno))
        sys.exit()	
        return

def p_np_asignacion_arreglo_quad4(p):
    '''
    np_asignacion_arreglo_quad4 :
    '''	
    global iColumnasDeclaradas
    global iVarColumnas
    if iColumnasDeclaradas != iVarColumnas-1:
        print("In line {}, number of arguments provided doesn't match the amount specified.".format(lexer.lineno))
        sys.exit()
        return
    else:
        iColumnasDeclaradas = 0

def p_np_asignacion_matrix_quad1(p):
    '''
    np_asignacion_matrix_quad1 : 
    '''
    global iFilasDeclaradas
    global iColumnasDeclaradas
    global iVarFilas
    if iFilasDeclaradas < iVarFilas-1:
        tempOperator = '='
        addOperadorToStack(tempOperator)
        iFilasDeclaradas += 1
        iColumnasDeclaradas = 0
        addTipoToStack(tipoDato)
    else:
        print("In line {}, number of arguments provided doesn't match the amount specified.".format(lexer.lineno))
        sys.exit()
        return

def p_np_asignacion_matrix_quad2(p):
    '''
    np_asignacion_matrix_quad2 : 
    '''
    global iFilasDeclaradas
    global iVarFilas
    if iFilasDeclaradas != iVarFilas-1:
        print("In line {}, number of arguments provided doesn't match the amount specified.".format(lexer.lineno))
        sys.exit()
        return
    else:
        iFilasDeclaradas = 0

def p_np_solo_asignar_matrix_quad1(p):
    '''
    np_solo_asignar_matrix_quad1 : 
    '''
    global tempIdArrMat
    global nombreFunc
    global iColumnasLlamadas
    global iFilasLlamadas
    global dirFunc
    idName = tempIdArrMat.pop()
    if (idName in dirFunc.val[nombreFunc][1] or idName in dirFunc.val['globals'][1]):
        if idName in dirFunc.val[nombreFunc][1]:
            tipoTemp = dirFunc.val[nombreFunc][1][idName][0]      #Se da prioridad a buscar la variable en la funciones
            if dirFunc.getFilasVar(nombreFunc,idName)==0:           #Verificar el llamado a filas
                if iFilasLlamadas>=0:
                    print("In line {}, unexpected matrix call".format(lexer.lineno))
                    sys.exit()
                    return
            addQuad('ver',dirFunc.getFilasVar(nombreFunc,idName), dirFunc.getVarMemPos(nombreFunc, idName), iFilasLlamadas)
            if dirFunc.getColumnasVar(nombreFunc,idName)==0:            #Verificar el llamado a columas
                if iColumnasLlamadas>=0:
                    print("In line {}, unexpected array call".format(lexer.lineno))
                    sys.exit()
                    return
            addQuad('ver', dirFunc.getColumnasVar(nombreFunc, idName),dirFunc.getVarMemPos(nombreFunc, idName), iColumnasLlamadas)
            temporalSiguiente = getAvail('int')
            temporalSiguiente2=getAvail('int')
            
            addQuad("**", iColumnasLlamadas, dirFunc.getColumnasVar(nombreFunc, idName), temporalSiguiente2)
            addQuad("+", temporalSiguiente2, iFilasLlamadas, temporalSiguiente2)
            addQuad("+**", temporalSiguiente2, dirFunc.getVarMemPos(nombreFunc,idName),temporalSiguiente)

            addOperandoToStack(temporalSiguiente)
        else:
            tipoTemp = dirFunc.val['globals'][1][idName][0]       #Si no, se busca de manera global
            if dirFunc.getFilasVar('globals',idName)==0:           #Verificar el llamado a filas
                if iFilasLlamadas>=0:
                    print("In line {}, unexpected matrix call".format(lexer.lineno))
                    sys.exit()
                    return
            addQuad('ver',dirFunc.getFilasVar('globals',idName), dirFunc.getVarMemPos('globals', idName), iFilasLlamadas)
            if dirFunc.getColumnasVar('globals',idName)==0:            #Verificar el llamado a columas
                if iColumnasLlamadas>=0:
                    print("In line {}, unexpected array call".format(lexer.lineno))
                    sys.exit()
                    return
            addQuad('ver', dirFunc.getColumnasVar('globals', idName),dirFunc.getVarMemPos('globals', idName), iColumnasLlamadas)
            temporalSiguiente = getAvail('int')
            temporalSiguiente2=getAvail('int')
            
            addQuad("**", iColumnasLlamadas, dirFunc.getColumnasVar('globals', idName), temporalSiguiente2)
            addQuad("+", temporalSiguiente2, iFilasLlamadas, temporalSiguiente2)
            addQuad("+**", temporalSiguiente2, dirFunc.getVarMemPos('globals',idName),temporalSiguiente)

            addOperandoToStack(temporalSiguiente)
        addTipoToStack(tipoTemp)
        checkIfTemporal(iColumnasLlamadas)
        checkIfTemporal(iFilasLlamadas)
        iFilasLlamadas=-1
        iColumnasLlamadas=-1
    else:
        print("In line {}, variable {} not declared.".format( lexer.lineno, idName))
        sys.exit()
        return

def p_np_solo_asignar_arreglo_quad1(p):
    '''
    np_solo_asignar_arreglo_quad1 : 
    '''
    global tempIdArrMat
    global nombreFunc
    global iColumnasLlamadas
    global iFilasLlamadas
    global dirFunc
    idName = tempIdArrMat.pop()
    if (idName in dirFunc.val[nombreFunc][1] or idName in dirFunc.val['globals'][1]):
        if idName in dirFunc.val[nombreFunc][1]:
            tipoTemp = dirFunc.val[nombreFunc][1][idName][0]      #Se da prioridad a buscar la variable en la funciones
            if dirFunc.getFilasVar(nombreFunc,idName)>0:           #Verificar el llamado a filas
                if iFilasLlamadas<0:
                    print("In line {}, unexpected array call".format(lexer.lineno))
                    sys.exit()
                    return
            if dirFunc.getColumnasVar(nombreFunc,idName)==0:            #Verificar el llamado a columas
                if iColumnasLlamadas>=0:
                    print("In line {}, unexpected array call".format(lexer.lineno))
                    sys.exit()
                    return
            addQuad('ver', dirFunc.getColumnasVar(nombreFunc, idName),dirFunc.getVarMemPos(nombreFunc, idName), iColumnasLlamadas)
            temporalSiguiente=getAvail('int')
            addQuad("+**", iColumnasLlamadas, dirFunc.getVarMemPos(nombreFunc, idName), temporalSiguiente)
            addOperandoToStack(temporalSiguiente)
        else:
            tipoTemp = dirFunc.val['globals'][1][idName][0]       #Si no, se busca de manera global
            if dirFunc.getFilasVar('globals',idName)>0:           #Verificar el llamado a filas
                if iFilasLlamadas<0:
                    print("In line {}, unexpected matrix call".format(lexer.lineno))
                    sys.exit()
                    return
            if dirFunc.getColumnasVar('globals',idName)==0:            #Verificar el llamado a columas
                if iColumnasLlamadas>=0:
                    print("In line {}, unexpected array call".format(lexer.lineno))
                    sys.exit()
                    return
            addQuad('ver', dirFunc.getColumnasVar('globals', idName),dirFunc.getVarMemPos('globals', idName), iColumnasLlamadas)
            temporalSiguiente=getAvail('int')
            addQuad("+**", iColumnasLlamadas, dirFunc.getVarMemPos('globals', idName), temporalSiguiente)
            addOperandoToStack(temporalSiguiente)
        checkIfTemporal(iColumnasLlamadas)
        iFilasLlamadas=-1
        iColumnasLlamadas=-1
        addTipoToStack(tipoTemp)

def p_np_asignacion_de_arreglo_quad1(p):
	'''
	np_asignacion_de_arreglo_quad1 : 
	'''
	addOperadorToStack('=*')

def p_np_flag_variables(p):
    '''
    np_flag_variables :
    '''
    global declaracionVariables
    declaracionVariables=False

def p_np_habilitar_variables(p):
    '''
    np_habilitar_variables : 
    '''
    global declaracionVariables
    declaracionVariables=True

def p_np_verificar_variables(p):
    '''
    np_verificar_variables :
    '''
    global declaracionVariables
    if not declaracionVariables:
        print("In line {}, unexpected variable declaration.".format(lexer.lineno))
        sys.exit()
        return

def p_np_check_return(p):
    '''
    np_check_return :
    '''
    global nombreFunc
    global habilitaReturn
    if dirFunc.getFuncType(nombreFunc)=='void':
        print("In line {}, unexpected return in void function.".format(lexer.lineno))
        sys.exit()
        return
    else:
        habilitaReturn=True

def p_np_check_return2(p):
    '''
    np_check_return2 :
    '''
    if dirFunc.getFuncType(nombreFunc)!='void':
        if not habilitaReturn:
            print("In line {}, return statment missing.".format(lexer.lineno))
            sys.exit()
            return

parser = yacc.yacc() 

#Cambiar el nombre del archivo de entrada para probar el codigo
#name='pruebaRose.txt'
#name='pruebaCuad3.txt'
name='fibonacci.txt'

with open(name, 'r') as myfile:
    s=myfile.read()
print(name)
parser.parse(s)


""""

while True:
    try:
        s=input('')
    except EOFError:
        break
    parser.parse(s) 
"""
