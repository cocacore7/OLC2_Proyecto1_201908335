reservadas = {
    '"package"': 'RPACKAGE',
    '"main"': 'RMAIN',
    'import': 'RIMPORT',
    '"fmt"': 'RFMT',
    '"math"': 'RMATH',
    'Mod': 'RMOD',
    'var': 'RVAR',
    'stack': 'RSTACK',
    'heap': 'RHEAP',
    'float64': 'RFLOAT',
    '[30101999]': 'RCANT',
    'func': 'RFUNC',
    'goto': 'RGOTO',
    'if': 'RIF',
    'Printf': 'RPRINTF',
    '-0.000001': 'ROPENA',
    '-0.000002': 'RCLOSEA',
}

tokens = [
             'ENTERO',
             'DECIMAL',
             'ID',

             'MAS',
             'MENOS',
             'MULTIPLICACION',
             'DIVISION',

             'MAYOR',
             'MENOR',
             'IGUALIGUAL',
             'MAYORIGUAL',
             'MENORIGUAL',
             'DISTINTO',
             'IGUAL',

             'PARIZQ',
             'PARDER',
             'LLADER',
             'LLAIZQ',
             'CORDER',
             'CORIZQ',
             'DOSPT',
             'COMA',
             'PUNTO',
             'PTCOMA',

             'PRCHAR',
             'PRINTEGER',
             'PRFLOAT',
         ] + list(reservadas.values())

# Tokens
t_MAS = r'\+'
t_MENOS = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'

t_MAYOR = r'>'
t_MENOR = r'<'
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_IGUALIGUAL = r'=='
t_DISTINTO = r'!='

t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_LLAIZQ = r'\{'
t_LLADER = r'\}'
t_IGUAL = r'='
t_DOSPT = r':'
t_COMA = r'\,'
t_PUNTO = r'\.'
t_PTCOMA = r'\;'

t_PRCHAR = r'"%c"'
t_PRINTEGER = r'"%d"'
t_PRFLOAT = r'"%f"'


def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = t.value
    except ValueError:
        print("Floaat value too large %d", t.value)
        t.value = 0
    return t


def t_ENTERO(t):
    r'\d+'
    try:
        t.value = t.value
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value, 'ID')
    return t


# Caracteres ignorados
t_ignore = " \t\r"
t_ignore_COMMENT = r'//.*'
t_ignore_COMMENTM = r'/\*(.|\n)*?\*/'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Error Lexico en Linea: " + str(t.lexer.lineno) + ", Columna:" + str(t.lexer.lexpos))
    t.lexer.skip(1)


# Construyendo el analizador léxico
from Enum.typeExpresionC3D import typeExpression

from OptimizacionC3D.AssignmentC3D import AssignmentC3D
from OptimizacionC3D.GotoC3D import GotoC3D
from OptimizacionC3D.LabelC3D import LabelC3D
from OptimizacionC3D.IfC3D import IfC3D

from OptimizacionC3D.RelationalC3D import RelationalC3D
from OptimizacionC3D.ArithmeticC3D import ArithmeticC3D
from OptimizacionC3D.PrimitiveC3D import PrimitiveC3D

import AnalyzerC3D.ply.lex as lex

lexer = lex.lex()

# Asociación de operadores y precedencia
precedence = (
    ('left', 'IGUALIGUAL', 'DISTINTO', 'MAYOR', 'MENOR', 'MAYORIGUAL', 'MENORIGUAL'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'MULTIPLICACION', 'DIVISION'),
    ('right', 'UMENOS')
)


# ================================Definición de la gramática
def p_initial(t):
    '''initial : instructions'''
    t[0] = t[1]


def p_instructions(t):
    '''instructions : instructions instruction
                    | instruction
    '''
    if len(t) == 3:
        t[1].append(t[2])
        t[0] = t[1]
    elif len(t) == 2:
        t[0] = [t[1]]


# ================================INSTRUCCIONES
def p_instruction(t):
    '''instruction  : assignment
                    | gotoSt
                    | labelSt
                    | ifSt
    '''
    t[0] = t[1]


# ================================INSTRUCCIONES
def p_ifSt(t):
    '''ifSt : RIF exp LLAIZQ gotoSt LLADER
    '''
    t[0] = IfC3D(t[2], t[4], str(t.lexer.lineno))


def p_assignment(t):
    '''assignment   : ID IGUAL exp PTCOMA
    '''
    t[0] = AssignmentC3D(t[1], t[3], str(t.lexer.lineno))


def p_gotoSt(t):
    '''gotoSt : RGOTO ID PTCOMA
    '''
    t[0] = GotoC3D(t[2], str(t.lexer.lineno))


def p_labelSt(t):
    '''labelSt : ID DOSPT
    '''
    t[0] = LabelC3D(t[1], str(t.lexer.lineno))


# ================================EXPRESIONES ARITMETICAS, LOGICAS Y RELACIONALES
def p_exp_aritmetica(t):
    '''exp  : exp MAS exp
            | exp MENOS exp
            | exp MULTIPLICACION exp
            | exp DIVISION exp
            | RMATH PUNTO RMOD PARIZQ exp COMA exp PARDER
            | MENOS exp %prec UMENOS
    '''
    if t[2] == '+':
        t[0] = ArithmeticC3D(t[1], t[3], typeExpression.PLUS)
    elif t[2] == '-':
        t[0] = ArithmeticC3D(t[1], t[3], typeExpression.MINUS)
    elif t[2] == '*':
        t[0] = ArithmeticC3D(t[1], t[3], typeExpression.MULTIPLY)
    elif t[2] == '/':
        t[0] = ArithmeticC3D(t[1], t[3], typeExpression.DIV)
    elif t[1] == '-':
        t[0] = ArithmeticC3D(t[2], None, typeExpression.NEG)
    elif t[1] == 'math' and t[3] == 'Mod':
        t[0] = ArithmeticC3D(t[5], t[7], typeExpression.MOD)


def p_exp_relacional(t):
    '''exp  : exp IGUALIGUAL exp
            | exp DISTINTO exp
            | exp MAYOR exp
            | exp MENOR exp
            | exp MAYORIGUAL exp
            | exp MENORIGUAL exp
    '''
    if t[2] == '==':
        t[0] = RelationalC3D(t[1], t[3], typeExpression.IGUAL)
    elif t[2] == '!=':
        t[0] = RelationalC3D(t[1], t[3], typeExpression.DISTINTO)
    elif t[2] == '>':
        t[0] = RelationalC3D(t[1], t[3], typeExpression.MAYOR)
    elif t[2] == '<':
        t[0] = RelationalC3D(t[1], t[3], typeExpression.MENOR)
    elif t[2] == '>=':
        t[0] = RelationalC3D(t[1], t[3], typeExpression.MAYORIGUAL)
    elif t[2] == '<=':
        t[0] = RelationalC3D(t[1], t[3], typeExpression.MENORIGUAL)


def p_exp_variable(t):
    '''exp  : ID
    '''
    t[0] = PrimitiveC3D(t[1])


def p_exp_valor_entero(t):
    '''exp  : ENTERO
    '''
    t[0] = PrimitiveC3D(t[1])


def p_exp_valor_decimal(t):
    '''exp  : DECIMAL
    '''
    t[0] = PrimitiveC3D(t[1])


# ====================================================
def p_error(t):
    print("Error Sintactico en Linea: " + str(t.lexer.lineno) + ", Columna:" + str(t.lexer.lexpos))
    pass


import AnalyzerC3D.ply.yacc as yacc

parser2 = yacc.yacc()
