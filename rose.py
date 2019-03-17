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
    #print("Salto de linea " + str(lexer.lineno) )
    t.lexer.lineno += 1
    return t

def t_COMENTARIO(t): 
    r'(\/\/.*)'
    #print("commentario en " + str(t.lexer.lineno) + ": " + str(t.value))
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
lexer.input('program test; globals int arbol = 3; func void myfunk(int ola;){ } main (){ int arbol = 5; if(arbol>6){print(arbol);}else{ print(arbol);};}')

while True:
    tok = lexer.token()
    if not tok:
        break
    print (tok)
"""

def p_rose(p):
    '''
    rose : comments_nl PROGRAM comments_nl ID comments_nl SEMICOLON comments_nl roseauxvars comments_nl roseauxfunc comments_nl main comments_nl
    '''
    print("Exito. # salto de linea: " + str(lexer.lineno))

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
    main : MAIN comments_nl LEFTPARENTHESIS comments_nl RIGHTPARENTHESIS comments_nl bloque comments_nl
    '''

def p_vars(p):
    '''
    vars : tipo comments_nl ID comments_nl LEFTBRACKET comments_nl CTEI comments_nl RIGHTBRACKET comments_nl LEFTBRACKET comments_nl CTEI comments_nl RIGHTBRACKET comments_nl EQUALS comments_nl LEFTKEY comments_nl asignacionmatriz comments_nl  RIGHTKEY comments_nl SEMICOLON comments_nl
        | tipo comments_nl ID comments_nl LEFTBRACKET comments_nl CTEI comments_nl RIGHTBRACKET comments_nl LEFTBRACKET comments_nl CTEI comments_nl RIGHTBRACKET comments_nl SEMICOLON comments_nl
        | tipo comments_nl ID comments_nl LEFTBRACKET comments_nl CTEI comments_nl RIGHTBRACKET comments_nl EQUALS comments_nl LEFTKEY comments_nl asignacionarreglo comments_nl RIGHTKEY comments_nl SEMICOLON comments_nl
        | tipo comments_nl ID comments_nl LEFTBRACKET comments_nl CTEI comments_nl RIGHTBRACKET comments_nl SEMICOLON comments_nl
        | tipo comments_nl ID comments_nl EQUALS comments_nl ctes comments_nl SEMICOLON comments_nl
        | tipo comments_nl ID comments_nl SEMICOLON comments_nl
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
    tipo : INT comments_nl
        | FLOAT comments_nl
        | STRING comments_nl
        | BOOL comments_nl
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
    expaux : PLUS comments_nl termino comments_nl expaux comments_nl
            | MINUS comments_nl termino comments_nl expaux comments_nl
            | empty 
    '''

def p_termino(p):
    '''
    termino : factor comments_nl terminoaux comments_nl
    '''

def p_terminoaux(p):
    '''
    terminoaux : DIVIDE comments_nl factor comments_nl terminoaux comments_nl
                | MULTIPLY comments_nl factor comments_nl terminoaux comments_nl
                | empty
    '''

def p_factor(p):
    '''
    factor : PLUS comments_nl vars_cte comments_nl
            | MINUS comments_nl vars_cte comments_nl
            | vars_cte comments_nl
            | LEFTPARENTHESIS comments_nl mega_exp comments_nl RIGHTPARENTHESIS comments_nl
    '''

def p_func(p):
    '''
    func : FUNC comments_nl VOID comments_nl restofuncion comments_nl
        | FUNC comments_nl tipo comments_nl restofuncion comments_nl
    '''

def p_restofuncion(p):
    '''
    restofuncion : ID comments_nl LEFTPARENTHESIS comments_nl argumentos comments_nl RIGHTPARENTHESIS comments_nl bloque comments_nl
    '''

def p_argumentos(p):
    '''
    argumentos : tipo comments_nl mismotipo comments_nl SEMICOLON comments_nl argumentos comments_nl
                | empty
    '''

def p_mismotipo(p):
    '''
    mismotipo : ID comments_nl LEFTBRACKET comments_nl CTEI comments_nl RIGHTBRACKET comments_nl LEFTBRACKET comments_nl CTEI comments_nl RIGHTBRACKET comments_nl COMMA comments_nl mismotipo comments_nl
                | ID comments_nl LEFTBRACKET comments_nl CTEI comments_nl RIGHTBRACKET comments_nl COMMA comments_nl mismotipo comments_nl
                | ID comments_nl COMMA comments_nl mismotipo comments_nl
                | ID comments_nl LEFTBRACKET comments_nl CTEI comments_nl RIGHTBRACKET comments_nl LEFTBRACKET comments_nl CTEI comments_nl RIGHTBRACKET comments_nl
                | ID comments_nl LEFTBRACKET comments_nl CTEI comments_nl RIGHTBRACKET comments_nl
                | ID comments_nl  

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
            | ID comments_nl
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
               | ID comments_nl EQUALS comments_nl mega_exp comments_nl SEMICOLON comments_nl
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