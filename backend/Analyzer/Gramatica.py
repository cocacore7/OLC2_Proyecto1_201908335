reservadas = {
    'true': 'VERDADERO',
    'false': 'FALSO',
    'nothing': 'NULO',

    'Int64': 'RINT',
    'Float64': 'RFLOAT',
    'String': 'RSTRING',
    'Char': 'RCHAR',
    'Bool': 'RBOOL',
    'Array{Int64}': 'RINTA',
    'Array{Float64}': 'RFLOATA',
    'Array{String}': 'RSTRINGA',
    'Array{Char}': 'RCHARA',
    'Array{Bool}': 'RBOOLA',
    'Array': 'RARRAY',

    'lowercase': 'LOWERCASE',
    'uppercase': 'UPPERCASE',
    'log10': 'LOG10',
    'log': 'LOG',
    'sin': 'SIN',
    'cos': 'COS',
    'tan': 'TAN',
    'sqrt': 'SQRT',
    'parse': 'PARSE',
    'trunc': 'TRUNC',
    'float': 'MFLOAT',
    'string': 'MSTRING',
    'typeof': 'TYPEOF',
    'push': 'RPUSH',
    'pop': 'RPOP',
    'length': 'RLENGTH',

    'print': 'PRINT',
    'println': 'PRINTLN',

    'function': 'FUNCTION',
    'global': 'GLOBAL',
    'local': 'LOCAL',
    'end': 'END',

    'if': 'RIF',
    'elseif': 'RELSEIF',
    'else': 'RELSE',
    'while': 'RWHILE',
    'for': 'RFOR',
    'in': 'RIN',

    'break': 'RBREAK',
    'continue': 'RCONTINUE',
    'return': 'RRETURN'
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
             'CORDER',
             'CORIZQ',
             'LLADER',
             'LLAIZQ',
             'PTCOMA'
         ] + list(reservadas.values())

# Tokens
t_MAS = r'\+'
t_MENOS = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_POTENCIA = r'\^'
t_MODULO = r'%'

t_MAYOR = r'>'
t_MENOR = r'<'
t_IGUALIGUAL = r'=='
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_DISTINTO = r'!='

t_ANDD = r'\|\|'
t_ORR = r'&&'
t_NOTT = r'!'

t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_LLAIZQ = r'\{'
t_LLADER = r'\}'
t_IGUAL = r'='
t_DOSPT = r':'
t_PTCOMA = r'\;'
t_COMA = r'\,'


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
    t.type = reservadas.get(t.value, 'ID')
    return t


# Caracteres ignorados
t_ignore = " \t\r"
t_ignore_COMMENT = r'\#.*'
t_ignore_COMMENTM = r'\#=(.|\n)*?=\#'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


