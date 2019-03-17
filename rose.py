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
	'RIGHTKEY',
	'NEWLINE'
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
    print("Salto de linea " + str(lexer.lineno))
    return t


def t_error(t):
    print("Caracteres no reconocidos " + str(t.type))
    t.lexer.skip(1)

t_ignore = r' '

lexer = lex.lex()


"""
lexer.input('program test; globals int arbol = 3; func void myfunk(int ola;){ } main (){ int arbol = 5; if(arbol>6){print(arbol);}else{ print(arbol);};}')

while True:
    tok = lexer.token()
    if not tok:
        break
    print (tok)
"""

def p_rose(p):
    '''
    rose : PROGRAM eol ID eol SEMICOLON eol roseauxvars eol roseauxfunc eol main eol
    '''
    print("Exito. # salto de linea: " + str(lexer.lineno))

def p_roseauxvars(p):
    '''
    roseauxvars : GLOBALS eol vars eol roseauxvars eol
            | empty
    '''

def p_roseauxfunc(p):
    '''
    roseauxfunc : func eol roseauxfunc eol
                | empty
    '''
def p_main(p):
    '''
    main : MAIN eol LEFTPARENTHESIS eol RIGHTPARENTHESIS eol bloque eol
    '''

def p_vars(p):
    '''
    vars : tipo eol ID eol LEFTBRACKET eol CTEI eol RIGHTBRACKET eol LEFTBRACKET eol CTEI eol RIGHTBRACKET eol EQUALS eol LEFTKEY eol asignacionmatriz eol  RIGHTKEY eol SEMICOLON eol
        | tipo eol ID eol LEFTBRACKET eol CTEI eol RIGHTBRACKET eol LEFTBRACKET eol CTEI eol RIGHTBRACKET eol SEMICOLON eol
        | tipo eol ID eol LEFTBRACKET eol CTEI eol RIGHTBRACKET eol EQUALS eol LEFTKEY eol asignacionarreglo eol RIGHTKEY eol SEMICOLON eol
        | tipo eol ID eol LEFTBRACKET eol CTEI eol RIGHTBRACKET eol SEMICOLON eol
        | tipo eol ID eol EQUALS eol ctes eol SEMICOLON eol
        | tipo eol ID eol SEMICOLON eol
    '''

def p_asignacionmatriz(p):
    '''
    asignacionmatriz : LEFTKEY eol asignacionarreglo eol RIGHTKEY eol COMMA eol asignacionmatriz eol
                    | LEFTKEY eol asignacionarreglo eol RIGHTKEY eol
    '''

def p_asignacionarreglo(p):
    '''
    asignacionarreglo : ctes eol COMMA eol asignacionarreglo eol
                    | ctes eol
    '''

def p_tipo(p):
    '''
    tipo : INT eol
        | FLOAT eol
        | STRING eol
        | BOOL eol
    '''

def p_durante(p):
    '''
    durante : WHILE eol LEFTPARENTHESIS eol mega_exp eol RIGHTPARENTHESIS eol bloque eol
    '''

def p_condition(p):
    '''
    condition : IF eol LEFTPARENTHESIS eol mega_exp eol RIGHTPARENTHESIS eol bloque eol else eol
    '''

def p_else(p):
    '''
    else : ELSE eol bloque eol
        | empty
    '''

def p_mega_exp(p):
    '''
    mega_exp : expression_compare eol mega_expaux eol
    '''

def p_mega_expaux(p):
    '''
    mega_expaux : OR eol expression_compare eol mega_expaux eol
                | AND eol expression_compare eol mega_expaux eol
                | empty
    '''

def p_expression_compare(p):
    '''
    expression_compare : exp eol DIFFERENT eol exp eol 
                    | exp eol GTEQ eol exp eol
                    | exp eol LTEQ eol exp eol 
                    | exp eol EQUIVALENTE eol exp eol
                    | exp eol GT eol exp eol
                    | exp eol LT eol exp eol
                    | exp eol
    '''

def p_exp(p):
    '''
    exp : termino eol expaux eol
    '''

def p_expaux(p):
    '''
    expaux : PLUS eol termino eol expaux eol
            | MINUS eol termino eol expaux eol
            | empty 
    '''

