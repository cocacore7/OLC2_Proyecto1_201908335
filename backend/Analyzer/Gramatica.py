reservadas = {
    'let' : 'LET',
    
    'true' : 'VERDADERO',
    'false' : 'FALSO',
    'nothing' : 'NULO',

    'int' : 'RINT',
    'float' : 'RFLOAT',
    'string' : 'RSTRING',
    'char' : 'RCHAR',
    'bool' : 'RBOOL',

    'print' : 'PRINT',
    'println' : 'PRINTLN',
    
    'function' : 'FUNCTION',
    
    'while' : 'RWHILE',
    'if' : 'RIF',
    'else' : 'RELSE'
}

tokens = [
    'ENTERO',
    'DECIMAL',
    'STRING',
    'CHAR',
    'ID',
    
    'MAS',
    'MENOS',
    'MULTIPLICACION',
    'DIVISION',
    'POTENCIA',
    'MODULO',

    'MAYOR',
    'MENOR',
    'IGUALIGUAL',
    'MAYORIGUAL',
    'MENORIGUAL',
    'DISTINTO',

    'ANDD',
    'ORR',
    'NOTT',

    'PARIZQ',
    'PARDER',
    'COMA',
    'IGUAL',
    'DOSPT',
    'LLAVEIZQ',
    'LLAVEDER',
    'CORDER',
    'CORIZQ',
    'PTCOMA'
] + list(reservadas.values())

#Tokens
t_MAS               = r'\+'
t_MENOS             = r'-'
t_MULTIPLICACION    = r'\*'
t_DIVISION          = r'/'
t_POTENCIA          = r'\^'
t_MODULO            = r'%'

t_MAYOR             = r'>'
t_MENOR             = r'<'
t_IGUALIGUAL        = r'=='
t_MAYORIGUAL        = r'>='
t_MENORIGUAL        = r'<='
t_DISTINTO          = r'!='


t_ANDD              = r'\|\|'
t_ORR               = r'&&'
t_NOTT              = r'!'

t_PARIZQ            = r'\('
t_PARDER            = r'\)'
t_LLAVEIZQ          = r'\{'
t_LLAVEDER          = r'\}'
t_CORIZQ            = r'\['
t_CORDER            = r'\]'
t_IGUAL             = r'='
t_DOSPT             = r':'
t_PTCOMA            = r'\;'
t_COMA              = r'\,'

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

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID') 
     return t

#Caracteres ignorados
t_ignore = " \t\r\n"

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)



# Construyendo el analizador léxico
from Enum.arithmeticOperation import arithmeticOperation
from Enum.relationalOperation import relationalOperation
from Enum.LogicOperation import logicOperation
from Enum.typeExpression import typeExpression

from Environment.Environment import Environment

from Expression.Primitive import Primitive
from Expression.Arithmetic import Arithmetic
from Expression.Relational import Relational
from Expression.Logic import Logic
from Expression.VariableCall import VariableCall
from Expression.Array import Array
from Expression.ArrayCall import ArrayCall

from Instruction.Print import Print
from Instruction.Print import Println

from Instruction.Declaration import Declaration
from Instruction.Assignment import Assignment

from Instruction.Function import Function
from Instruction.Parameter import Parameter
from Instruction.CallFuncSt import CallFuncSt
from Instruction.Block import Block

from Instruction.If import If
from Instruction.While import While

import Analyzer.ply.lex as lex
lexer = lex.lex()

# Asociación de operadores y precedencia
precedence = (
    ('left', 'ANDD'),
    ('left', 'ORR'),
    ('left','NOTT'),
    ('left', 'IGUAL','DISTINTO'),
    ('left', 'MAYOR', 'MENOR','MAYORIGUAL','MENORIGUAL'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'MULTIPLICACION', 'DIVISION','MODULO'),
    ('left', 'POTENCIA'),
)