def t_error(t):
    Errores.append(
        {'Descripcion': "Error Lexico '%s'" % t.value[0], 'Linea': t.lineno, 'Columna': "",
         'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
    t.lexer.skip(1)


# Construyendo el analizador l??xico
from Globales.Tablas import Errores
from datetime import datetime

from Environment.Environment import Environment

from Enum.arithmeticOperation import arithmeticOperation
from Enum.relationalOperation import relationalOperation
from Enum.LogicOperation import logicOperation
from Enum.OperacionVaria import operacionVaria
from Enum.typeExpression import typeExpression
from Enum.TransferSentence import TransferSentence

from Expression.Primitive import Primitive
from Expression.Array import Array
from Expression.Arithmetic import Arithmetic
from Expression.Relational import Relational
from Expression.Logic import Logic
from Expression.FuncionesVarias import FuncionVaria
from Expression.FuncionesVarias2 import FuncionVaria2
from Expression.Push import Push
from Expression.Pop import Pop
from Expression.VariableCall import VariableCall
from Expression.ArrayCall import ArrayCall

from Instruction.Print import Print
from Instruction.Print import Println
from Instruction.Declaration import Declaration
from Instruction.AssignmentArray import AssignmentArray
from Instruction.Function import Function
from Instruction.Parameter import Parameter
from Instruction.CallFuncSt import CallFuncSt
from Instruction.If import If
from Instruction.While import While
from Instruction.For import For
from Instruction.Block import Block
from Instruction.Return import Return
from Instruction.Break import Break
from Instruction.Continue import Continue

import Analyzer.ply.lex as lex

lexer = lex.lex()

# Asociaci??n de operadores y precedencia
precedence = (
    ('left', 'ANDD'),
    ('left', 'ORR'),
    ('right', 'UNOT'),
    ('left', 'IGUALIGUAL', 'DISTINTO', 'MAYOR', 'MENOR', 'MAYORIGUAL', 'MENORIGUAL'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'MULTIPLICACION', 'DIVISION', 'MODULO'),
    ('nonassoc', 'POTENCIA'),
    ('right', 'UMENOS')
)


# ================================Definici??n de la gram??tica
def p_initial(t):
    '''initial : instructions'''
    globalEnv = Environment(None)
    for ins in t[1]:
        temp = ins.execute(globalEnv)
        if temp is not None:
            if temp.type == TransferSentence.RETURN:
                if not temp.funcion:
                    if temp.ciclo:
                        print("No Puede Haber Return En Ciclo Sin Una Funcion")
                    else:
                        print("No Puede Haber Return En Entorno Global")
            elif temp.type == TransferSentence.BREAK:
                print("No Puede Haber Break En Entorno Global")
            elif temp.type == TransferSentence.CONTINUE:
                print("No Puede Haber Continue En Entorno Global")


# ================================LISTA DE INSTRUCCIONES
def p_instructions(t):
    '''instructions : instructions instruction
                    | instruction
    '''
    if len(t) == 3:
        t[1].append(t[2])
        t[0] = t[1]
    elif len(t) == 2:
        t[0] = [t[1]]


def p_instructionsf(t):
    '''instructionsf : instructionsf instructionf
                     | instructionf
    '''
    if (len(t) == 3):
        t[1].append(t[2])
        t[0] = t[1]
    elif (len(t) == 2):
        t[0] = [t[1]]


def p_instructionsc(t):
    '''instructionsc : instructionsc instructionc
                     | instructionc
    '''
    if (len(t) == 3):
        t[1].append(t[2])
        t[0] = t[1]
    elif (len(t) == 2):
        t[0] = [t[1]]


# ================================INSTRUCCIONES
def p_instruction(t):
    '''instruction  : p_print 
                    | p_println
                    | declaration
                    | assignmentA
                    | function
                    | callFuncSt
                    | ifSt
                    | whileSt
                    | forSt
                    | returnST
                    | breakST
                    | continueST
                    | push
                    | pop
    '''
    t[0] = t[1]


def p_instructionf(t):
    '''instructionf : p_print
                    | p_println
                    | declarationf
                    | assignmentAf
                    | callFuncSt
                    | ifSt
                    | whileSt
                    | forSt
                    | returnST
                    | breakST
                    | continueST
                    | push
                    | pop
    '''
    t[0] = t[1]


def p_instructionc(t):
    '''instructionc : p_print
                    | p_println
                    | declarationc
                    | assignmentAc
                    | callFuncSt
                    | ifStc
                    | whileSt
                    | forSt
                    | returnST
                    | breakST
                    | continueST
                    | push
                    | pop
    '''
    t[0] = t[1]


# ================================INSTRUCCIONES IMPRIMIR
def p_print(t):
    '''p_print  : PRINT PARIZQ exps PARDER PTCOMA
                | PRINT PARIZQ PARDER PTCOMA
    '''
    if len(t) == 6:
        t[0] = Print(t[3])
    else:
        t[0] = Print([Primitive("", typeExpression.STRING)])


def p_println(t):
    '''p_println    : PRINTLN PARIZQ exps PARDER PTCOMA
                    | PRINTLN PARIZQ PARDER PTCOMA
    '''
    if len(t) == 6:
        t[0] = Println(t[3])
    else:
        t[0] = Println([Primitive("", typeExpression.STRING)])


def p_expresions(t):
    '''exps     : exps COMA exp
                | exp
    '''
    if len(t) == 4:
        t[1].append(t[3])
        t[0] = t[1]
    elif len(t) == 2:
        t[0] = [t[1]]


# ================================DECLARACIONES Y ASIGNACIONES
def p_declaration(t):
    '''declaration  : ID IGUAL exp PTCOMA
                    | ID IGUAL exp DOSPT DOSPT typeDef PTCOMA
                    | GLOBAL ID IGUAL exp DOSPT DOSPT typeDef PTCOMA
                    | GLOBAL ID IGUAL exp PTCOMA
                    | GLOBAL ID PTCOMA
                    | LOCAL ID IGUAL exp DOSPT DOSPT typeDef PTCOMA
                    | LOCAL ID IGUAL exp PTCOMA
                    | LOCAL ID PTCOMA
                    | ID IGUAL CORIZQ exps CORDER PTCOMA
                    | ID IGUAL CORIZQ exps CORDER DOSPT DOSPT typeDef PTCOMA
                    | GLOBAL ID IGUAL CORIZQ exps CORDER DOSPT DOSPT typeDef PTCOMA
                    | GLOBAL ID IGUAL CORIZQ exps CORDER PTCOMA
                    | LOCAL ID IGUAL CORIZQ exps CORDER DOSPT DOSPT typeDef PTCOMA
                    | LOCAL ID IGUAL CORIZQ exps CORDER PTCOMA
    '''
    if len(t) == 5:
        t[0] = Declaration(t[1], t[3], typeExpression.NULO, False, "N", "N")
    elif len(t) == 8:
        if t[4] == "[":
            t[0] = Declaration(t[2], t[5], typeExpression.ANY, True, "N", "N")
        else:
            t[0] = Declaration(t[1], t[3], t[6], False, "N", "N")
    elif len(t) == 9:
        t[0] = Declaration(t[2], t[4], t[7], False, "N", "N")
    elif len(t) == 6:
        t[0] = Declaration(t[2], t[4], typeExpression.NULO, False, "N", "N")
    elif len(t) == 4:
        t[0] = Declaration(t[2], None, typeExpression.NULO, False, "N", "N")
    elif len(t) == 7:
        t[0] = Declaration(t[1], t[4], typeExpression.ANY, True, "N", "N")
    elif len(t) == 10:
        t[0] = Declaration(t[1], t[4], t[8], True, "N", "N")
    elif len(t) == 11:
        t[0] = Declaration(t[2], t[5], t[9], True, "N", "N")


def p_declarationf(t):
    '''declarationf : ID IGUAL exp PTCOMA
                    | ID IGUAL exp DOSPT DOSPT typeDef PTCOMA
                    | GLOBAL ID IGUAL exp DOSPT DOSPT typeDef PTCOMA
                    | GLOBAL ID IGUAL exp PTCOMA
                    | GLOBAL ID PTCOMA
                    | LOCAL ID IGUAL exp DOSPT DOSPT typeDef PTCOMA
                    | LOCAL ID IGUAL exp PTCOMA
                    | LOCAL ID PTCOMA
                    | ID IGUAL CORIZQ exps CORDER PTCOMA
                    | ID IGUAL CORIZQ exps CORDER DOSPT DOSPT typeDef PTCOMA
                    | GLOBAL ID IGUAL CORIZQ exps CORDER DOSPT DOSPT typeDef PTCOMA
                    | GLOBAL ID IGUAL CORIZQ exps CORDER PTCOMA
                    | LOCAL ID IGUAL CORIZQ exps CORDER DOSPT DOSPT typeDef PTCOMA
                    | LOCAL ID IGUAL CORIZQ exps CORDER PTCOMA
    '''
    if len(t) == 5:
        t[0] = Declaration(t[1], t[3], typeExpression.NULO, False, "L", "F")
    elif len(t) == 8:
        if t[4] == "[":
            if t[1] == "local":
                t[0] = Declaration(t[2], t[5], typeExpression.ANY, True, "L", "F")
            elif t[1] == "global":
                t[0] = Declaration(t[2], t[5], typeExpression.ANY, True, "G", "F")
        else:
            t[0] = Declaration(t[1], t[3], t[6], False, "L", "F")
    elif len(t) == 9:
        if t[1] == "local":
            t[0] = Declaration(t[2], t[4], t[7], False, "L", "F")
        elif t[1] == "global":
            t[0] = Declaration(t[2], t[4], t[7], False, "G", "F")
    elif len(t) == 6:
        if t[1] == "local":
            t[0] = Declaration(t[2], t[4], typeExpression.NULO, False, "L", "F")
        elif t[1] == "global":
            t[0] = Declaration(t[2], t[4], typeExpression.NULO, False, "G", "F")
    elif len(t) == 4:
        if t[1] == "local":
            t[0] = Declaration(t[2], None, typeExpression.NULO, False, "L", "F")
        elif t[1] == "global":
            t[0] = Declaration(t[2], None, typeExpression.NULO, False, "G", "F")
    elif len(t) == 7:
        t[0] = Declaration(t[1], t[4], typeExpression.ANY, True, "L", "F")
    elif len(t) == 10:
        t[0] = Declaration(t[1], t[4], t[8], True, "L", "F")
    elif len(t) == 11:
        if t[1] == "local":
            t[0] = Declaration(t[2], t[5], t[9], True, "L", "F")
        elif t[1] == "global":
            t[0] = Declaration(t[2], t[5], t[9], True, "G", "F")


def p_declarationc(t):
    '''declarationc : ID IGUAL exp PTCOMA
                    | ID IGUAL exp DOSPT DOSPT typeDef PTCOMA
                    | LOCAL ID IGUAL exp DOSPT DOSPT typeDef PTCOMA
                    | LOCAL ID IGUAL exp PTCOMA
                    | LOCAL ID PTCOMA
                    | GLOBAL ID IGUAL exp DOSPT DOSPT typeDef PTCOMA
                    | GLOBAL ID IGUAL exp PTCOMA
                    | GLOBAL ID PTCOMA
                    | ID IGUAL CORIZQ exps CORDER PTCOMA
                    | ID IGUAL CORIZQ exps CORDER DOSPT DOSPT typeDef PTCOMA
                    | GLOBAL ID IGUAL CORIZQ exps CORDER DOSPT DOSPT typeDef PTCOMA
                    | GLOBAL ID IGUAL CORIZQ exps CORDER PTCOMA
                    | LOCAL ID IGUAL CORIZQ exps CORDER DOSPT DOSPT typeDef PTCOMA
                    | LOCAL ID IGUAL CORIZQ exps CORDER PTCOMA
    '''
    if len(t) == 5:
        t[0] = Declaration(t[1], t[3], typeExpression.NULO, False, "G", "C")
    elif len(t) == 8:
        if t[4] == "[":
            if t[1] == "local":
                t[0] = Declaration(t[2], t[5], typeExpression.ANY, True, "L", "C")
            elif t[1] == "global":
                t[0] = Declaration(t[2], t[5], typeExpression.ANY, True, "G", "C")
        else:
            t[0] = Declaration(t[1], t[3], t[6], False, "G", "C")
    elif len(t) == 9:
        if t[1] == "local":
            t[0] = Declaration(t[2], t[4], t[7], False, "L", "C")
        elif t[1] == "global":
            t[0] = Declaration(t[2], t[4], t[7], False, "G", "C")
    elif len(t) == 6:
        if t[1] == "local":
            t[0] = Declaration(t[2], t[4], typeExpression.NULO, False, "L", "C")
        elif t[1] == "global":
            t[0] = Declaration(t[2], t[4], typeExpression.NULO, False, "G", "C")
    elif len(t) == 4:
        if t[1] == "local":
            t[0] = Declaration(t[2], None, typeExpression.NULO, False, "L", "C")
        elif t[1] == "global":
            t[0] = Declaration(t[2], None, typeExpression.NULO, False, "G", "C")
    elif len(t) == 7:
        t[0] = Declaration(t[1], t[4], typeExpression.ANY, True, "G", "C")
    elif len(t) == 10:
        t[0] = Declaration(t[1], t[4], t[8], True, "G", "C")
    elif len(t) == 11:
        if t[1] == "local":
            t[0] = Declaration(t[2], t[5], t[9], True, "L", "C")
        elif t[1] == "global":
            t[0] = Declaration(t[2], t[5], t[9], True, "G", "C")


def p_assignment(t):
    '''assignmentA  : ID listArray2 IGUAL CORIZQ exps CORDER PTCOMA
                    | ID listArray2 IGUAL CORIZQ exps CORDER DOSPT DOSPT typeDef PTCOMA
                    | GLOBAL ID listArray2 IGUAL CORIZQ exps CORDER DOSPT DOSPT typeDef PTCOMA
                    | GLOBAL ID listArray2 IGUAL CORIZQ exps CORDER PTCOMA
                    | LOCAL ID listArray2 IGUAL CORIZQ exps CORDER DOSPT DOSPT typeDef PTCOMA
                    | LOCAL ID listArray2 IGUAL CORIZQ exps CORDER PTCOMA

                    | ID listArray2 IGUAL exp PTCOMA
                    | ID listArray2 IGUAL exp DOSPT DOSPT typeDef PTCOMA
                    | GLOBAL ID listArray2 IGUAL exp DOSPT DOSPT typeDef PTCOMA
                    | GLOBAL ID listArray2 IGUAL exp PTCOMA
                    | LOCAL ID listArray2 IGUAL exp DOSPT DOSPT typeDef PTCOMA
                    | LOCAL ID listArray2 IGUAL exp PTCOMA
    '''
    if len(t) == 8:
        t[0] = AssignmentArray(t[1], VariableCall(t[1]), t[2], t[5], typeExpression.ANY, True, "N", "N")
    elif len(t) == 11:
        t[0] = AssignmentArray(t[1], VariableCall(t[1]), t[2], t[5], t[9], True, "N", "N")
    elif len(t) == 12:
        t[0] = AssignmentArray(t[2], VariableCall(t[2]), t[3], t[6], t[10], True, "N", "N")
    elif len(t) == 9:
        if t[1] == "local":
            t[0] = AssignmentArray(t[2], VariableCall(t[2]), t[3], t[6], typeExpression.ANY, True, "N", "N")
        elif t[1] == "global":
            t[0] = AssignmentArray(t[2], VariableCall(t[2]), t[3], t[6], typeExpression.ANY, True, "N", "N")
        else:
            t[0] = AssignmentArray(t[1], VariableCall(t[1]), t[2], t[4], t[7], False, "N", "N")
    elif len(t) == 6:
        t[0] = AssignmentArray(t[1], VariableCall(t[1]), t[2], t[4], typeExpression.NULO, False, "N", "N")
    elif len(t) == 10:
        t[0] = AssignmentArray(t[2], VariableCall(t[2]), t[3], t[5], t[8], False, "N", "N")
    elif len(t) == 7:
        t[0] = AssignmentArray(t[2], VariableCall(t[2]), t[3], t[5], typeExpression.NULO, False, "N", "N")


def p_assignmentf(t):
    '''assignmentAf : ID listArray2 IGUAL CORIZQ exps CORDER PTCOMA
                    | ID listArray2 IGUAL CORIZQ exps CORDER DOSPT DOSPT typeDef PTCOMA
                    | GLOBAL ID listArray2 IGUAL CORIZQ exps CORDER DOSPT DOSPT typeDef PTCOMA
                    | GLOBAL ID listArray2 IGUAL CORIZQ exps CORDER PTCOMA
                    | LOCAL ID listArray2 IGUAL CORIZQ exps CORDER DOSPT DOSPT typeDef PTCOMA
                    | LOCAL ID listArray2 IGUAL CORIZQ exps CORDER PTCOMA

                    | ID listArray2 IGUAL exp PTCOMA
                    | ID listArray2 IGUAL exp DOSPT DOSPT typeDef PTCOMA
                    | GLOBAL ID listArray2 IGUAL exp DOSPT DOSPT typeDef PTCOMA
                    | GLOBAL ID listArray2 IGUAL exp PTCOMA
                    | LOCAL ID listArray2 IGUAL exp DOSPT DOSPT typeDef PTCOMA
                    | LOCAL ID listArray2 IGUAL exp PTCOMA
    '''
    if len(t) == 8:
        t[0] = AssignmentArray(t[1], VariableCall(t[1]), t[2], t[5], typeExpression.ANY, True, "L", "F")
    elif len(t) == 11:
        t[0] = AssignmentArray(t[1], VariableCall(t[1]), t[2], t[5], t[9], True, "L", "F")
    elif len(t) == 12:
        if t[1] == "local":
            t[0] = AssignmentArray(t[2], VariableCall(t[2]), t[3], t[6], t[10], True, "L", "F")
        else:
            t[0] = AssignmentArray(t[2], VariableCall(t[2]), t[3], t[6], t[10], True, "G", "F")
    elif len(t) == 9:
        if t[1] == "local":
            t[0] = AssignmentArray(t[2], VariableCall(t[2]), t[3], t[6], typeExpression.ANY, True, "L", "F")
        elif t[1] == "global":
            t[0] = AssignmentArray(t[2], VariableCall(t[2]), t[3], t[6], typeExpression.ANY, True, "G", "F")
        else:
            t[0] = AssignmentArray(t[1], VariableCall(t[1]), t[2], t[4], t[7], False, "L", "F")
    elif len(t) == 6:
        t[0] = AssignmentArray(t[1], VariableCall(t[1]), t[2], t[4], typeExpression.NULO, False, "L", "F")
    elif len(t) == 10:
        if t[1] == "local":
            t[0] = AssignmentArray(t[2], VariableCall(t[2]), t[3], t[5], t[8], False, "L", "F")
        else:
            t[0] = AssignmentArray(t[2], VariableCall(t[2]), t[3], t[5], t[8], False, "G", "F")
    elif len(t) == 7:
        if t[1] == "local":
            t[0] = AssignmentArray(t[2], VariableCall(t[2]), t[3], t[5], typeExpression.NULO, False, "L", "F")
        else:
            t[0] = AssignmentArray(t[2], VariableCall(t[2]), t[3], t[5], typeExpression.NULO, False, "G", "F")


def p_assignmentc(t):
    '''assignmentAc : ID listArray2 IGUAL CORIZQ exps CORDER PTCOMA
                    | ID listArray2 IGUAL CORIZQ exps CORDER DOSPT DOSPT typeDef PTCOMA
                    | GLOBAL ID listArray2 IGUAL CORIZQ exps CORDER DOSPT DOSPT typeDef PTCOMA
                    | GLOBAL ID listArray2 IGUAL CORIZQ exps CORDER PTCOMA
                    | LOCAL ID listArray2 IGUAL CORIZQ exps CORDER DOSPT DOSPT typeDef PTCOMA
                    | LOCAL ID listArray2 IGUAL CORIZQ exps CORDER PTCOMA

                    | ID listArray2 IGUAL exp PTCOMA
                    | ID listArray2 IGUAL exp DOSPT DOSPT typeDef PTCOMA
                    | GLOBAL ID listArray2 IGUAL exp DOSPT DOSPT typeDef PTCOMA
                    | GLOBAL ID listArray2 IGUAL exp PTCOMA
                    | LOCAL ID listArray2 IGUAL exp DOSPT DOSPT typeDef PTCOMA
                    | LOCAL ID listArray2 IGUAL exp PTCOMA
    '''
    if len(t) == 8:
        t[0] = AssignmentArray(t[1], VariableCall(t[1]), t[2], t[5], typeExpression.ANY, True, "G", "C")
    elif len(t) == 11:
        t[0] = AssignmentArray(t[1], VariableCall(t[1]), t[2], t[5], t[9], True, "G", "C")
    elif len(t) == 12:
        if t[1] == "local":
            t[0] = AssignmentArray(t[2], VariableCall(t[2]), t[3], t[6], t[10], True, "L", "C")
        else:
            t[0] = AssignmentArray(t[2], VariableCall(t[2]), t[3], t[6], t[10], True, "G", "C")
    elif len(t) == 9:
        if t[1] == "local":
            t[0] = AssignmentArray(t[2], VariableCall(t[2]), t[3], t[6], typeExpression.ANY, True, "L", "C")
        elif t[1] == "global":
            t[0] = AssignmentArray(t[2], VariableCall(t[2]), t[3], t[6], typeExpression.ANY, True, "G", "C")
        else:
            t[0] = AssignmentArray(t[1], VariableCall(t[1]), t[2], t[4], t[7], False, "G", "C")
    elif len(t) == 6:
        t[0] = AssignmentArray(t[1], VariableCall(t[1]), t[2], t[4], typeExpression.NULO, False, "G", "C")
    elif len(t) == 10:
        if t[1] == "local":
            t[0] = AssignmentArray(t[2], VariableCall(t[2]), t[3], t[5], t[8], False, "L", "C")
        else:
            t[0] = AssignmentArray(t[2], VariableCall(t[2]), t[3], t[5], t[8], False, "G", "C")
    elif len(t) == 7:
        if t[1] == "local":
            t[0] = AssignmentArray(t[2], VariableCall(t[2]), t[3], t[5], typeExpression.NULO, False, "L", "C")
        else:
            t[0] = AssignmentArray(t[2], VariableCall(t[2]), t[3], t[5], typeExpression.NULO, False, "G", "C")


# ================================FUNCIONES
def p_function(t):
    '''function : FUNCTION ID parametersFunc blockf
    '''
    t[0] = Function(t[2], t[3], t[4])


def p_parametersFunc(t):
    '''parametersFunc   : PARIZQ parameters PARDER
                        | PARIZQ PARDER
    '''
    if len(t) == 4:
        t[0] = t[2]
    elif len(t) == 3:
        t[0] = []


def p_parameters(t):
    '''parameters   : parameters COMA parameter
                    | parameter
    '''
    if len(t) == 4:
        t[1].append(t[3])
        t[0] = t[1]
    elif len(t) == 2:
        t[0] = [t[1]]


def p_parameter(t):
    '''parameter    : ID DOSPT DOSPT typeDef
                    | ID
    '''
    if len(t) == 5:
        t[0] = Parameter(t[1], t[4])
    elif len(t) == 2:
        t[0] = Parameter(t[1], None)


# ================================LLAMADA A FUNCIONES
def p_callFuncSt(t):
    '''callFuncSt   : ID parametersCallFunc PTCOMA
    '''
    t[0] = CallFuncSt(t[1], t[2])


def p_parametersCallFunc(t):
    '''parametersCallFunc   : PARIZQ listValues PARDER
                            | PARIZQ PARDER
    '''
    if len(t) == 4:
        t[0] = t[2]
    elif len(t) == 3:
        t[0] = []


def p_listValues(t):
    '''listValues   : listValues COMA exp
                    | exp
    '''
    if len(t) == 4:
        t[1].append(t[3])
        t[0] = t[1]
    elif len(t) == 2:
        t[0] = [t[1]]


# ================================CONDICIONAL IF
def p_ifSt(t):
    ''' ifSt    : RIF exp END PTCOMA
                | RIF exp blockiff END PTCOMA
                | RIF exp blockiff RELSE blockiff END PTCOMA
                | RIF exp blockiff RELSE END PTCOMA
                | RIF exp blockiff elseifSt END PTCOMA
                | RIF exp blockiff elseifSt RELSE blockiff END PTCOMA
                | RIF exp blockiff elseifSt RELSE END PTCOMA
    '''
    if len(t) == 5:
        t[0] = If(t[2], Block([]), [], Block([]))
    elif len(t) == 6:
        t[0] = If(t[2], Block(t[3]), [], Block([]))
    elif len(t) == 8:
        if t[4] == 'else':
            t[0] = If(t[2], Block(t[3]), [], Block(t[5]))
        elif t[5] == 'else':
            t[0] = If(t[2], Block(t[3]), t[4], Block([]))
    elif len(t) == 7:
        if t[4] == 'else':
            t[0] = If(t[2], Block(t[3]), [], Block([]))
        elif t[5] == 'end':
            t[0] = If(t[2], Block(t[3]), t[4], Block([]))
    elif len(t) == 9:
        t[0] = If(t[2], Block(t[3]), t[4], Block(t[6]))


def p_elseifSt(t):
    '''elseifSt : elseifSt conelseif
    '''
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]


def p_elseifSt_2(t):
    '''elseifSt : conelseif
    '''
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]


