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
        t.type='histogramChart'
    else:
        t.type = 'ID'
    return t

def t_CTES (t):
    r'\"[a-zA-Z_ 0-9]+\"'
    t.type = 'CTES'
    return t

def t_error(t):
    print("Caracteres no reconocidos")
    t.lexer.skip(1)

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
    rose : PROGRAM ID SEMICOLON roseauxvars roseauxfunc MAIN main
    '''
    print("Exito")

def p_roseauxvars(p):
    '''
    roseauxvars : GLOBALS vars roseauxvars
            | empty
    '''

def p_roseauxfunc(p):
    '''
    roseauxfunc : func roseauxfunc
                | empty
    '''
def p_main(p):
    '''
    main : LEFTPARENTHESIS RIGHTPARENTHESIS bloque
    '''

def p_vars(p):
    '''
    vars : tipo ID LEFTBRACKET CTEI RIGHTBRACKET LEFTBRACKET CTEI RIGHTBRACKET EQUALS LEFTKEY asignacionmatriz  RIGHTKEY SEMICOLON
        | tipo ID LEFTBRACKET CTEI RIGHTBRACKET LEFTBRACKET CTEI RIGHTBRACKET SEMICOLON
        | tipo ID LEFTBRACKET CTEI RIGHTBRACKET EQUALS LEFTKEY asignacionarreglo RIGHTKEY SEMICOLON
        | tipo ID LEFTBRACKET CTEI RIGHTBRACKET SEMICOLON
        | tipo ID EQUALS vars_cte SEMICOLON
        | tipo ID SEMICOLON
    '''

def p_asignacionmatriz(p):
    '''
    asignacionmatriz : LEFTKEY asignacionarreglo RIGHTKEY COMMA asignacionmatriz
                    | LEFTKEY asignacionarreglo RIGHTKEY
    '''

def p_asignacionarreglo(p):
    '''
    asignacionarreglo : vars_cte COMMA asignacionarreglo
                    | vars_cte
    '''

def p_tipo(p):
    '''
    tipo : INT
        | FLOAT
        | STRING
        | BOOL
    '''

def p_durante(p):
    '''
    durante : WHILE LEFTPARENTHESIS mega_exp RIGHTPARENTHESIS sudo_bloque
    '''

def p_condition(p):
    '''
    condition : IF LEFTPARENTHESIS mega_exp RIGHTPARENTHESIS sudo_bloque else
    '''

def p_else(p):
    '''
    else : ELSE sudo_bloque
        | empty
    '''

def p_mega_exp(p):
    '''
    mega_exp : expression_compare mega_expaux
    '''

def p_mega_expaux(p):
    '''
    mega_expaux : OR expression_compare mega_expaux
                | AND expression_compare mega_expaux
                | empty
    '''

def p_expression_compare(p):
    '''
    expression_compare : exp DIFFERENT exp 
                    | exp GTEQ exp
                    | exp LTEQ exp 
                    | exp EQUIVALENTE exp
                    | exp GT exp
                    | exp LT exp
                    | exp
    '''

def p_exp(p):
    '''
    exp : termino expaux
    '''

def p_expaux(p):
    '''
    expaux : PLUS termino expaux
            | MINUS termino expaux
            | empty 
    '''

def p_termino(p):
    '''
    termino : factor terminoaux
    '''

def p_terminoaux(p):
    '''
    terminoaux : DIVIDE factor terminoaux
                | MULTIPLY factor terminoaux
                | empty
    '''

def p_factor(p):
    '''
    factor : PLUS vars_cte
            | MINUS vars_cte
            | vars_cte
            | LEFTPARENTHESIS mega_exp RIGHTPARENTHESIS
    '''

def p_func(p):
    '''
    func : FUNC VOID restofuncion
        | FUNC tipo restofuncion
    '''

def p_restofuncion(p):
    '''
    restofuncion : ID LEFTPARENTHESIS argumentos RIGHTPARENTHESIS bloque
    '''

def p_argumentos(p):
    '''
    argumentos : tipo mismotipo SEMICOLON argumentos
                | empty
    '''

def p_mismotipo(p):
    '''
    mismotipo : ID LEFTBRACKET CTEI RIGHTBRACKET LEFTBRACKET CTEI RIGHTBRACKET COMMA mismotipo
                | ID LEFTBRACKET CTEI RIGHTBRACKET COMMA mismotipo
                | ID COMMA mismotipo
                | ID LEFTBRACKET CTEI RIGHTBRACKET LEFTBRACKET CTEI RIGHTBRACKET  
                | ID LEFTBRACKET CTEI RIGHTBRACKET  
                | ID  

    '''

def p_bloque(p):
    '''
    bloque : LEFTKEY estatuto RIGHTKEY
    '''

def p_estatuto(p):
    '''
    estatuto : declaracionvariables aplicaciones
    '''

def p_declaracionvariables(p):
    '''
    declaracionvariables : vars declaracionvariables
                        | empty
    '''
def p_aplicaciones(p):
    '''
    aplicaciones : condition aplicaciones
                | escritura aplicaciones
                | lectura aplicaciones
                | llama_spec_func aplicaciones
                | asignacion aplicaciones
                | durante aplicaciones
                | llama_func aplicaciones
                | empty
    '''

def p_sudo_bloque(p):
    '''
    sudo_bloque : LEFTKEY sudo_estatuto RIGHTKEY
    '''

def p_sudo_estatuto(p):
    '''
    sudo_estatuto : aplicaciones
    '''

def p_vars_cte(p):
    '''
    vars_cte : spec_func
            | ID LEFTBRACKET mega_exp RIGHTBRACKET LEFTBRACKET mega_exp RIGHTBRACKET
            | ID LEFTBRACKET mega_exp RIGHTBRACKET
            | ID LEFTPARENTHESIS params RIGHTPARENTHESIS
            | ID
            | CTEI
            | CTEF
            | CTES 
            | CTEB
    '''

def p_params(p):
    '''
    params : paramsaux
            | empty
    '''
def p_paramsaux(p):
    '''
    paramsaux : mega_exp COMMA paramsaux
                | mega_exp
    '''

def p_asignacion(p):
    '''
    asignacion : ID LEFTBRACKET mega_exp RIGHTBRACKET LEFTBRACKET mega_exp RIGHTBRACKET EQUALS mega_exp SEMICOLON
               | ID LEFTBRACKET mega_exp RIGHTBRACKET EQUALS mega_exp SEMICOLON
               | ID EQUALS mega_exp SEMICOLON
    '''

def p_escritura(p):
    '''
    escritura : PRINT LEFTPARENTHESIS escrito RIGHTPARENTHESIS SEMICOLON
    '''
def p_escrito(p):
    '''
    escrito : mega_exp PLUS escrito
            | mega_exp
    '''
def p_lectura(p):
    '''
    lectura : READ LEFTPARENTHESIS ID LEFTBRACKET mega_exp RIGHTBRACKET LEFTBRACKET mega_exp RIGHTBRACKET RIGHTPARENTHESIS SEMICOLON
            | READ LEFTPARENTHESIS ID LEFTBRACKET mega_exp RIGHTBRACKET RIGHTPARENTHESIS SEMICOLON
            | READ LEFTPARENTHESIS ID RIGHTPARENTHESIS SEMICOLON
    '''

def p_llama_spec_func(p):
    '''
    llama_spec_func : spec_func SEMICOLON
    '''

def p_spec_func(p):
    '''
    spec_func : SQRT LEFTPARENTHESIS mega_exp RIGHTPARENTHESIS 
                | POW LEFTPARENTHESIS mega_exp COMMA mega_exp RIGHTPARENTHESIS 
                | ABS LEFTPARENTHESIS mega_exp RIGHTPARENTHESIS 
                | STDEV LEFTPARENTHESIS mega_exp RIGHTPARENTHESIS 
                | MEAN LEFTPARENTHESIS mega_exp RIGHTPARENTHESIS 
                | MEDIAN LEFTPARENTHESIS mega_exp RIGHTPARENTHESIS 
                | MODE LEFTPARENTHESIS mega_exp RIGHTPARENTHESIS 
                | FACTORIAL LEFTPARENTHESIS mega_exp RIGHTPARENTHESIS 
                | SORT LEFTPARENTHESIS mega_exp RIGHTPARENTHESIS 
                | SIN LEFTPARENTHESIS mega_exp RIGHTPARENTHESIS 
                | COS LEFTPARENTHESIS mega_exp RIGHTPARENTHESIS 
                | TRANSPOSE LEFTPARENTHESIS mega_exp RIGHTPARENTHESIS 
                | EXPORTCSV LEFTPARENTHESIS mega_exp COMMA mega_exp RIGHTPARENTHESIS 
                | ARRANGE LEFTPARENTHESIS mega_exp COMMA mega_exp COMMA mega_exp RIGHTPARENTHESIS 
    '''

def p_llama_func(p):
    '''
    llama_func : ID LEFTPARENTHESIS params RIGHTPARENTHESIS SEMICOLON
    '''
########################
# Nombres de funciones #
########################

"""
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

"""



def p_empty(p):
	'''
    empty :
    ''' 

def p_error(p):
    print ("Error de compilacion")

parser = yacc.yacc() 

#Cambiar el nombre del archivo de entrada para probar el codigo
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