#================================Definición de la gramática
def p_initial(t):
    '''initial : instructions'''
    globalEnv = Environment(None)
    for ins in t[1]:
        ins.execute(globalEnv)

#================================LISTA DE INSTRUCCIONES
def p_instructions(t):
    '''instructions : instructions instruction
                    | instruction
    '''
    if(len(t) == 3):
        t[1].append(t[2])
        t[0] = t[1]
    elif(len(t) == 2):
        t[0] = [t[1]]

#================================INSTRUCCIONES
def p_instruction(t):
    '''instruction  : p_print 
                    | p_println
                    | declaration
                    | assignment
                    | function
                    | callFuncSt
                    | whileSt
                    | ifSt
    '''
    t[0] = t[1]

def p_empty(t):
     'empty :'
     pass

#================================INSTRUCCIONES IMPRIMIR
def p_print(t):
    '''p_print : PRINT PARIZQ exp PARDER PTCOMA
    '''
    t[0] = Print(t[3])

def p_println(t):
    '''p_println : PRINTLN PARIZQ exp PARDER PTCOMA
    '''
    t[0] = Println(t[3])

#================================DECLARACION Y ASIGNACION
def p_declaration(t):
    '''declaration  : LET ID DOSPT typeDef decArray IGUAL exp PTCOMA
    '''
    t[0] = Declaration(t[2],t[4],t[7],t[5])

def p_assignment(t):
    '''assignment   : ID IGUAL exp PTCOMA
    '''
    t[0] = Assignment(t[1],t[3])

#================================FUNCIONES
def p_function(t):
    '''function : FUNCTION ID parametersFunc DOSPT typeDef block
    '''
    t[0] = Function(t[2],t[3],t[5],t[6])

def p_parametersFunc(t):
    '''parametersFunc   : PARIZQ parameters PARDER
                        | PARIZQ PARDER
    '''
    if(len(t) == 4):
        t[0] = t[2]
    elif(len(t) == 3):
        t[0] = []

def p_callFuncSt(t):
    '''callFuncSt   : ID parametersCallFunc PTCOMA
    '''
    t[0] = CallFuncSt(t[1],t[2])

#================================PARAMETROS
def p_parameters(t):
    '''parameters   : parameters COMA parameter
                    | parameter
    '''
    if(len(t) == 4):
        t[1].append(t[3])
        t[0] = t[1]
    elif(len(t) == 2):
        t[0] = [t[1]]

def p_parameter(t):
    '''parameter    : ID DOSPT typeDef
    '''
    t[0] = Parameter(t[1],t[3])

def p_parametersCallFunc(t):
    '''parametersCallFunc   : PARIZQ listValues PARDER
                            | PARIZQ PARDER
    '''
    if(len(t) == 4):
        t[0] = t[2]
    elif(len(t) == 3):
        t[0] = []

#================================BLOQUES DE CODIGO
def p_block(t):
    '''block    : LLAVEIZQ instructions LLAVEDER
                | LLAVEIZQ LLAVEDER
    '''
    if(len(t) == 4):
        t[0] = t[2]
    else:
        t[0] = []

#================================INSTRUCCION WHILE
def p_whileSt(t):
    '''whileSt  : RWHILE PARIZQ exp PARDER block 
    '''
    t[0] = While(t[3],t[5])

#================================INSTRUCCIONES IF
def p_ifSt(t):
    ''' ifSt  : RIF PARIZQ exp PARDER block elseSt
    '''
    t[0] = If(t[3],Block(t[5]),t[6])

def p_elseSt(t):
    '''elseSt   : RELSE block
                | ifSt
    '''
    if(len(t) == 2):
        t[0] = t[2]
    elif(len(t) == 3):
        t[0] = Block(t[2])

#================================ARREGLOS
def p_decArray(t):
    '''decArray : CORIZQ CORDER
                | empty 
    '''
    if(len(t) == 3):
        t[0] = True
    elif(len(t) == 2):
        t[0] = False