def p_conelseift(t):
    '''conelseif    : RELSEIF exp blockiff
                    | RELSEIF exp
    '''
    if len(t) == 3:
        t[0] = If(t[2], Block([]), Block([]), Block([]))
    elif len(t) == 4:
        t[0] = If(t[2], Block(t[3]), Block([]), Block([]))


def p_ifStc(t):
    ''' ifStc    : RIF exp END PTCOMA
                | RIF exp blockifc END PTCOMA
                | RIF exp blockifc RELSE blockifc END PTCOMA
                | RIF exp blockifc RELSE END PTCOMA
                | RIF exp blockifc elseifStc END PTCOMA
                | RIF exp blockifc elseifStc RELSE blockifc END PTCOMA
                | RIF exp blockifc elseifStc RELSE END PTCOMA
    '''
    if len(t) == 5:
        t[0] = If(t[2], Block([]), [], Block([]))
    elif len(t) == 6:
        t[0] = If(t[2], Block(t[3]), [], Block([]))
    elif len(t) == 8:
        if t[4] == 'else':
            t[0] = If(t[2], Block(t[3]), [], Block(t[5]))
        elif t[5] == 'else':
            t[0] = If(t[2], Block(t[3]), t[4], Block([]))
    elif len(t) == 7:
        if t[4] == 'else':
            t[0] = If(t[2], Block(t[3]), [], Block([]))
        elif t[5] == 'end':
            t[0] = If(t[2], Block(t[3]), t[4], Block([]))
    elif len(t) == 9:
        t[0] = If(t[2], Block(t[3]), t[4], Block(t[6]))


