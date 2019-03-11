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
    'ID'
]

t_COLON= r'\:'
t_SEMICOLON= r'\;'
t_PERIOD= r'\.'
t_COMMA= r'\,'
t_PLUS= r'\+'
t_MINUS= r'\-'
t_DIVIDE= r'\/'
t_MULTIPLY= r'\*'
t_EQUALS= r'\='
t_GT= r'\>'
t_LT= r'\<'
t_DIFFERENT= r'\<\>'
t_LEFTBRACKET= r'\{'
t_RIGHTBRACKET= r'\}'
t_LEFTPARENTHESIS= r'\('
t_RIGHTPARENTHESIS= r'\)'
t_VAR=r'var'
t_IF=r'if'
t_ELSE=r'else'
t_PROGRAM=r'program'
t_INT=r'int'
t_FLOAT=r'float'
t_PRINT=r'print'
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
    elif t.value=='var':
        t.type='VAR'
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

""""
lexer.input("program test;")

while True:
    tok = lexer.token()
    if not tok:
        break
    print (tok)
"""

def p_patito(p):
    '''
    patito : PROGRAM ID SEMICOLON vars bloque
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
    vars : VAR c
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