#================================LISTAS DE VALORES PARA PARAMETROS DE FUNCION
def p_listValues(t):
    '''listValues   : listValues COMA exp
                    | exp
    '''
    if(len(t) == 4):
        t[1].append(t[3])
        t[0] = t[1]
    elif(len(t) == 2):
        t[0] = [t[1]]

def p_typeDef(t):
    '''typeDef  : RSTRING
                | RINT
                | RFLOAT
                | RBOOL
                | RCHAR
    '''
    if t[1] == 'string' : t[0] = typeExpression.STRING
    elif t[1] == 'int' : t[0] = typeExpression.INTEGER
    elif t[1] == 'float' : t[0] = typeExpression.FLOAT
    elif t[1] == 'bool' : t[0] = typeExpression.BOOL
    elif t[1] == 'char' : t[0] = typeExpression.CHAR

#================================EXPRESIONES ARITMETICAS, LOGICAS Y RELACIONALES
def p_exp_aritmetica(t):
    '''exp  : exp MAS exp
            | exp MENOS exp
            | exp MULTIPLICACION exp
            | exp DIVISION exp
            | exp POTENCIA exp
            | exp MODULO exp
            | exp MAYOR exp
            | exp MENOR exp
            | exp IGUALIGUAL exp
            | exp MAYORIGUAL exp
            | exp MENORIGUAL exp
            | exp DISTINTO exp
            | exp ANDD exp
            | exp ORR exp
            | NOTT exp
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
    elif t[2] == '&&':
        t[0] = Logic(t[1], t[3], logicOperation.AND)
    elif t[2] == '||':
        t[0] = Logic(t[1], t[3], logicOperation.OR)
    elif t[1] == '!':
        t[0] = Logic(t[2], t[2], logicOperation.NOT)


#================================TIPOS DE EXPRESIONES, DATOS Y ARREGLOS
def p_exp_agrupacion(t):
    'exp : PARIZQ exp PARDER'
    t[0] = t[2]

def p_exp_valor_entero(t):
    '''exp  : ENTERO
    '''
    t[0] = Primitive(t[1],typeExpression.INTEGER)

def p_exp_valor_decimal(t):
    '''exp  : DECIMAL
    '''
    t[0] = Primitive(t[1],typeExpression.FLOAT)

def p_exp_valor_string(t):
    '''exp  : STRING
    '''
    t[0] = Primitive(t[1],typeExpression.STRING)

def p_exp_valor_char(t):
    '''exp  : CHAR
    '''
    t[0] = Primitive(t[1], typeExpression.CHAR)

def p_exp_valor_verdadero(t):
    '''exp  : VERDADERO
    '''
    t[0] = Primitive(t[1], typeExpression.BOOL)

def p_exp_valor_falso(t):
    '''exp  : FALSO
    '''
    t[0] = Primitive(t[1], typeExpression.BOOL)

def p_exp_valor_nulo(t):
    '''exp  : NULO
    '''
    t[0] = Primitive(t[1], typeExpression.NULO)

def p_exp_variable(t):
    '''exp  : ID
            | ID listArray
    '''
    if(len(t) == 2):
        t[0] = VariableCall(t[1])
    elif(len(t) == 3):
        t[0] = t[2]
        
def p_exp_array(t):
    'exp : CORIZQ listValues CORDER'
    t[0] = Array(t[2])

def p_list_array(t):
    '''listArray    : listArray  CORIZQ exp CORDER 
                    | CORIZQ exp CORDER
    '''
    if(len(t) == 5):
        t[0] = ArrayCall(t[1],t[3])
    elif(len(t) == 4):
        tempVar = VariableCall(t[-1])
        t[0] = ArrayCall(tempVar,t[2])


#====================================================
def p_error(t):
    print("Error sintáctico en '%s'" % t.value)


import Analyzer.ply.yacc as yacc
parser = yacc.yacc()