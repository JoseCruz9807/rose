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
    'FUNCTION',
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
    'FALSE',
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
    'TRUE',
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

	###CHECAR SI ESTAS SE QUEDAN O SE VAN
    'GET',
    'SET',

    'QUOTE',
    'NOT',
    'OR'
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
t_NOT= r'\!'
t_GTEQ= r'\>\='
t_LTEQ= r'\<\='
t_EQUIVALENTE= r'\=\='

t_EQUALS= r'\='
t_GT= r'\>'
t_LT= r'\<'
t_DIFFERENT= r'\!\='
t_LEFTBRACKET= r'\{'
t_RIGHTBRACKET= r'\}'
t_LEFTPARENTHESIS= r'\('
t_RIGHTPARENTHESIS= r'\)'

t_INT= r'int'
t_IF= r'if'
t_FLOAT= r'float'
t_ELSE= r'else'
t_STRING= r'string'
t_FALSE= r'false'
t_WHILE= r'while'
t_BOOL= r'bool'
t_TRUE= r'true'
t_SIN= r'sin'
t_COS= r'cos'
t_OR= r'OR'
t_AND= r'AND'
t_TAN= r'tan'
t_PRINT= r'print'
t_RETURN= r'return'
t_READ= r'read'
t_SQRT= r'sqrt'
t_POW= r'pow'
t_ABS= r'abs'

###CHECAR SI SE QUEDAN O SE VAN SET Y GET
t_GET= r'get'
t_SET= r'set'
###

t_GRAPH= r'graph'
t_STDEV= r'stdev'
t_MEAN= r'mean'
t_MEDIAN= r'median'
t_MODE= r'mode'
t_FACTORIAL= r'factorial'
t_SORT= r'sort'
t_LINREG= r'linreg'
t_FUNCTION= r'function'

###CHECAR SI APPEND SE QUEDA
t_APPEND= r'append'

t_MAIN= r'main'
t_EXPORTCSV= r'exportCSV'
t_ARRANGE= r'arrange'
t_GRAPH3D= r'graph3d'
t_PIECHART= r'pieChart'
t_LINECHART= r'lineChart'
t_BARCHART= r'barChart'
t_HISTOGRAMCHART= r'histogramChart'
t_TRANSPOSE= r'transpose'
t_GLOBALS= r'globals'
t_PROGRAM= r'program'



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
    


	###CHECAR SI ESTOS SEQUEDAN O SE VAN
    elif t.value=='set':
        t.type='SET'
    elif t.value=='get':
        t.type='GET'



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
    elif t.value=='TRUE':
        t.type='TRUE'
    elif t.value=='while':
        t.type='WHILE'
    elif t.value=='false':
        t.type='FALSE'
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
    elif t.value=='function':
        t.type='FUNCTION'
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
lexer.input("program test; ")

while True:
    tok = lexer.token()
    if not tok:
        break
    print (tok)
"""


def p_rose(p):
    '''
    rose : PROGRAM ID SEMICOLON vars bloque
            | PROGRAM ID SEMICOLON bloque
    '''
    print("Exito")


def p_bloque(p):
    '''
    bloque : LEFTBRACKET b RIGHTBRACKET
    '''
def p_b(p):
    '''
    b : estatuto b
        | empty
    '''

def p_estatuto(p):
    '''
    estatuto : asignacion
            | condicion
            | escritura
    '''

def p_vars(p):
    '''
    vars : GLOBALS c
    '''


def p_c(p):
    '''
    c : ID COMMA c
        | ID COLON tipo SEMICOLON c
        | ID COLON tipo SEMICOLON
    '''

def p_tipo(p):
    '''
    tipo : INT 
        | FLOAT
    '''

def p_asignacion(p):
    '''
    asignacion : ID EQUALS expresion SEMICOLON
    '''

def p_escritura(p):
    '''
    escritura : PRINT LEFTPARENTHESIS e RIGHTPARENTHESIS SEMICOLON
    '''

def p_e(p):
    '''
    e : expresion PERIOD e
        | CTES PERIOD e
        | CTES
        | expresion
        | empty
    '''


def p_expresion(p):
    '''
    expresion : exp GT exp
                | exp LT exp
                | exp DIFFERENT exp
                | exp
    '''

def p_exp(p):
    '''
    exp : termino g
    '''


def p_g(p):
    '''
    g : PLUS termino g
        | MINUS termino g
        | empty
    '''

def p_condicion(p):
    '''
    condicion : IF LEFTPARENTHESIS expresion RIGHTPARENTHESIS bloque h SEMICOLON
    '''

def p_h(p):
    '''
    h : ELSE bloque 
        | empty
    '''

def p_termino(p):
    '''
    termino : factor i
            | factor
    '''

def p_i(p):
    '''
    i : MULTIPLY factor i
        | DIVIDE factor i
        | MULTIPLY factor
        | DIVIDE factor
    '''

def p_factor(p):
    '''
    factor : LEFTPARENTHESIS expresion RIGHTPARENTHESIS
            | PLUS varcte
            | MINUS varcte
            | varcte
    '''

def p_varcte(p):
    '''
    varcte : ID
            | CTEI
            | CTEF
    '''

def p_empty(p):
    '''
    empty : 
    '''

def p_error(p):
    print ("Error de compilacion")

parser = yacc.yacc() 

#Cambiar el nombre del archivo de entrada para tener probar el codigo incorrecto
name='codigoCorrecto.txt'
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
