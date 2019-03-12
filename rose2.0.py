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
    'STRING',
    'BOOL',
    'VOID',
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
    elif t.value=='graph3d':
        t.type='GRAPH3D'
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
    elif t.value=='lineChart':
        t.type='LINECHART'
    elif t.value=='barChart':
        t.type='BARCHART'
    elif t.value=='histogramChart':
        t.type='HISTOGRAMCHART'
    elif t.value=='void':
        t.type='VOID'
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

def p_program(p):
    '''
    program : PROGRAM ID SEMICOLON program1 INT MAIN main 
    '''
    print("Exito")
def p_program1(p):
    '''
    program1   : GLOBALS vars varsaux program2
                | program2
                | empty
    '''
def p_varsaux(p):
    '''
    varsaux : vars varsaux
            | empty
    '''
def p_program2(p):
    '''
    program2    : func program2
                | empty
    '''

def p_main(p):
    '''
    main    : LEFTPARENTHESIS RIGHTPARENTHESIS bloque
    '''

def p_vars(p):
    '''
    vars    : tipo ID vars1 SEMICOLON
    '''
def p_vars1(p):
    '''
    vars1   : EQUALS varscte
            | LEFTBRACKET INT RIGHTBRACKET asignaruni
            | LEFTBRACKET INT RIGHTBRACKET LEFTBRACKET INT RIGHTBRACKET asignarbi
            | empty
    '''
    
#######################
###CHECAR ESTA PARTE###
#######################
def p_asignaruni(p):
    '''
    asignaruni  : EQUALS contenidoarray
                | empty
    '''
def p_contenidoarray(p):
    '''
    contenidoarray  : LEFTKEY varscte asignaruni1 RIGHTKEY
                    | empty
    '''
def p_asignaruni1(p):
    '''
    asignaruni1 : COMMA varscte asignaruni1
                | empty
    '''
def p_asignarbi(p):
    '''
    asignarbi   : EQUALS LEFTKEY asignarbi2 RIGHTKEY
                | empty
    '''
def p_asignarbi2(p):
    '''
    asignarbi2  : contenidoarray asignarbi3
                | empty
    '''
def p_asignarbi3(p):
    '''
    asignarbi3  : COMMA contenidoarray asignarbi3
                | empty
    '''