def p_elseifStc(t):
    '''elseifStc : elseifStc conelseifc
    '''
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]


def p_elseifStc_2(t):
    '''elseifStc : conelseifc
    '''
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]


def p_conelseiftc(t):
    '''conelseifc    : RELSEIF exp blockifc
                     | RELSEIF exp
    '''
    if len(t) == 3:
        t[0] = If(t[2], Block([]), Block([]), Block([]))
    elif len(t) == 4:
        t[0] = If(t[2], Block(t[3]), Block([]), Block([]))


# ================================CICLO WHILE
def p_whileSt(t):
    '''whileSt  : RWHILE exp blockc
    '''
    t[0] = While(t[2], t[3])


# ================================CICLO FOR
def p_forSt(t):
    '''forSt    : RFOR parameter RIN exp DOSPT exp blockc
                | RFOR parameter RIN exp blockc
    '''
    if len(t) == 8:
        t[0] = For(t[2], t[4], t[6], t[7])
    elif len(t) == 6:
        t[0] = For(t[2], t[4], Primitive('nothing', typeExpression.NULO), t[5])


# ================================BLOQUES DE CODIGO
def p_blockf(t):
    '''blockf   : instructionsf END PTCOMA
                | END PTCOMA
    '''
    if len(t) == 4:
        t[0] = t[1]
    else:
        t[0] = []


