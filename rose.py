import ply.lex as lex
import ply.yacc as yacc
import sys

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
    'PIECHART',
    'BARCHART',
    'ARRANGE',
    'GRAPH3D',
    'GLOBALS',
    'STRING',
    'RETURN',
    'MEDIAN',
    'LINREG',
    'APPEND',
    'WHILE',
    'POW',
    'GRAPH',
    'STDEV',
    'MULTICOMOP',
    'MULTICOMCL',
    'COMMENT',
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
	'RIGHTKEY'
]

#MultiCommentOpen
t_MULTICOMOP= r'\/\*'
#MultiCommentClose
t_MULTICOMCL= r'\*\/'

t_COMMENT= r'\/\/'

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
t_NOT= r'\!'
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


t_ignore = r' '

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
        t.type='RETURN'
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
        t.type='histogramChart'
    else:
        t.type = 'ID'
    return t

def t_CTES (t):
    r'\'[a-zA-Z_ 0-9]+\''
    t.type = 'CTES'
    return t

def t_error(t):
    print("Caracteres no reconocidos")
    t.lexer.skip(1)

lexer = lex.lex()


"""
lexer.input("globals arbol: int; ")

while True:
    tok = lexer.token()
    if not tok:
        break
    print (tok)
"""

def p_rose(p):
    '''
    rose : PROGRAM ID SEMICOLON roseaux MAIN main
    '''
    print("Exito")


def p_roseaux(p):
    '''
	roseaux :	GLOBALS vars roseaux2 roseaux3
			| 	func roseaux3
			|	empty
    '''
def p_roseaux2(p):
    '''
	roseaux2 :	vars roseaux2
			 |	empty
	'''
def p_roseaux3(p):
    '''
	roseaux3 :	func roseaux3
			 |	empty
	'''

def p_vars(p):
	'''
	vars : tipo ID varsaux SEMICOLON
	'''
def p_varsaux(p):
	'''
	varsaux :	arreglo varsaux1
			|	EQUALS varscte
			|	empty
	'''
def p_varsaux1(p):
	'''
	varsaux1 :	asigna
			 |	arreglo asigna
	'''

def p_arreglo(p):
	'''
	arreglo :	LEFTBRACKET varscte RIGHTBRACKET
	'''

def p_asigna(p):
	'''
	asigna	:	EQUALS asigna1
			|	empty
	'''
def p_asigna1(p):
	'''
	asigna1	:	unidimensional
			|	bidimensional
	'''


def p_unidimensional(p):
	'''
	unidimensional :	LEFTKEY varscte unidime1 RIGHTKEY
	'''
def p_unidime1(p):
	'''
	unidime1 :	COMMA varscte unidime1
			 |	empty
	'''

def p_bidimensional(p):
	'''
	bidimensional :	LEFTKEY unidimensional bidi1 RIGHTKEY
	'''
def p_bidi1(p):
	'''
	bidi1	:	COMMA unidimensional
			|	empty
	'''


def p_expcomp(p):
	'''
	expcomp	:	exp expcomp1
	'''
def p_expcomp1(p):
	'''
	expcomp1 :	expcomp2
			 |	empty
	'''
def p_expcomp2(p):
	'''
	expcomp2 :	logicalexp exp
			 |	GTEQ exp
			 |	LTEQ exp
			 |	EQUIVALENTE exp
			 |	GT exp
			 |	LT exp
			 |	DIFFERENT exp
	'''

def p_logicalexp(p):
	'''
	logicalexp	:	OR
				|	AND
	'''

def p_durante(p):
	'''
	durante	:	WHILE LEFTPARENTHESIS expcomp RIGHTPARENTHESIS bloque
			
	'''

def p_exp(p):
	'''
	exp	:	termino exp1
	'''
def p_exp1(p):
	'''
	exp1 :	PLUS exp
		 |	MINUS exp
         |  empty
	'''

def p_termino(p):
	'''
	termino	:	factor ter1
	'''
def p_ter1(p):
	'''
	ter1 :	MULTIPLY termino
		 |	DIVIDE termino
         |  empty
	'''

