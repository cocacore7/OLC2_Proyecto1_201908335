tokens = (
    'ENTERO',
    'DECIMAL',
    'STRING',
    'VERDADERO',
    'FALSO',
    'CHAR',
    'NULO',
    
    'MAS',
    'MENOS',
    'MULTIPLICACION',
    'DIVISION',
    'POTENCIA',
    'MODULO',

    'MAYOR',
    'MENOR',
    'IGUAL',
    'MAYORIGUAL',
    'MENORIGUAL',
    'DISTINTO',

    'PRINT',
    'PRINTLN',

    'PARIZQ',
    'PARDER',
    'PTCOMA'
)

#Tokens
t_VERDADERO         = r'true'
t_FALSO             = r'false'
t_NULO              = r'null'

t_MAS               = r'\+'
t_MENOS             = r'-'
t_MULTIPLICACION    = r'\*'
t_DIVISION          = r'/'
t_POTENCIA          = r'\^'
t_MODULO            = r'%'

t_MAYOR             = r'>'
t_MENOR             = r'<'
t_IGUAL             = r'=='
t_MAYORIGUAL        = r'>='
t_MENORIGUAL        = r'<='
t_DISTINTO          = r'!='

t_PRINT             = r'print'
t_PRINTLN           = r'println'

t_PARIZQ            = r'\('
t_PARDER            = r'\)'
t_PTCOMA            = r'\;'

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Floaat value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_STRING(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

def t_CHAR(t):
    r'\'.*?\''
    t.value = t.value[1:-1]
    return t

#Caracteres ignorados
t_ignore = " \t\n\r"

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Construyendo el analizador léxico
from Environment.Environment import Environment
from Instruction.Print import Print
from Expression.Primitive import Primitive
from Expression.Arithmetic import Arithmetic
from Expression.Relational import Relational
from Enum.arithmeticOperation import arithmeticOperation
from Enum.relationalOperation import relationalOperation
from Enum.typeExpression import typeExpression
import Analyzer.ply.lex as lex
lexer = lex.lex()

# Asociación de operadores y precedencia
precedence = (
    ('left', 'IGUAL','DISTINTO'),
    ('left', 'MAYOR', 'MENOR','MAYORIGUAL','MENORIGUAL'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'MULTIPLICACION', 'DIVISION'),
    ('left', 'POTENCIA', 'MODULO'),
)

# Definición de la gramática========================
def p_initial(t):
    '''initial : instructions'''
    globalEnv = Environment(None)
    for ins in t[1]:
        ins.execute(globalEnv)

#====================================================
def p_instructions(t):
    '''instructions : instructions instruction
                    | instruction
    '''
    if(len(t) == 3):
        t[1].append(t[2])
        t[0] = t[1]
    elif(len(t) == 2):
        t[0] = [t[1]]

#====================================================
def p_instruction(t):
    '''instruction : p_print 
    '''
    t[0] = t[1]

#====================================================
def p_print(t):
    '''p_print : PRINT PARIZQ exp PARDER PTCOMA
    '''
    t[0] = Print(t[3])

# ====================================================
def p_exp_aritmetica(t):
    '''exp  : exp MAS exp
            | exp MENOS exp
            | exp MULTIPLICACION exp
            | exp DIVISION exp
            | exp POTENCIA exp
            | exp MODULO exp
            | exp MAYOR exp
            | exp MENOR exp
            | exp IGUAL exp
            | exp MAYORIGUAL exp
            | exp MENORIGUAL exp
            | exp DISTINTO exp
    '''
    if t[2] == '+':
        t[0] = Arithmetic(t[1], t[3], arithmeticOperation.PLUS)
    elif t[2] == '-':
        t[0] = Arithmetic(t[1], t[3], arithmeticOperation.MINUS)
    elif t[2] == '*':
        t[0] = Arithmetic(t[1], t[3], arithmeticOperation.MULTIPLY)
    elif t[2] == '/':
        t[0] = Arithmetic(t[1], t[3], arithmeticOperation.DIV)
    elif t[2] == '^':
        t[0] = Arithmetic(t[1], t[3], arithmeticOperation.POT)
    elif t[2] == '%':
        t[0] = Arithmetic(t[1], t[3], arithmeticOperation.MOD)
    elif t[2] == '>':
        t[0] = Relational(t[1], t[3], relationalOperation.MAYOR)
    elif t[2] == '<':
        t[0] = Relational(t[1], t[3], relationalOperation.MENOR)
    elif t[2] == '==':
        t[0] = Relational(t[1], t[3], relationalOperation.IGUAL)
    elif t[2] == '>=':
        t[0] = Relational(t[1], t[3], relationalOperation.MAYORIGUAL)
    elif t[2] == '<=':
        t[0] = Relational(t[1], t[3], relationalOperation.MENORIGUAL)
    elif t[2] == '!=':
        t[0] = Relational(t[1], t[3], relationalOperation.DISTINTO)


#====================================================
def p_exp_agrupacion(t):
    'exp : PARIZQ exp PARDER'
    t[0] = t[2]


#====================================================
def p_exp_valor_entero(t):
    '''exp  : ENTERO
    '''
    t[0] = Primitive(t[1],typeExpression.INTEGER)


#====================================================
def p_exp_valor_decimal(t):
    '''exp  : DECIMAL
    '''
    t[0] = Primitive(t[1],typeExpression.FLOAT)


#====================================================
def p_exp_valor_string(t):
    '''exp  : STRING
    '''
    t[0] = Primitive(t[1],typeExpression.STRING)


#====================================================
def p_exp_valor_char(t):
    '''exp  : CHAR
    '''
    t[0] = Primitive(t[1], typeExpression.CHAR)


#====================================================
def p_exp_valor_verdadero(t):
    '''exp  : VERDADERO
    '''
    t[0] = Primitive(t[1], typeExpression.BOOL)


#====================================================
def p_exp_valor_falso(t):
    '''exp  : FALSO
    '''
    t[0] = Primitive(t[1], typeExpression.BOOL)


#====================================================
def p_exp_valor_nulo(t):
    '''exp  : NULO
    '''
    t[0] = Primitive(t[1], typeExpression.NULO)


#====================================================
def p_error(t):
    print("Error sintáctico en '%s'" % t.value)


import Analyzer.ply.yacc as yacc
parser = yacc.yacc()