def p_blockc(t):
    '''blockc   : instructionsc END PTCOMA
                | END PTCOMA
    '''
    if len(t) == 4:
        t[0] = t[1]
    else:
        t[0] = []


def p_blockiff(t):
    '''blockiff  : instructionsf
    '''
    t[0] = t[1]


def p_blockifc(t):
    '''blockifc  : instructionsc
    '''
    t[0] = t[1]


# ================================SENTENCIAS DE TRANSFERENCIA
def p_return(t):
    '''returnST : RRETURN exp PTCOMA
                | RRETURN PTCOMA
    '''
    if len(t) == 4:
        t[0] = Return(TransferSentence.RETURN, t[2])
    else:
        t[0] = Return(TransferSentence.RETURN, Primitive('nothing', typeExpression.NULO))


def p_break(t):
    '''breakST  : RBREAK PTCOMA
    '''
    t[0] = Break(TransferSentence.BREAK)


def p_continue(t):
    '''continueST  : RCONTINUE PTCOMA
    '''
    t[0] = Continue(TransferSentence.CONTINUE)


# ================================ARREGLOS
def p_list_array(t):
    '''listArray    : listArray  CORIZQ exp CORDER
                    | CORIZQ exp CORDER
    '''
    if len(t) == 5:
        t[0] = ArrayCall(t[1], t[3])
    elif len(t) == 4:
        tempVar = VariableCall(t[-1])
        t[0] = ArrayCall(tempVar, t[2])