def p_termino(p):
    '''
    termino : factor eol terminoaux eol
    '''

def p_terminoaux(p):
    '''
    terminoaux : DIVIDE eol factor eol terminoaux eol
                | MULTIPLY eol factor eol terminoaux eol
                | empty
    '''

def p_factor(p):
    '''
    factor : PLUS eol vars_cte eol
            | MINUS eol vars_cte eol
            | vars_cte eol
            | LEFTPARENTHESIS eol mega_exp eol RIGHTPARENTHESIS eol
    '''

def p_func(p):
    '''
    func : FUNC eol VOID eol restofuncion eol
        | FUNC eol tipo eol restofuncion eol
    '''

def p_restofuncion(p):
    '''
    restofuncion : ID eol LEFTPARENTHESIS eol argumentos eol RIGHTPARENTHESIS eol bloque eol
    '''

def p_argumentos(p):
    '''
    argumentos : tipo eol mismotipo eol SEMICOLON eol argumentos eol
                | empty
    '''

def p_mismotipo(p):
    '''
    mismotipo : ID eol LEFTBRACKET eol CTEI eol RIGHTBRACKET eol LEFTBRACKET eol CTEI eol RIGHTBRACKET eol COMMA eol mismotipo eol
                | ID eol LEFTBRACKET eol CTEI eol RIGHTBRACKET eol COMMA eol mismotipo eol
                | ID eol COMMA eol mismotipo eol
                | ID eol LEFTBRACKET eol CTEI eol RIGHTBRACKET eol LEFTBRACKET eol CTEI eol RIGHTBRACKET eol
                | ID eol LEFTBRACKET eol CTEI eol RIGHTBRACKET eol
                | ID eol  

    '''

def p_bloque(p):
    '''
    bloque : LEFTKEY eol estatuto eol RIGHTKEY eol
    '''

def p_estatuto(p):
    '''
    estatuto : declaracionvariables eol aplicaciones eol
    '''

def p_declaracionvariables(p):
    '''
    declaracionvariables : vars eol declaracionvariables eol
                        | empty
    '''
def p_aplicaciones(p):
    '''
    aplicaciones : condition eol aplicaciones eol
                | escritura eol aplicaciones eol
                | lectura eol aplicaciones eol
                | llama_spec_func eol aplicaciones eol
                | asignacion eol aplicaciones eol
                | durante eol aplicaciones eol
                | llama_func eol aplicaciones eol
                | returnx eol aplicaciones eol
                | empty
    '''

def p_vars_cte(p):
    '''
    vars_cte : spec_func
            | ID eol LEFTBRACKET eol mega_exp eol RIGHTBRACKET eol LEFTBRACKET eol mega_exp eol RIGHTBRACKET eol
            | ID eol LEFTBRACKET eol mega_exp eol RIGHTBRACKET eol
            | ID eol LEFTPARENTHESIS eol params eol RIGHTPARENTHESIS eol
            | ID eol
            | ctes eol
    '''

def p_params(p):
    '''
    params : paramsaux eol
            | empty
    '''
def p_paramsaux(p):
    '''
    paramsaux : mega_exp eol COMMA eol paramsaux eol
                | mega_exp
    '''

def p_asignacion(p):
    '''
    asignacion : ID eol LEFTBRACKET eol mega_exp eol RIGHTBRACKET eol LEFTBRACKET eol mega_exp eol RIGHTBRACKET eol EQUALS eol mega_exp eol SEMICOLON eol
               | ID eol LEFTBRACKET eol mega_exp eol RIGHTBRACKET eol EQUALS eol mega_exp eol SEMICOLON eol
               | ID eol EQUALS eol mega_exp eol SEMICOLON eol
    '''

def p_escritura(p):
    '''
    escritura : PRINT eol LEFTPARENTHESIS eol escrito eol RIGHTPARENTHESIS eol SEMICOLON eol
    '''
def p_escrito(p):
    '''
    escrito : mega_exp eol PLUS eol escrito eol
            | mega_exp eol
    '''