def p_factor(p):
	'''
	factor	:	PLUS varscte
			|	MINUS varscte
			|	varscte
			|	LEFTPARENTHESIS exp RIGHTPARENTHESIS
	'''

def p_func(p):
	'''
	func	:	func1 LEFTPARENTHESIS func2 RIGHTPARENTHESIS bloque
	'''
def p_func1(p):
	'''
	func1	:	tipo
			|	FUNC
	'''
def p_func2(p):
	'''
	func2	:	tipo func3
	'''
def p_func3(p):
	'''
	func3	:	ID tiposid func4
	'''
def p_func4(p):
	'''
	func4	:	COMMA ID func3
			| 	SEMICOLON func5
	'''
def p_func5(p):
	'''
	func5	:	func2
			| 	empty
	'''

def p_tiposid(p):
    '''
    tiposid : LEFTBRACKET exp RIGHTBRACKET tiposid1
    		| empty
    '''
def p_tiposid1(p):
    '''
    tiposid1 : LEFTBRACKET exp RIGHTBRACKET
    		 | empty
    '''

def p_condition(p):
    '''
    condition 	: IF LEFTPARENTHESIS expcomp RIGHTPARENTHESIS bloque condi1
    '''
def p_condi1(p):
    '''
    condi1 	: 	ELSE bloque
    		|	empty
    '''

def p_bloque(p):
    '''
    bloque 	: 	LEFTKEY bloque1 RIGHTKEY
    '''
def p_bloque1(p):
    '''
    bloque1	: 	estatuto
    		|	empty
    '''

def p_estatuto(p):
    '''
    estatuto 	: 	estatuto1 estatuto2
    '''
def p_estatuto1(p):
    '''
    estatuto1 	: 	vars estatuto1
    			|	empty
    '''
def p_estatuto2(p):
    '''
    estatuto2 	: 	condition estatuto2
    			|	escritura estatuto2
    			|	lectura estatuto2
    			|	specfun estatuto2
    			|	asignacion estatuto2
    			|	durante estatuto2
    			|	empty
    '''

def p_varscte(p):
	'''
    varscte : ID tiposid
    		| CTEI
    		| CTEF
    		| CTES
    		| CTEB
    ''' 

def p_asignacion(p):
	'''
    asignacion : ID tiposid EQUALS expcomp SEMICOLON
    ''' 

def p_escritura(p):
	'''
    escritura : PRINT LEFTPARENTHESIS escri1 RIGHTPARENTHESIS SEMICOLON
    ''' 
def p_escri1(p):
	'''
    escri1 : expcomp escri2
    ''' 
def p_escri2(p):
	'''
    escri2 	: PLUS escri1
			| empty
    ''' 

def p_lectura(p):
	'''
    lectura : READ LEFTPARENTHESIS ID tiposid LEFTPARENTHESIS SEMICOLON
    '''

def p_specfun(p):
	'''
    specfun : specfun1 LEFTPARENTHESIS specfun2 RIGHTPARENTHESIS SEMICOLON
    ''' 

########################
# Nombres de funciones #
########################
def p_specfun1(p):
	'''
    specfun1 : SQRT
    		 | POW
    		 | ABS
    		 | STDEV
    		 | MEAN
    		 | MEDIAN
    		 | MODE
    		 | FACTORIAL
    		 | SORT
    		 | SIN
    		 | COS
    		 | TRANSPOSE
    		 | EXPORTCSV
    		 | ARRANGE
    		
    ''' 
def p_specfun2(p):
	'''
    specfun2 : varscte specfun3
    		 | empty
    ''' 
def p_specfun3(p):
	'''
    specfun3 : COMMA specfun2
    		 | empty
	'''

def p_main(p):
    '''
    main : bloque
    ''' 

def p_tipo(p):
    '''
    tipo    : INT
            | FLOAT
            | STRING
            | BOOL 
    ''' 



def p_empty(p):
	'''
    empty :
    ''' 

def p_error(p):
    print ("Error de compilacion")

parser = yacc.yacc() 

#Cambiar el nombre del archivo de entrada para tener probar el codigo incorrecto
name='pruebaRose.txt'
with open(name, 'r') as myfile:
    s=myfile.read().replace('\n', '')
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