def p_list_array2(t):
    '''listArray2   : listArray2  CORIZQ exp CORDER
                    | CORIZQ exp CORDER
    '''
    if len(t) == 5:
        t[1].append(t[3])
        t[0] = t[1]
    elif len(t) == 4:
        t[0] = [t[2]]


# ================================EXPRESIONES ARITMETICAS, LOGICAS Y RELACIONALES
def p_exp_aritmetica(t):
    '''exp  : exp MAS exp
            | exp MENOS exp
            | exp MULTIPLICACION exp
            | exp DIVISION exp
            | exp POTENCIA exp
            | exp MODULO exp
            | MENOS exp %prec UMENOS
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
    elif t[1] == '-':
        t[0] = Arithmetic(t[2], t[2], arithmeticOperation.NEG)


def p_exp_relacional(t):
    '''exp  : exp IGUALIGUAL exp
            | exp DISTINTO exp
            | exp MAYOR exp
            | exp MENOR exp
            | exp MAYORIGUAL exp
            | exp MENORIGUAL exp
    '''
    if t[2] == '==':
        t[0] = Relational(t[1], t[3], relationalOperation.IGUAL)
    elif t[2] == '!=':
        t[0] = Relational(t[1], t[3], relationalOperation.DISTINTO)
    elif t[2] == '>':
        t[0] = Relational(t[1], t[3], relationalOperation.MAYOR)
    elif t[2] == '<':
        t[0] = Relational(t[1], t[3], relationalOperation.MENOR)
    elif t[2] == '>=':
        t[0] = Relational(t[1], t[3], relationalOperation.MAYORIGUAL)
    elif t[2] == '<=':
        t[0] = Relational(t[1], t[3], relationalOperation.MENORIGUAL)


def p_exp_logica(t):
    '''exp  : exp ANDD exp
            | exp ORR exp
            | NOTT exp %prec UNOT
    '''
    if t[2] == '&&':
        t[0] = Logic(t[1], t[3], logicOperation.AND)
    elif t[2] == '||':
        t[0] = Logic(t[1], t[3], logicOperation.OR)
    elif t[1] == '!':
        t[0] = Logic(t[2], t[2], logicOperation.NOT)


# ================================EXPRESION RETURN FUNCIONES
def p_callFuncSt2(t):
    '''exp   : ID parametersCallFunc
    '''
    t[0] = CallFuncSt(t[1], t[2])


# ================================FUNCIONES VARIAS
def p_exp_uppercase(t):
    'exp : UPPERCASE PARIZQ exp PARDER'
    t[0] = FuncionVaria(t[3], Primitive('nothing', typeExpression.NULO), operacionVaria.UPPER)


def p_exp_lowercase(t):
    'exp : LOWERCASE PARIZQ exp PARDER'
    t[0] = FuncionVaria(t[3], Primitive('nothing', typeExpression.NULO), operacionVaria.LOWER)


def p_exp_log(t):
    'exp : LOG PARIZQ exp COMA exp PARDER'
    t[0] = FuncionVaria(t[3], t[5], operacionVaria.LOG)


def p_exp_log10(t):
    'exp : LOG10 PARIZQ exp PARDER'
    t[0] = FuncionVaria(t[3], Primitive('nothing', typeExpression.NULO), operacionVaria.LOG10)


def p_exp_sin(t):
    'exp : SIN PARIZQ exp PARDER'
    t[0] = FuncionVaria(t[3], Primitive('nothing', typeExpression.NULO), operacionVaria.SIN)


def p_exp_cos(t):
    'exp : COS PARIZQ exp PARDER'
    t[0] = FuncionVaria(t[3], Primitive('nothing', typeExpression.NULO), operacionVaria.COS)


def p_exp_tan(t):
    'exp : TAN PARIZQ exp PARDER'
    t[0] = FuncionVaria(t[3], Primitive('nothing', typeExpression.NULO), operacionVaria.TAN)


def p_exp_sqrt(t):
    'exp : SQRT PARIZQ exp PARDER'
    t[0] = FuncionVaria(t[3], Primitive('nothing', typeExpression.NULO), operacionVaria.SQRT)


# ================================FUNCIONES VARIAS 2
def p_exp_parse(t):
    'exp : PARSE PARIZQ typeDef COMA exp PARDER'
    t[0] = FuncionVaria2(t[3], t[5], operacionVaria.PARSE)


def p_exp_trunc(t):
    '''exp  : TRUNC PARIZQ typeDef COMA exp PARDER
            | TRUNC PARIZQ exp PARDER
    '''
    if len(t) == 7:
        t[0] = FuncionVaria2(t[3], t[5], operacionVaria.TRUNC)
    else:
        t[0] = FuncionVaria2(typeExpression.INTEGER, t[3], operacionVaria.TRUNC)


def p_exp_float(t):
    'exp : MFLOAT PARIZQ exp PARDER'
    t[0] = FuncionVaria2(Primitive('nothing', typeExpression.NULO), t[3], operacionVaria.FLOAT)


def p_exp_string(t):
    'exp : MSTRING PARIZQ exp PARDER'
    t[0] = FuncionVaria2(Primitive('nothing', typeExpression.NULO), t[3], operacionVaria.STRING)


def p_exp_typeof(t):
    'exp : TYPEOF PARIZQ exp PARDER'
    t[0] = FuncionVaria2(Primitive('nothing', typeExpression.NULO), t[3], operacionVaria.TYPEOF)


def p_exp_push(t):
    '''exp  : RPUSH NOTT PARIZQ ID COMA exp PARDER
            | RPUSH NOTT PARIZQ ID COMA CORIZQ CORDER PARDER
            | RPUSH NOTT PARIZQ ID COMA CORIZQ exps CORDER PARDER
            | RPUSH NOTT PARIZQ ID listArray2 COMA exp PARDER
            | RPUSH NOTT PARIZQ ID listArray2 COMA CORIZQ CORDER PARDER
            | RPUSH NOTT PARIZQ ID listArray2 COMA CORIZQ exps CORDER PARDER
    '''
    if len(t) == 8:
        t[0] = Push(t[4], VariableCall(t[4]), [], t[6])
    elif len(t) == 9:
        if t[5] == ",":
            t[0] = Push(t[4], VariableCall(t[4]), [], [])
        else:
            t[0] = Push(t[4], VariableCall(t[4]), t[5], t[7])
    elif len(t) == 10:
        if t[5] == ",":
            t[0] = Push(t[4], VariableCall(t[4]), [], t[7])
        else:
            t[0] = Push(t[4], VariableCall(t[4]), t[5], [])
    elif len(t) == 11:
        t[0] = Push(t[4], VariableCall(t[4]), t[5], t[8])


def p_exp_pop(t):
    '''exp  : RPOP NOTT PARIZQ ID PARDER
            | RPOP NOTT PARIZQ ID listArray2 PARDER
    '''
    if len(t) == 6:
        t[0] = Pop(t[4], VariableCall(t[4]), [])
    else:
        t[0] = Pop(t[4], VariableCall(t[4]), t[5])


def p_exp_push2(t):
    '''push : RPUSH NOTT PARIZQ ID COMA exp PARDER PTCOMA
            | RPUSH NOTT PARIZQ ID COMA CORIZQ CORDER PARDER PTCOMA
            | RPUSH NOTT PARIZQ ID COMA CORIZQ exps CORDER PARDER PTCOMA
            | RPUSH NOTT PARIZQ ID listArray2 COMA exp PARDER PTCOMA
            | RPUSH NOTT PARIZQ ID listArray2 COMA CORIZQ CORDER PARDER PTCOMA
            | RPUSH NOTT PARIZQ ID listArray2 COMA CORIZQ exps CORDER PARDER PTCOMA

    '''
    if len(t) == 9:
        t[0] = Push(t[4], VariableCall(t[4]), [], t[6])
    elif len(t) == 10:
        if t[5] == ",":
            t[0] = Push(t[4], VariableCall(t[4]), [], [])
        else:
            t[0] = Push(t[4], VariableCall(t[4]), t[5], t[7])
    elif len(t) == 11:
        if t[5] == ",":
            t[0] = Push(t[4], VariableCall(t[4]), [], t[7])
        else:
            t[0] = Push(t[4], VariableCall(t[4]), t[5], [])
    elif len(t) == 12:
        t[0] = Push(t[4], VariableCall(t[4]), t[5], t[8])


def p_exp_pop2(t):
    '''pop  : RPOP NOTT PARIZQ ID PARDER PTCOMA
            | RPOP NOTT PARIZQ ID listArray2 PARDER PTCOMA
    '''
    if len(t) == 7:
        t[0] = Pop(t[4], VariableCall(t[4]), [])
    else:
        t[0] = Pop(t[4], VariableCall(t[4]), t[5])


def p_exp_length(t):
    'exp : RLENGTH PARIZQ exp PARDER'
    t[0] = FuncionVaria2(Primitive('nothing', typeExpression.NULO), t[3], operacionVaria.LENGTH)


# ================================TIPOS DE EXPRESIONES, DATOS Y ARREGLOS
def p_typeDef(t):
    '''typeDef  : RINT
                | RFLOAT
                | RSTRING
                | RCHAR
                | RBOOL
                | RARRAY LLAIZQ RINT LLADER
                | RARRAY LLAIZQ RFLOAT LLADER
                | RARRAY LLAIZQ RSTRING LLADER
                | RARRAY LLAIZQ RCHAR LLADER
                | RARRAY LLAIZQ RBOOL LLADER
    '''
    if t[1] == 'Int64':
        t[0] = typeExpression.INTEGER
    elif t[1] == 'Float64':
        t[0] = typeExpression.FLOAT
    elif t[1] == 'String':
        t[0] = typeExpression.STRING
    elif t[1] == 'Char':
        t[0] = typeExpression.CHAR
    elif t[1] == 'Bool':
        t[0] = typeExpression.BOOL
    elif t[1] == 'Array':
        if t[3] == 'Int64':
            t[0] = typeExpression.INTEGERA
        elif t[3] == 'Float64':
            t[0] = typeExpression.FLOATA
        elif t[3] == 'String':
            t[0] = typeExpression.STRINGA
        elif t[3] == 'Char':
            t[0] = typeExpression.CHARA
        elif t[3] == 'Bool':
            t[0] = typeExpression.BOOLA


def p_exp_agrupacion(t):
    'exp : PARIZQ exp PARDER'
    t[0] = t[2]


def p_exp_valor_entero(t):
    '''exp  : ENTERO
    '''
    t[0] = Primitive(int(t[1]), typeExpression.INTEGER)


def p_exp_valor_decimal(t):
    '''exp  : DECIMAL
    '''
    t[0] = Primitive(float(t[1]), typeExpression.FLOAT)


def p_exp_valor_string(t):
    '''exp  : STRING
    '''
    t[0] = Primitive(t[1], typeExpression.STRING)


def p_exp_valor_char(t):
    '''exp  : CHAR
    '''
    t[0] = Primitive(t[1], typeExpression.CHAR)


def p_exp_valor_verdadero(t):
    '''exp  : VERDADERO
    '''
    t[0] = Primitive(True, typeExpression.BOOL)


def p_exp_valor_falnso(t):
    '''exp  : FALSO
    '''
    t[0] = Primitive(False, typeExpression.BOOL)


def p_exp_valor_nulo(t):
    '''exp  : NULO
    '''
    t[0] = Primitive(t[1], typeExpression.NULO)


def p_exp_variable(t):
    '''exp  : ID
            | ID listArray
    '''
    if len(t) == 2:
        t[0] = VariableCall(t[1])
    elif len(t) == 3:
        t[0] = t[2]


def p_exp_array(t):
    '''exp  : CORIZQ listValues CORDER
            | CORIZQ listValues CORDER DOSPT DOSPT typeDef
            | CORIZQ CORDER
    '''
    if len(t) == 4:
        t[0] = Array(t[2], typeExpression.ANY)
    elif len(t) == 3:
        t[0] = Array([], typeExpression.ANY)
    else:
        t[0] = Array(t[2], t[6])


# ====================================================
def p_error(t):
    Errores.append(
        {'Descripcion': "Error sint??ctico en '%s'" % t.value, 'Linea': t.lineno, 'Columna': "",
         'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})


import Analyzer.ply.yacc as yacc

parser = yacc.yacc()