def p_lectura(p):
    '''
    lectura : READ eol LEFTPARENTHESIS eol ID eol LEFTBRACKET eol mega_exp eol RIGHTBRACKET eol LEFTBRACKET eol mega_exp eol RIGHTBRACKET eol RIGHTPARENTHESIS eol SEMICOLON eol
            | READ eol LEFTPARENTHESIS eol ID eol LEFTBRACKET eol mega_exp eol RIGHTBRACKET eol RIGHTPARENTHESIS eol SEMICOLON eol
            | READ eol LEFTPARENTHESIS eol ID eol RIGHTPARENTHESIS eol SEMICOLON eol
    '''

def p_llama_spec_func(p):
    '''
    llama_spec_func : spec_func eol SEMICOLON eol
    '''

def p_spec_func(p):
    '''
    spec_func : SQRT eol LEFTPARENTHESIS eol mega_exp eol RIGHTPARENTHESIS eol 
                | POW eol LEFTPARENTHESIS eol mega_exp eol COMMA eol mega_exp eol RIGHTPARENTHESIS eol 
                | ABS eol LEFTPARENTHESIS eol mega_exp eol RIGHTPARENTHESIS eol 
                | STDEV eol LEFTPARENTHESIS eol mega_exp eol RIGHTPARENTHESIS eol 
                | MEAN eol LEFTPARENTHESIS eol mega_exp eol RIGHTPARENTHESIS eol 
                | MEDIAN eol LEFTPARENTHESIS eol mega_exp eol RIGHTPARENTHESIS eol 
                | MODE eol LEFTPARENTHESIS eol mega_exp eol RIGHTPARENTHESIS eol 
                | FACTORIAL eol LEFTPARENTHESIS eol mega_exp eol RIGHTPARENTHESIS eol 
                | SORT eol LEFTPARENTHESIS eol mega_exp eol RIGHTPARENTHESIS eol 
                | SIN eol LEFTPARENTHESIS eol mega_exp eol RIGHTPARENTHESIS eol 
                | COS eol LEFTPARENTHESIS eol mega_exp eol RIGHTPARENTHESIS eol 
                | TRANSPOSE eol LEFTPARENTHESIS eol mega_exp eol RIGHTPARENTHESIS eol 
                | EXPORTCSV eol LEFTPARENTHESIS eol mega_exp eol COMMA eol mega_exp eol RIGHTPARENTHESIS eol 
                | ARRANGE eol LEFTPARENTHESIS eol mega_exp eol COMMA eol mega_exp eol COMMA eol mega_exp eol RIGHTPARENTHESIS eol 
                | GRAPH3D eol LEFTPARENTHESIS eol mega_exp eol COMMA eol mega_exp eol COMMA eol mega_exp eol RIGHTPARENTHESIS eol 
                | PIECHART eol LEFTPARENTHESIS eol mega_exp eol RIGHTPARENTHESIS eol
                | HISTOGRAMCHART eol LEFTPARENTHESIS eol mega_exp eol COMMA eol mega_exp eol RIGHTPARENTHESIS eol
                | LINECHART eol LEFTPARENTHESIS eol mega_exp eol COMMA eol mega_exp eol RIGHTPARENTHESIS eol
                | BARCHART eol LEFTPARENTHESIS eol mega_exp eol COMMA eol mega_exp eol RIGHTPARENTHESIS eol
                | LINREG eol LEFTPARENTHESIS eol mega_exp eol COMMA eol mega_exp eol RIGHTPARENTHESIS eol
                | NOT eol LEFTPARENTHESIS eol mega_exp eol RIGHTPARENTHESIS eol
    '''

def p_returnx(p):
    '''
    returnx : RETURNX eol mega_exp eol SEMICOLON eol
    '''

def p_ctes(p):
    '''
    ctes : CTEI eol
        | CTEF eol
        | CTES eol
        | CTEB eol
    '''

def p_llama_func(p):
    '''
    llama_func : ID eol LEFTPARENTHESIS eol params eol RIGHTPARENTHESIS eol SEMICOLON eol
    '''
def p_eol(p):
	'''
	eol : NEWLINE eol
		| empty
	'''
	#print("Nueva linea" + str(p.lineno(1)))

def p_empty(p):
	'''
    empty :
    ''' 

def p_error(p):
    print ("Syntax error in line " + str(lexer.lineno))

parser = yacc.yacc() 

#Cambiar el nombre del archivo de entrada para probar el codigo
name='pruebaRose.txt'
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
