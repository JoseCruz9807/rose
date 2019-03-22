
import ply.lex as lex
import ply.yacc as yacc
import sys
from DirFunc import *
from CuboSemantico import *

tokens = [
    'COLON',
    'SEMICOLON',
    'PERIOD',
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
    'VAR',
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
    'APPEND',
    'WHILE',
    'POW',
    'GRAPH',
    'STDEV',
    'MULTICOMOP',
    'MULTICOMCL',
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
    'TAN',
    'ABS',
    'QUOTE',
    'NOT',
    'OR' ,
	'LEFTKEY',
	'RIGHTKEY',
	'NEWLINE',
	'COMENTARIO'
]

#MultiCommentOpen
t_MULTICOMOP= r'\/\*'
#MultiCommentClose
t_MULTICOMCL= r'\*\/'


t_COLON= r'\:'
t_SEMICOLON= r'\;'
t_PERIOD= r'\.'
t_COMMA= r'\,'
t_PLUS= r'\+'
t_MINUS= r'\-'
t_DIVIDE= r'\/'
t_MULTIPLY= r'\*'
t_QUOTE= r'\"'

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

def t_CTEF (t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_CTEI (t):
    r'\d+'
    t.value = int(t.value)
    return t

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
    elif t.value=='tan':
        t.type='TAN'
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
    elif t.value=='graph':
        t.type='GRAPH'
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
    elif t.value=='append':
        t.type='APPEND'
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

def t_CTES (t):
    r'\"[a-zA-Z_ 0-9]+\"'
    t.type = 'CTES'
    return t

def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1
    return t

def t_COMENTARIO(t): 
    r'(\/\/.*)'
    return t

def t_tabulador(t):
    r'\t'
    pass

def t_error(t):
    print("Caracteres no reconocidos " + str(t.type))
    t.lexer.skip(1)

t_ignore = r' '

lexer = lex.lex()

"""
lexer.input('program test; globals int arbol = 3; main (){ int arbol; arbol = arbol-3; if(arbol>6){print(arbol);}else{ print(arbol);};}')

while True:
    tok = lexer.token()
    if not tok:
        break
    print (tok)
"""

# Variable que almacena el nombre de la Función a añadir al directorio de funciones.
nombreFunc = 'globals'
# Variable que almacena el nombre de la variable a añadir a la función especificada.
nombreVar = ''
# Variable que almacena el tipo de Función/variable a añadir
tipoDato = 'void'
# Variable que almacena la cantidad de Filas que tiene la variable especificada
iVarFilas = 0
# Variable que almacena la cantidad de Columnas que tiene la variable especificada
iVarColumnas = 0

# Directorio donde se almacenan las funciones y sus variables
dirFunc = DirFunc(nombreFunc,tipoDato)

# Variable que se encarga de manejar el tipo de operaciones que se pueden realizar entre los diferentes tipos de datos válidos en rose
semantica = CuboSemantico()

# Pila que almacena las direcciones de memoria de los Operandos
pilaOperando = []

# Pila que almacena los Tipos de los Operandos
pilaTipos = []

# Pila que almacena los Operadores de la expresión
pilaOperadores = []

# Vector que almacena los Cuadruplos del programa
arrCuad = []

# Valor que apunta al siguiente espacio de memoria disponible
iMemoryAdd = 0;

# Valor que apunta al siguiente espacio temporal disponible
iAvail = 1;

# Valor que almacena el nombre del ID
idName = ''


############################
### FUNCIONES AUXILIARES ###
############################
def getMemAdd():
    global iMemoryAdd
    iMemoryAdd += 1
    return iMemoryAdd

def setTipoDato(tipo):
    global tipoDato
    tipoDato = tipo

def setNombreFunc(name):
    global nombreFunc
    nombreFunc = name

def setNombreVar(nameVar):
    global nombreVar
    nombreVar = nameVar

def setIVarFilas(numFil):
    global iVarFilas
    iVarFilas = numFil

def setIVarColumnas(numCol):
    global iVarColumnas
    iVarColumnas = numCol

def anadirVar():
    global nombreFunc
    global nombreVar
    global tipoDato
    global iVarFilas
    global iVarColumnas
    dirFunc.addVariable(nombreFunc, nombreVar, tipoDato, iVarFilas, iVarColumnas)

def anadirFunc():
    global nombreFunc
    global tipoDato
    dirFunc.addFunc(nombreFunc, tipoDato)

def getAvail():
	global iAvail
	iAvail += 1
	strAvail = 'temp' + str(iAvail-1)
	return strAvail


def addQuad(operador, operandoUno, operandoDos, valorGuardar):
	global arrCuad
	tupla = (operador, operandoUno, operandoDos, valorGuardar)
	arrCuad.append(tupla)
	return getMemAdd()

def addIdToStack(nameId):
	global idName
	global nombreFunc
	global pilaOperando
	global pilaTipos
	idName = nameId
		
	if (idName in dirFunc.val[nombreFunc][1] or idName in dirFunc.val['globals'][1]):
		tipoTemp = dirFunc.val[nombreFunc][1][idName][0]
		addOperandoToStack(idName)
		addTipoToStack(tipoTemp)
	else:
		print("In line {}, variable {} not declared.".format( lexer.lineno, idName))
		sys.exit()

def addOperadorToStack(operator):
	global pilaOperadores
	pilaOperadores.append(operator)

def getTopOperator():
	global pilaOperadores
	pilaSize = len(pilaOperadores)
	lastIndex = pilaSize-1
	return pilaOperadores[lastIndex]

def addOperandoToStack(operando):
	global pilaOperando
	pilaOperando.append(operando)

def addTipoToStack(tipoResult):
	global pilaTipos
	pilaTipos.append(tipoResult)

def popOperando():
	global pilaOperando
	return pilaOperando.pop()

def popOperadores():
	global pilaOperadores
	return pilaOperadores.pop()

def popTipos():
	global pilaTipos
	return pilaTipos.pop()

def arithmeticOperator():
	
	print("arithmeticOp")

	

	rightOperand = popOperando()
	rightType = popTipos()
	leftOperand = popOperando()
	leftType = popTipos()
	tempOperator = popOperadores()
	resultType = semantica.resultType(leftType, rightType, tempOperator)

	if resultType != 'error':
		result = getAvail()
		addQuad(tempOperator, leftOperand, rightOperand, result)
		addOperandoToStack(result)
		addTipoToStack(resultType)
		##Regresar el temp al AVAIL
	else:
		print("In line {}, type mismatch".format(lexer.lineno))
		sys.exit()


def assignOperator():

	print("assignOp")

	rightOperand = popOperando()
	rightType = popTipos()
	leftOperand = popOperando()
	leftType = popTipos()
	tempOperator = popOperadores()
	resultType = semantica.resultType(leftType, rightType, tempOperator)

	if resultType != 'error':
		#result = getAvail()
		addQuad(tempOperator, rightOperand, '', leftOperand)
		##Regresar el temp al AVAIL
	else:
		print("In line {}, type mismatch".format(lexer.lineno))
		sys.exit()


def switchOperator(arg):
	switcher = {
		1: arithmeticOperator,
		2: assignOperator
	}
	return switcher.get(arg)


def operacionesEnPilasId(operators, tipoFunc):
	if (getTopOperator() in operators):
		func = switchOperator(tipoFunc)
		func()

#################
### GRAMÁTICA ###
#################
def p_rose(p):
    '''
    rose : comments_nl PROGRAM comments_nl ID comments_nl SEMICOLON comments_nl roseauxvars comments_nl roseauxfunc comments_nl main comments_nl
    '''
    print(arrCuad)
    print("Éxito compilando")

def p_roseauxvars(p):
    '''
    roseauxvars : GLOBALS comments_nl vars comments_nl roseauxvars comments_nl
            | empty
    '''

def p_roseauxfunc(p):
    '''
    roseauxfunc : func comments_nl roseauxfunc comments_nl
                | empty
    '''
def p_main(p):
    '''
    main : MAIN np_main_func comments_nl LEFTPARENTHESIS comments_nl RIGHTPARENTHESIS comments_nl bloque comments_nl
    '''

def p_vars(p):
    '''
    vars : tipo comments_nl ID np_obtener_nombre_var comments_nl LEFTBRACKET comments_nl CTEI np_obtener_filas comments_nl RIGHTBRACKET comments_nl LEFTBRACKET comments_nl CTEI np_obtener_columnas comments_nl RIGHTBRACKET comments_nl EQUALS comments_nl LEFTKEY comments_nl asignacionmatriz comments_nl RIGHTKEY comments_nl SEMICOLON np_anadir_variable comments_nl
        | tipo comments_nl ID np_obtener_nombre_var comments_nl LEFTBRACKET comments_nl CTEI np_obtener_filas comments_nl RIGHTBRACKET comments_nl LEFTBRACKET comments_nl CTEI np_obtener_columnas comments_nl RIGHTBRACKET comments_nl SEMICOLON np_anadir_variable comments_nl
        | tipo comments_nl ID np_obtener_nombre_var comments_nl LEFTBRACKET comments_nl CTEI np_obtener_filas comments_nl RIGHTBRACKET comments_nl EQUALS comments_nl LEFTKEY comments_nl asignacionarreglo comments_nl RIGHTKEY comments_nl SEMICOLON np_asignar_arreglo comments_nl
        | tipo comments_nl ID np_obtener_nombre_var comments_nl LEFTBRACKET comments_nl CTEI np_obtener_filas comments_nl RIGHTBRACKET comments_nl SEMICOLON np_asignar_arreglo comments_nl
        | tipo comments_nl ID np_obtener_nombre_var comments_nl EQUALS comments_nl ctes comments_nl SEMICOLON np_asignar_fil_col comments_nl
        | tipo comments_nl ID np_obtener_nombre_var comments_nl SEMICOLON np_asignar_fil_col comments_nl
    '''

def p_asignacionmatriz(p):
    '''
    asignacionmatriz : LEFTKEY comments_nl asignacionarreglo comments_nl RIGHTKEY comments_nl COMMA comments_nl asignacionmatriz comments_nl
                    | LEFTKEY comments_nl asignacionarreglo comments_nl RIGHTKEY comments_nl
    '''

def p_asignacionarreglo(p):
    '''
    asignacionarreglo : ctes comments_nl COMMA comments_nl asignacionarreglo comments_nl
                    | ctes comments_nl
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
    durante : WHILE comments_nl LEFTPARENTHESIS comments_nl mega_exp comments_nl RIGHTPARENTHESIS comments_nl bloque comments_nl
    '''

def p_condition(p):
    '''
    condition : IF comments_nl LEFTPARENTHESIS comments_nl mega_exp comments_nl RIGHTPARENTHESIS comments_nl bloque comments_nl else comments_nl
    '''

def p_else(p):
    '''
    else : ELSE comments_nl bloque comments_nl
        | empty
    '''

def p_mega_exp(p):
    '''
    mega_exp : expression_compare comments_nl mega_expaux comments_nl
    '''

def p_mega_expaux(p):
    '''
    mega_expaux : OR comments_nl expression_compare comments_nl mega_expaux comments_nl
                | AND comments_nl expression_compare comments_nl mega_expaux comments_nl
                | empty
    '''

def p_expression_compare(p):
    '''
    expression_compare : exp comments_nl DIFFERENT comments_nl exp comments_nl 
                    | exp comments_nl GTEQ comments_nl exp comments_nl
                    | exp comments_nl LTEQ comments_nl exp comments_nl 
                    | exp comments_nl EQUIVALENTE comments_nl exp comments_nl
                    | exp comments_nl GT comments_nl exp comments_nl
                    | exp comments_nl LT comments_nl exp comments_nl
                    | exp comments_nl
    '''

def p_exp(p):
    '''
    exp : termino comments_nl expaux comments_nl
    '''

def p_expaux(p):
    '''
    expaux : PLUS np_expaux_quad3 comments_nl termino np_expaux_quad4 comments_nl expaux comments_nl
            | MINUS np_expaux_quad3 comments_nl termino np_expaux_quad4 comments_nl expaux comments_nl
            | empty 
    '''

def p_termino(p):
    '''
    termino : factor comments_nl terminoaux comments_nl
    '''

def p_terminoaux(p):
    '''
    terminoaux : DIVIDE np_terminoaux_quad2 comments_nl factor np_terminoaux_quad5 comments_nl terminoaux comments_nl
                | MULTIPLY np_terminoaux_quad2 comments_nl factor np_terminoaux_quad5 comments_nl terminoaux comments_nl
                | empty
    '''

def p_factor(p):
    '''
    factor : vars_cte comments_nl
    		| PLUS comments_nl vars_cte comments_nl
            | MINUS comments_nl vars_cte comments_nl
            | LEFTPARENTHESIS comments_nl mega_exp comments_nl RIGHTPARENTHESIS comments_nl
    '''

def p_func(p):
    '''
    func : FUNC comments_nl VOID np_obtener_tipo comments_nl restofuncion comments_nl
        | FUNC comments_nl tipo comments_nl restofuncion comments_nl
    '''

def p_restofuncion(p):
    '''
    restofuncion : ID np_obtener_nombre_func comments_nl LEFTPARENTHESIS comments_nl argumentos comments_nl RIGHTPARENTHESIS comments_nl bloque comments_nl
    '''

def p_argumentos(p):
    '''
    argumentos : tipo comments_nl mismotipo comments_nl SEMICOLON comments_nl argumentos comments_nl
                | empty
    '''

def p_mismotipo(p):
    '''
    mismotipo : ID np_obtener_nombre_var comments_nl LEFTBRACKET comments_nl CTEI np_obtener_filas comments_nl RIGHTBRACKET comments_nl LEFTBRACKET comments_nl CTEI np_obtener_columnas comments_nl RIGHTBRACKET comments_nl COMMA np_anadir_variable comments_nl mismotipo comments_nl
                | ID np_obtener_nombre_var comments_nl LEFTBRACKET comments_nl CTEI np_obtener_filas comments_nl RIGHTBRACKET comments_nl COMMA np_asignar_arreglo comments_nl mismotipo comments_nl
                | ID np_obtener_nombre_var comments_nl COMMA np_asignar_fil_col comments_nl mismotipo comments_nl
                | ID np_obtener_nombre_var comments_nl LEFTBRACKET comments_nl CTEI np_obtener_filas comments_nl RIGHTBRACKET comments_nl LEFTBRACKET comments_nl CTEI np_obtener_columnas comments_nl RIGHTBRACKET comments_nl np_anadir_variable
                | ID np_obtener_nombre_var comments_nl LEFTBRACKET comments_nl CTEI np_obtener_filas comments_nl RIGHTBRACKET comments_nl np_asignar_arreglo
                | ID np_obtener_nombre_var comments_nl np_asignar_fil_col
    '''

def p_bloque(p):
    '''
    bloque : LEFTKEY comments_nl estatuto comments_nl RIGHTKEY comments_nl
    '''

def p_estatuto(p):
    '''
    estatuto : declaracionvariables comments_nl aplicaciones comments_nl
    '''

def p_declaracionvariables(p):
    '''
    declaracionvariables : vars comments_nl declaracionvariables comments_nl
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
                | llama_func comments_nl aplicaciones comments_nl
                | returnx comments_nl aplicaciones comments_nl
                | empty
    '''

def p_vars_cte(p):
    '''
    vars_cte : spec_func
            | ID comments_nl LEFTBRACKET comments_nl mega_exp comments_nl RIGHTBRACKET comments_nl LEFTBRACKET comments_nl mega_exp comments_nl RIGHTBRACKET comments_nl
            | ID comments_nl LEFTBRACKET comments_nl mega_exp comments_nl RIGHTBRACKET comments_nl
            | ID comments_nl LEFTPARENTHESIS comments_nl params comments_nl RIGHTPARENTHESIS comments_nl
            | ID np_factor_quad1 comments_nl
            | ctes comments_nl
    '''

def p_params(p):
    '''
    params : paramsaux comments_nl
            | empty
    '''
def p_paramsaux(p):
    '''
    paramsaux : mega_exp comments_nl COMMA comments_nl paramsaux comments_nl
                | mega_exp
    '''

def p_asignacion(p):
    '''
    asignacion : ID comments_nl LEFTBRACKET comments_nl mega_exp comments_nl RIGHTBRACKET comments_nl LEFTBRACKET comments_nl mega_exp comments_nl RIGHTBRACKET comments_nl EQUALS comments_nl mega_exp comments_nl SEMICOLON comments_nl
               | ID comments_nl LEFTBRACKET comments_nl mega_exp comments_nl RIGHTBRACKET comments_nl EQUALS comments_nl mega_exp comments_nl SEMICOLON comments_nl
               | ID np_asignacion_quad1 comments_nl EQUALS np_asignacion_quad2 comments_nl mega_exp comments_nl SEMICOLON np_asignacion_quad4 comments_nl
    '''	

def p_escritura(p):
    '''
    escritura : PRINT comments_nl LEFTPARENTHESIS comments_nl escrito comments_nl RIGHTPARENTHESIS comments_nl SEMICOLON comments_nl
    '''

def p_escrito(p):
    '''
    escrito : mega_exp comments_nl PLUS comments_nl escrito comments_nl
            | mega_exp comments_nl
    '''

def p_lectura(p):
    '''
    lectura : READ comments_nl LEFTPARENTHESIS comments_nl ID comments_nl LEFTBRACKET comments_nl mega_exp comments_nl RIGHTBRACKET comments_nl LEFTBRACKET comments_nl mega_exp comments_nl RIGHTBRACKET comments_nl RIGHTPARENTHESIS comments_nl SEMICOLON comments_nl
            | READ comments_nl LEFTPARENTHESIS comments_nl ID comments_nl LEFTBRACKET comments_nl mega_exp comments_nl RIGHTBRACKET comments_nl RIGHTPARENTHESIS comments_nl SEMICOLON comments_nl
            | READ comments_nl LEFTPARENTHESIS comments_nl ID comments_nl RIGHTPARENTHESIS comments_nl SEMICOLON comments_nl
    '''

def p_llama_spec_func(p):
    '''
    llama_spec_func : spec_func comments_nl SEMICOLON comments_nl
    '''

def p_spec_func(p):
    '''
    spec_func : SQRT comments_nl LEFTPARENTHESIS comments_nl mega_exp comments_nl RIGHTPARENTHESIS comments_nl 
                | POW comments_nl LEFTPARENTHESIS comments_nl mega_exp comments_nl COMMA comments_nl mega_exp comments_nl RIGHTPARENTHESIS comments_nl 
                | ABS comments_nl LEFTPARENTHESIS comments_nl mega_exp comments_nl RIGHTPARENTHESIS comments_nl 
                | STDEV comments_nl LEFTPARENTHESIS comments_nl mega_exp comments_nl RIGHTPARENTHESIS comments_nl 
                | MEAN comments_nl LEFTPARENTHESIS comments_nl mega_exp comments_nl RIGHTPARENTHESIS comments_nl 
                | MEDIAN comments_nl LEFTPARENTHESIS comments_nl mega_exp comments_nl RIGHTPARENTHESIS comments_nl 
                | MODE comments_nl LEFTPARENTHESIS comments_nl mega_exp comments_nl RIGHTPARENTHESIS comments_nl 
                | FACTORIAL comments_nl LEFTPARENTHESIS comments_nl mega_exp comments_nl RIGHTPARENTHESIS comments_nl 
                | SORT comments_nl LEFTPARENTHESIS comments_nl mega_exp comments_nl RIGHTPARENTHESIS comments_nl 
                | SIN comments_nl LEFTPARENTHESIS comments_nl mega_exp comments_nl RIGHTPARENTHESIS comments_nl 
                | COS comments_nl LEFTPARENTHESIS comments_nl mega_exp comments_nl RIGHTPARENTHESIS comments_nl 
                | TRANSPOSE comments_nl LEFTPARENTHESIS comments_nl mega_exp comments_nl RIGHTPARENTHESIS comments_nl 
                | EXPORTCSV comments_nl LEFTPARENTHESIS comments_nl mega_exp comments_nl COMMA comments_nl mega_exp comments_nl RIGHTPARENTHESIS comments_nl 
                | ARRANGE comments_nl LEFTPARENTHESIS comments_nl mega_exp comments_nl COMMA comments_nl mega_exp comments_nl COMMA comments_nl mega_exp comments_nl RIGHTPARENTHESIS comments_nl 
                | GRAPH3D comments_nl LEFTPARENTHESIS comments_nl mega_exp comments_nl COMMA comments_nl mega_exp comments_nl COMMA comments_nl mega_exp comments_nl RIGHTPARENTHESIS comments_nl 
                | PIECHART comments_nl LEFTPARENTHESIS comments_nl mega_exp comments_nl RIGHTPARENTHESIS comments_nl
                | HISTOGRAMCHART comments_nl LEFTPARENTHESIS comments_nl mega_exp comments_nl COMMA comments_nl mega_exp comments_nl RIGHTPARENTHESIS comments_nl
                | LINECHART comments_nl LEFTPARENTHESIS comments_nl mega_exp comments_nl COMMA comments_nl mega_exp comments_nl RIGHTPARENTHESIS comments_nl
                | BARCHART comments_nl LEFTPARENTHESIS comments_nl mega_exp comments_nl COMMA comments_nl mega_exp comments_nl RIGHTPARENTHESIS comments_nl
                | LINREG comments_nl LEFTPARENTHESIS comments_nl mega_exp comments_nl COMMA comments_nl mega_exp comments_nl RIGHTPARENTHESIS comments_nl
                | NOT comments_nl LEFTPARENTHESIS comments_nl mega_exp comments_nl RIGHTPARENTHESIS comments_nl
    '''

def p_returnx(p):
    '''
    returnx : RETURNX comments_nl mega_exp comments_nl SEMICOLON comments_nl
    '''

def p_ctes(p):
    '''
    ctes : CTEI comments_nl
        | CTEF comments_nl
        | CTES comments_nl
        | CTEB comments_nl
    '''

def p_llama_func(p):
    '''
    llama_func : ID comments_nl LEFTPARENTHESIS comments_nl params comments_nl RIGHTPARENTHESIS comments_nl SEMICOLON comments_nl
    '''

def p_comments_nl(p):
	'''
	comments_nl : NEWLINE comments_nl
				| COMENTARIO comentarioaux
				| empty
	'''

def p_comentarioaux(p):
    '''
    comentarioaux 	: NEWLINE comentarioaux comments_nl
    				| empty
        
    '''

def p_empty(p):
	'''
    empty :
    ''' 

def p_error(p):
    print ("Syntax error in line " + str(lexer.lineno))


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

def p_np_obtener_filas(p):
    '''
    np_obtener_filas : empty
    '''
    numFilas = int(p[-1])
    setIVarFilas(numFilas)

def p_np_obtener_columnas(p):
    '''
    np_obtener_columnas : empty
    '''
    numCol = int(p[-1])
    setIVarColumnas(numCol)

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
	setIVarColumnas(0)
	anadirVar()

def p_np_main_func(p):
    '''
    np_main_func : empty
    '''
    funName = str(p[-1])
    setNombreFunc(funName)
    setTipoDato('void')
    anadirFunc()

def p_np_factor_quad1(p):
	'''
	np_factor_quad1 : empty
	'''
	tempIdName = str(p[-1])
	addIdToStack(tempIdName)

def p_np_asignacion_quad1(p):
	'''
	np_asignacion_quad1 : empty
	'''
	tempIdName = str(p[-1])
	addIdToStack(tempIdName)

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
	print("Asignacion_quad4: ")
	print(pilaOperadores)
	print(pilaOperando)
	print(pilaTipos)
	tuplaOperadores = ('=')
	operacionesEnPilasId(tuplaOperadores, 2)

def p_np_terminoaux_quad5(p):
	'''
	np_terminoaux_quad5 : empty
	'''
	tuplaOperadores = ('*','/')
	operacionesEnPilasId(tuplaOperadores, 1)

parser = yacc.yacc() 

#Cambiar el nombre del archivo de entrada para probar el codigo
#name='pruebaRose.txt'
name='pruebaCuad1.txt'

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
