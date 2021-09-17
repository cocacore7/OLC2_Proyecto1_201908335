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
    return t


def t_ENTERO(t):
    r'\d+'
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
    t.lexer.skip(1)


# Construyendo el analizador léxico
from Node.Node import Node
from Globales.Tablas import Errores
from datetime import datetime
import Analyzer.ply.lex as lex

lexer = lex.lex()

# Asociación de operadores y precedencia
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


# ================================Definición de la gramática
def p_initial(t):
    '''initial : instructions'''

    nodeInitial = Node("initial")
    nodeInitial.insertChild(t[1])

    f = open("./salida.txt", "w")
    f.write(nodeInitial.getGraphAST())


# ================================LISTA DE INSTRUCCIONES
def p_instructions(t):
    '''instructions : instructions instruction
                    | instruction
    '''
    node = Node("instructions")
    if len(t) == 3:
        node.insertChild(t[1])
        node.insertChild(t[2])
    elif len(t) == 2:
        node.insertChild(t[1])
    t[0] = node


def p_instructionsf(t):
    '''instructionsf : instructionsf instructionf
                     | instructionf
    '''
    node = Node("instructions")
    if len(t) == 3:
        node.insertChild(t[1])
        node.insertChild(t[2])
    elif len(t) == 2:
        node.insertChild(t[1])
    t[0] = node


def p_instructionsc(t):
    '''instructionsc : instructionsc instructionc
                     | instructionc
    '''
    node = Node("instructions")
    if len(t) == 3:
        node.insertChild(t[1])
        node.insertChild(t[2])
    elif len(t) == 2:
        node.insertChild(t[1])
    t[0] = node


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
    node = Node("instruction")
    node.insertChild(t[1])
    t[0] = node


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
    node = Node("instruction")
    node.insertChild(t[1])
    t[0] = node


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
    node = Node("instruction")
    node.insertChild(t[1])
    t[0] = node


# ================================INSTRUCCIONES IMPRIMIR
def p_print(t):
    '''p_print  : PRINT PARIZQ exps PARDER PTCOMA
                | PRINT PARIZQ PARDER PTCOMA
    '''
    nodePrint = Node("PrintSt")
    nodePrint.insertChild(Node("Print"))
    nodePrint.insertChild(Node("("))
    if len(t) == 6:
        nodePrint.insertChild(t[3])
    nodePrint.insertChild(Node(")"))
    nodePrint.insertChild(Node(";"))
    t[0] = nodePrint


def p_println(t):
    '''p_println    : PRINTLN PARIZQ exps PARDER PTCOMA
                    | PRINTLN PARIZQ PARDER PTCOMA
    '''
    nodePrint = Node("PrintlnSt")
    nodePrint.insertChild(Node("Println"))
    nodePrint.insertChild(Node("("))
    if len(t) == 6:
        nodePrint.insertChild(t[3])
    nodePrint.insertChild(Node(")"))
    nodePrint.insertChild(Node(";"))
    t[0] = nodePrint


def p_expresions(t):
    '''exps     : exps COMA exp
                | exp
    '''
    nodeExp = Node("EXP")
    nodeExp.insertChild(t[1])
    if len(t) == 4:
        nodeExp.insertChild(Node(","))
        nodeExp.insertChild(t[3])
    t[0] = nodeExp


# ================================DECLARACIONES Y ASIGNACIONES
def p_declaration(t):
    '''declaration  : ID IGUAL exp PTCOMA
                    | ID IGUAL exp DOSPT DOSPT typeDef PTCOMA
                    | LOCAL ID IGUAL CORIZQ exps CORDER PTCOMA
                    | GLOBAL ID IGUAL CORIZQ exps CORDER PTCOMA
                    | LOCAL ID IGUAL exp DOSPT DOSPT typeDef PTCOMA
                    | GLOBAL ID IGUAL exp DOSPT DOSPT typeDef PTCOMA
                    | LOCAL ID IGUAL exp PTCOMA
                    | GLOBAL ID IGUAL exp PTCOMA
                    | LOCAL ID PTCOMA
                    | GLOBAL ID PTCOMA
                    | ID IGUAL CORIZQ exps CORDER PTCOMA
                    | ID IGUAL CORIZQ exps CORDER DOSPT DOSPT typeDef PTCOMA
                    | LOCAL ID IGUAL CORIZQ exps CORDER DOSPT DOSPT typeDef PTCOMA
                    | GLOBAL ID IGUAL CORIZQ exps CORDER DOSPT DOSPT typeDef PTCOMA
    '''
    nodeDec = Node("Dec")
    if len(t) == 5:
        nodeDec.insertChild(t[1])
        nodeDec.insertChild(Node("="))
        nodeDec.insertChild(t[3])
        nodeDec.insertChild(Node(";"))
    elif len(t) == 8:
        if t[1] == "local":
            nodeDec.insertChild("local")
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(Node("["))
            nodeDec.insertChild(t[5])
            nodeDec.insertChild(Node("]"))
            nodeDec.insertChild(Node(";"))
        elif t[1] == "global":
            nodeDec.insertChild("global")
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(Node("["))
            nodeDec.insertChild(t[5])
            nodeDec.insertChild(Node("]"))
            nodeDec.insertChild(Node(";"))
        else:
            nodeDec.insertChild(t[1])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(t[3])
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(t[6])
            nodeDec.insertChild(Node(";"))
            t[0] = nodeDec
    elif len(t) == 9:
        if t[1] == "local":
            nodeDec.insertChild("local")
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(t[4])
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(t[7])
            nodeDec.insertChild(Node(";"))
        elif t[1] == "global":
            nodeDec.insertChild("global")
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(t[4])
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(t[7])
            nodeDec.insertChild(Node(";"))
    elif len(t) == 6:
        if t[1] == "local":
            nodeDec.insertChild("local")
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(t[4])
            nodeDec.insertChild(Node(";"))
        elif t[1] == "global":
            nodeDec.insertChild("global")
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(t[4])
            nodeDec.insertChild(Node(";"))
    elif len(t) == 4:
        if t[1] == "local":
            nodeDec.insertChild("local")
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(Node(";"))
        elif t[1] == "global":
            nodeDec.insertChild("global")
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(Node(";"))
    elif len(t) == 7:
        nodeDec.insertChild(t[1])
        nodeDec.insertChild(Node("="))
        nodeDec.insertChild(Node("["))
        nodeDec.insertChild(t[4])
        nodeDec.insertChild(Node("]"))
        nodeDec.insertChild(Node(";"))
    elif len(t) == 10:
        nodeDec.insertChild(t[1])
        nodeDec.insertChild(Node("="))
        nodeDec.insertChild(Node("["))
        nodeDec.insertChild(t[4])
        nodeDec.insertChild(Node("]"))
        nodeDec.insertChild(Node(":"))
        nodeDec.insertChild(Node(":"))
        nodeDec.insertChild(t[8])
        nodeDec.insertChild(Node(";"))
    elif len(t) == 11:
        if t[1] == "local":
            nodeDec.insertChild("local")
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(Node("["))
            nodeDec.insertChild(t[5])
            nodeDec.insertChild(Node("]"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(t[9])
            nodeDec.insertChild(Node(";"))
        elif t[1] == "global":
            nodeDec.insertChild("global")
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(Node("["))
            nodeDec.insertChild(t[5])
            nodeDec.insertChild(Node("]"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(t[9])
            nodeDec.insertChild(Node(";"))
    t[0] = nodeDec


def p_declarationf(t):
    '''declarationf : ID IGUAL exp PTCOMA
                    | ID IGUAL exp DOSPT DOSPT typeDef PTCOMA
                    | LOCAL ID IGUAL CORIZQ exps CORDER PTCOMA
                    | GLOBAL ID IGUAL CORIZQ exps CORDER PTCOMA
                    | LOCAL ID IGUAL exp DOSPT DOSPT typeDef PTCOMA
                    | GLOBAL ID IGUAL exp DOSPT DOSPT typeDef PTCOMA
                    | LOCAL ID IGUAL exp PTCOMA
                    | GLOBAL ID IGUAL exp PTCOMA
                    | LOCAL ID PTCOMA
                    | GLOBAL ID PTCOMA
                    | ID IGUAL CORIZQ exps CORDER PTCOMA
                    | ID IGUAL CORIZQ exps CORDER DOSPT DOSPT typeDef PTCOMA
                    | LOCAL ID IGUAL CORIZQ exps CORDER DOSPT DOSPT typeDef PTCOMA
                    | GLOBAL ID IGUAL CORIZQ exps CORDER DOSPT DOSPT typeDef PTCOMA
    '''
    nodeDec = Node("Dec")
    if len(t) == 5:
        nodeDec.insertChild(t[1])
        nodeDec.insertChild(Node("="))
        nodeDec.insertChild(t[3])
        nodeDec.insertChild(Node(";"))
    elif len(t) == 8:
        if t[1] == "local":
            nodeDec.insertChild("local")
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(Node("["))
            nodeDec.insertChild(t[5])
            nodeDec.insertChild(Node("]"))
            nodeDec.insertChild(Node(";"))
        elif t[1] == "global":
            nodeDec.insertChild("global")
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(Node("["))
            nodeDec.insertChild(t[5])
            nodeDec.insertChild(Node("]"))
            nodeDec.insertChild(Node(";"))
        else:
            nodeDec.insertChild(t[1])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(t[3])
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(t[6])
            nodeDec.insertChild(Node(";"))
            t[0] = nodeDec
    elif len(t) == 9:
        if t[1] == "local":
            nodeDec.insertChild("local")
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(t[4])
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(t[7])
            nodeDec.insertChild(Node(";"))
        elif t[1] == "global":
            nodeDec.insertChild("global")
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(t[4])
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(t[7])
            nodeDec.insertChild(Node(";"))
    elif len(t) == 6:
        if t[1] == "local":
            nodeDec.insertChild("local")
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(t[4])
            nodeDec.insertChild(Node(";"))
        elif t[1] == "global":
            nodeDec.insertChild("global")
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(t[4])
            nodeDec.insertChild(Node(";"))
    elif len(t) == 4:
        if t[1] == "local":
            nodeDec.insertChild("local")
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(Node(";"))
        elif t[1] == "global":
            nodeDec.insertChild("global")
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(Node(";"))
    elif len(t) == 7:
        nodeDec.insertChild(t[1])
        nodeDec.insertChild(Node("="))
        nodeDec.insertChild(Node("["))
        nodeDec.insertChild(t[4])
        nodeDec.insertChild(Node("]"))
        nodeDec.insertChild(Node(";"))
    elif len(t) == 10:
        nodeDec.insertChild(t[1])
        nodeDec.insertChild(Node("="))
        nodeDec.insertChild(Node("["))
        nodeDec.insertChild(t[4])
        nodeDec.insertChild(Node("]"))
        nodeDec.insertChild(Node(":"))
        nodeDec.insertChild(Node(":"))
        nodeDec.insertChild(t[8])
        nodeDec.insertChild(Node(";"))
    elif len(t) == 11:
        if t[1] == "local":
            nodeDec.insertChild("local")
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(Node("["))
            nodeDec.insertChild(t[5])
            nodeDec.insertChild(Node("]"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(t[9])
            nodeDec.insertChild(Node(";"))
        elif t[1] == "global":
            nodeDec.insertChild("global")
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(Node("["))
            nodeDec.insertChild(t[5])
            nodeDec.insertChild(Node("]"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(t[9])
            nodeDec.insertChild(Node(";"))
    t[0] = nodeDec


def p_declarationc(t):
    '''declarationc : ID IGUAL exp PTCOMA
                    | ID IGUAL exp DOSPT DOSPT typeDef PTCOMA
                    | LOCAL ID IGUAL CORIZQ exps CORDER PTCOMA
                    | GLOBAL ID IGUAL CORIZQ exps CORDER PTCOMA
                    | LOCAL ID IGUAL exp DOSPT DOSPT typeDef PTCOMA
                    | GLOBAL ID IGUAL exp DOSPT DOSPT typeDef PTCOMA
                    | LOCAL ID IGUAL exp PTCOMA
                    | GLOBAL ID IGUAL exp PTCOMA
                    | LOCAL ID PTCOMA
                    | GLOBAL ID PTCOMA
                    | ID IGUAL CORIZQ exps CORDER PTCOMA
                    | ID IGUAL CORIZQ exps CORDER DOSPT DOSPT typeDef PTCOMA
                    | LOCAL ID IGUAL CORIZQ exps CORDER DOSPT DOSPT typeDef PTCOMA
                    | GLOBAL ID IGUAL CORIZQ exps CORDER DOSPT DOSPT typeDef PTCOMA
    '''
    nodeDec = Node("Dec")
    if len(t) == 5:
        nodeDec.insertChild(t[1])
        nodeDec.insertChild(Node("="))
        nodeDec.insertChild(t[3])
        nodeDec.insertChild(Node(";"))
    elif len(t) == 8:
        if t[1] == "local":
            nodeDec.insertChild("local")
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(Node("["))
            nodeDec.insertChild(t[5])
            nodeDec.insertChild(Node("]"))
            nodeDec.insertChild(Node(";"))
        elif t[1] == "global":
            nodeDec.insertChild("global")
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(Node("["))
            nodeDec.insertChild(t[5])
            nodeDec.insertChild(Node("]"))
            nodeDec.insertChild(Node(";"))
        else:
            nodeDec.insertChild(t[1])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(t[3])
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(t[6])
            nodeDec.insertChild(Node(";"))
            t[0] = nodeDec
    elif len(t) == 9:
        if t[1] == "local":
            nodeDec.insertChild("local")
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(t[4])
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(t[7])
            nodeDec.insertChild(Node(";"))
        elif t[1] == "global":
            nodeDec.insertChild("global")
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(t[4])
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(t[7])
            nodeDec.insertChild(Node(";"))
    elif len(t) == 6:
        if t[1] == "local":
            nodeDec.insertChild("local")
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(t[4])
            nodeDec.insertChild(Node(";"))
        elif t[1] == "global":
            nodeDec.insertChild("global")
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(t[4])
            nodeDec.insertChild(Node(";"))
    elif len(t) == 4:
        if t[1] == "local":
            nodeDec.insertChild("local")
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(Node(";"))
        elif t[1] == "global":
            nodeDec.insertChild("global")
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(Node(";"))
    elif len(t) == 7:
        nodeDec.insertChild(t[1])
        nodeDec.insertChild(Node("="))
        nodeDec.insertChild(Node("["))
        nodeDec.insertChild(t[4])
        nodeDec.insertChild(Node("]"))
        nodeDec.insertChild(Node(";"))
    elif len(t) == 10:
        nodeDec.insertChild(t[1])
        nodeDec.insertChild(Node("="))
        nodeDec.insertChild(Node("["))
        nodeDec.insertChild(t[4])
        nodeDec.insertChild(Node("]"))
        nodeDec.insertChild(Node(":"))
        nodeDec.insertChild(Node(":"))
        nodeDec.insertChild(t[8])
        nodeDec.insertChild(Node(";"))
    elif len(t) == 11:
        if t[1] == "local":
            nodeDec.insertChild("local")
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(Node("["))
            nodeDec.insertChild(t[5])
            nodeDec.insertChild(Node("]"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(t[9])
            nodeDec.insertChild(Node(";"))
        elif t[1] == "global":
            nodeDec.insertChild("global")
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(Node("["))
            nodeDec.insertChild(t[5])
            nodeDec.insertChild(Node("]"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(t[9])
            nodeDec.insertChild(Node(";"))
    t[0] = nodeDec


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
    nodeDec = Node("Dec")
    if len(t) == 8:
        nodeDec.insertChild(t[1])
        nodeDec.insertChild(t[2])
        nodeDec.insertChild(Node("="))
        nodeDec.insertChild(Node("["))
        nodeDec.insertChild(t[5])
        nodeDec.insertChild(Node("]"))
        nodeDec.insertChild(Node(";"))
    elif len(t) == 11:
        nodeDec.insertChild(t[1])
        nodeDec.insertChild(t[2])
        nodeDec.insertChild(Node("="))
        nodeDec.insertChild(Node("["))
        nodeDec.insertChild(t[5])
        nodeDec.insertChild(Node("]"))
        nodeDec.insertChild(Node(":"))
        nodeDec.insertChild(Node(":"))
        nodeDec.insertChild(t[9])
        nodeDec.insertChild(Node(";"))
    elif len(t) == 12:
        if t[1] == "local":
            nodeDec.insertChild(Node("local"))
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(t[3])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(Node("["))
            nodeDec.insertChild(t[6])
            nodeDec.insertChild(Node("]"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(t[10])
            nodeDec.insertChild(Node(";"))
        elif t[1] == "global":
            nodeDec.insertChild(Node("global"))
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(t[3])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(Node("["))
            nodeDec.insertChild(t[6])
            nodeDec.insertChild(Node("]"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(t[10])
            nodeDec.insertChild(Node(";"))
    elif len(t) == 9:
        if t[1] == "local":
            nodeDec.insertChild(Node("local"))
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(t[3])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(Node("["))
            nodeDec.insertChild(t[6])
            nodeDec.insertChild(Node("]"))
            nodeDec.insertChild(Node(";"))
        elif t[1] == "global":
            nodeDec.insertChild(Node("global"))
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(t[3])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(Node("["))
            nodeDec.insertChild(t[6])
            nodeDec.insertChild(Node("]"))
            nodeDec.insertChild(Node(";"))
        else:
            nodeDec.insertChild(t[1])
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(t[4])
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(t[7])
            nodeDec.insertChild(Node(";"))
    elif len(t) == 6:
        nodeDec.insertChild(t[2])
        nodeDec.insertChild(t[3])
        nodeDec.insertChild(Node("="))
        nodeDec.insertChild(t[5])
        nodeDec.insertChild(Node(";"))
    elif len(t) == 10:
        if t[1] == "local":
            nodeDec.insertChild(Node("local"))
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(t[3])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(t[5])
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(t[8])
            nodeDec.insertChild(Node(";"))
        elif t[1] == "global":
            nodeDec.insertChild(Node("global"))
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(t[3])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(t[5])
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(t[8])
            nodeDec.insertChild(Node(";"))
    elif len(t) == 7:
        if t[1] == "local":
            nodeDec.insertChild(Node("local"))
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(t[3])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(t[5])
            nodeDec.insertChild(Node(";"))
        elif t[1] == "global":
            nodeDec.insertChild(Node("global"))
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(t[3])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(t[5])
            nodeDec.insertChild(Node(";"))
    t[0] = nodeDec


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
    nodeDec = Node("Dec")
    if len(t) == 8:
        nodeDec.insertChild(t[1])
        nodeDec.insertChild(t[2])
        nodeDec.insertChild(Node("="))
        nodeDec.insertChild(Node("["))
        nodeDec.insertChild(t[5])
        nodeDec.insertChild(Node("]"))
        nodeDec.insertChild(Node(";"))
    elif len(t) == 11:
        nodeDec.insertChild(t[1])
        nodeDec.insertChild(t[2])
        nodeDec.insertChild(Node("="))
        nodeDec.insertChild(Node("["))
        nodeDec.insertChild(t[5])
        nodeDec.insertChild(Node("]"))
        nodeDec.insertChild(Node(":"))
        nodeDec.insertChild(Node(":"))
        nodeDec.insertChild(t[9])
        nodeDec.insertChild(Node(";"))
    elif len(t) == 12:
        if t[1] == "local":
            nodeDec.insertChild(Node("local"))
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(t[3])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(Node("["))
            nodeDec.insertChild(t[6])
            nodeDec.insertChild(Node("]"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(t[10])
            nodeDec.insertChild(Node(";"))
        elif t[1] == "global":
            nodeDec.insertChild(Node("global"))
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(t[3])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(Node("["))
            nodeDec.insertChild(t[6])
            nodeDec.insertChild(Node("]"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(t[10])
            nodeDec.insertChild(Node(";"))
    elif len(t) == 9:
        if t[1] == "local":
            nodeDec.insertChild(Node("local"))
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(t[3])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(Node("["))
            nodeDec.insertChild(t[6])
            nodeDec.insertChild(Node("]"))
            nodeDec.insertChild(Node(";"))
        elif t[1] == "global":
            nodeDec.insertChild(Node("global"))
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(t[3])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(Node("["))
            nodeDec.insertChild(t[6])
            nodeDec.insertChild(Node("]"))
            nodeDec.insertChild(Node(";"))
        else:
            nodeDec.insertChild(t[1])
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(t[4])
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(t[7])
            nodeDec.insertChild(Node(";"))
    elif len(t) == 6:
        nodeDec.insertChild(t[2])
        nodeDec.insertChild(t[3])
        nodeDec.insertChild(Node("="))
        nodeDec.insertChild(t[5])
        nodeDec.insertChild(Node(";"))
    elif len(t) == 10:
        if t[1] == "local":
            nodeDec.insertChild(Node("local"))
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(t[3])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(t[5])
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(t[8])
            nodeDec.insertChild(Node(";"))
        elif t[1] == "global":
            nodeDec.insertChild(Node("global"))
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(t[3])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(t[5])
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(t[8])
            nodeDec.insertChild(Node(";"))
    elif len(t) == 7:
        if t[1] == "local":
            nodeDec.insertChild(Node("local"))
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(t[3])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(t[5])
            nodeDec.insertChild(Node(";"))
        elif t[1] == "global":
            nodeDec.insertChild(Node("global"))
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(t[3])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(t[5])
            nodeDec.insertChild(Node(";"))
    t[0] = nodeDec


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
    nodeDec = Node("Dec")
    if len(t) == 8:
        nodeDec.insertChild(t[1])
        nodeDec.insertChild(t[2])
        nodeDec.insertChild(Node("="))
        nodeDec.insertChild(Node("["))
        nodeDec.insertChild(t[5])
        nodeDec.insertChild(Node("]"))
        nodeDec.insertChild(Node(";"))
    elif len(t) == 11:
        nodeDec.insertChild(t[1])
        nodeDec.insertChild(t[2])
        nodeDec.insertChild(Node("="))
        nodeDec.insertChild(Node("["))
        nodeDec.insertChild(t[5])
        nodeDec.insertChild(Node("]"))
        nodeDec.insertChild(Node(":"))
        nodeDec.insertChild(Node(":"))
        nodeDec.insertChild(t[9])
        nodeDec.insertChild(Node(";"))
    elif len(t) == 12:
        if t[1] == "local":
            nodeDec.insertChild(Node("local"))
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(t[3])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(Node("["))
            nodeDec.insertChild(t[6])
            nodeDec.insertChild(Node("]"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(t[10])
            nodeDec.insertChild(Node(";"))
        elif t[1] == "global":
            nodeDec.insertChild(Node("global"))
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(t[3])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(Node("["))
            nodeDec.insertChild(t[6])
            nodeDec.insertChild(Node("]"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(t[10])
            nodeDec.insertChild(Node(";"))
    elif len(t) == 9:
        if t[1] == "local":
            nodeDec.insertChild(Node("local"))
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(t[3])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(Node("["))
            nodeDec.insertChild(t[6])
            nodeDec.insertChild(Node("]"))
            nodeDec.insertChild(Node(";"))
        elif t[1] == "global":
            nodeDec.insertChild(Node("global"))
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(t[3])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(Node("["))
            nodeDec.insertChild(t[6])
            nodeDec.insertChild(Node("]"))
            nodeDec.insertChild(Node(";"))
        else:
            nodeDec.insertChild(t[1])
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(t[4])
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(t[7])
            nodeDec.insertChild(Node(";"))
    elif len(t) == 6:
        nodeDec.insertChild(t[2])
        nodeDec.insertChild(t[3])
        nodeDec.insertChild(Node("="))
        nodeDec.insertChild(t[5])
        nodeDec.insertChild(Node(";"))
    elif len(t) == 10:
        if t[1] == "local":
            nodeDec.insertChild(Node("local"))
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(t[3])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(t[5])
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(t[8])
            nodeDec.insertChild(Node(";"))
        elif t[1] == "global":
            nodeDec.insertChild(Node("global"))
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(t[3])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(t[5])
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(Node(":"))
            nodeDec.insertChild(t[8])
            nodeDec.insertChild(Node(";"))
    elif len(t) == 7:
        if t[1] == "local":
            nodeDec.insertChild(Node("local"))
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(t[3])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(t[5])
            nodeDec.insertChild(Node(";"))
        elif t[1] == "global":
            nodeDec.insertChild(Node("global"))
            nodeDec.insertChild(t[2])
            nodeDec.insertChild(t[3])
            nodeDec.insertChild(Node("="))
            nodeDec.insertChild(t[5])
            nodeDec.insertChild(Node(";"))
    t[0] = nodeDec


# ================================FUNCIONES
def p_function(t):
    '''function : FUNCTION ID parametersFunc blockf
    '''
    nodeFunc = Node("Func")
    nodeFunc.insertChild(Node("function"))
    nodeFunc.insertChild(t[2])
    nodeFunc.insertChild(t[3])
    nodeFunc.insertChild(t[4])
    t[0] = nodeFunc


def p_parametersFunc(t):
    '''parametersFunc   : PARIZQ parameters PARDER
                        | PARIZQ PARDER
    '''
    nodeParamFunc = Node("ParamFunc")
    nodeParamFunc.insertChild(Node("("))
    if len(t) == 4:
        nodeParamFunc.insertChild(t[2])
    nodeParamFunc.insertChild(Node(")"))
    t[0] = nodeParamFunc


def p_parameters(t):
    '''parameters   : parameters COMA parameter
                    | parameter
    '''
    nodeParams = Node("ParamFunc")
    nodeParams.insertChild(t[1])
    if len(t) == 4:
        nodeParams.insertChild(Node(","))
        nodeParams.insertChild(t[3])
    t[0] = nodeParams


def p_parameter(t):
    '''parameter    : ID DOSPT DOSPT typeDef
                    | ID
    '''
    nodeParam = Node("ParamFunc")
    nodeParam.insertChild(t[1])
    if len(t) == 5:
        nodeParam.insertChild(Node(":"))
        nodeParam.insertChild(Node(":"))
        nodeParam.insertChild(t[4])
    t[0] = nodeParam


# ================================LLAMADA A FUNCIONES
def p_callFuncSt(t):
    '''callFuncSt   : ID parametersCallFunc PTCOMA
    '''
    nodeCallFunc = Node("CallFunc")
    nodeCallFunc.insertChild(t[1])
    nodeCallFunc.insertChild(t[2])
    nodeCallFunc.insertChild(Node(";"))
    t[0] = nodeCallFunc


def p_parametersCallFunc(t):
    '''parametersCallFunc   : PARIZQ listValues PARDER
                            | PARIZQ PARDER
    '''
    node = Node("ValuesCallFunc")
    node.insertChild(Node("("))
    if len(t) == 4:
        node.insertChild(t[2])
    node.insertChild(Node(")"))
    t[0] = node


def p_listValues(t):
    '''listValues   : listValues COMA exp
                    | exp
    '''
    node = Node("Value")
    node.insertChild(t[1])
    if len(t) == 4:
        node.insertChild(Node(","))
        node.insertChild(t[3])
    t[0] = node


# ================================CONDICIONAL IF
def p_ifSt(t):
    ''' ifSt    : RIF exp END PTCOMA
                | RIF exp blockiff END PTCOMA
                | RIF exp blockiff RELSE blockiff END PTCOMA
                | RIF exp blockiff elseifSt RELSE END PTCOMA
                | RIF exp blockiff RELSE END PTCOMA
                | RIF exp blockiff elseifSt END PTCOMA
                | RIF exp blockiff elseifSt RELSE blockiff END PTCOMA
    '''
    node = Node("IfSt")
    node.insertChild(Node("if"))
    if len(t) == 5:
        node.insertChild(t[2])
    elif len(t) == 6:
        node.insertChild(t[2])
        node.insertChild(t[3])
    elif len(t) == 8:
        if t[4] == 'else':
            node.insertChild(t[2])
            node.insertChild(t[3])
            node.insertChild(Node("else"))
            node.insertChild(t[5])
        elif t[5] == 'else':
            node.insertChild(t[2])
            node.insertChild(t[3])
            node.insertChild(t[4])
            node.insertChild(Node("else"))
    elif len(t) == 7:
        if t[4] == 'else':
            node.insertChild(t[2])
            node.insertChild(t[3])
            node.insertChild(Node("else"))
        else:
            node.insertChild(t[2])
            node.insertChild(t[3])
            node.insertChild(t[4])
    elif len(t) == 9:
        node.insertChild(t[2])
        node.insertChild(t[3])
        node.insertChild(t[4])
        node.insertChild(Node("else"))
        node.insertChild(t[6])
    node.insertChild(Node("end"))
    node.insertChild(Node(";"))
    t[0] = node


def p_elseifSt(t):
    '''elseifSt : elseifSt conelseif
    '''
    node = Node("ElseIfSt")
    node.insertChild(t[1])
    node.insertChild(t[2])
    t[0] = node


def p_elseifSt_2(t):
    '''elseifSt : conelseif
    '''
    node = Node("ElseIfSt")
    node.insertChild(t[1])
    t[0] = node


def p_conelseift(t):
    '''conelseif    : RELSEIF exp blockiff
                    | RELSEIF exp
    '''
    node = Node("ElseIfSt")
    node.insertChild(Node("elseif"))
    if len(t) == 3:
        node.insertChild(t[2])
    elif len(t) == 4:
        node.insertChild(t[2])
        node.insertChild(t[3])
    t[0] = node


def p_ifStc(t):
    ''' ifStc    : RIF exp END PTCOMA
                | RIF exp blockifc END PTCOMA
                | RIF exp blockifc RELSE blockifc END PTCOMA
                | RIF exp blockifc RELSE END PTCOMA
                | RIF exp blockifc elseifStc END PTCOMA
                | RIF exp blockifc elseifStc RELSE blockifc END PTCOMA
                | RIF exp blockifc elseifStc RELSE END PTCOMA
    '''
    node = Node("IfSt")
    node.insertChild(Node("if"))
    if len(t) == 5:
        node.insertChild(t[2])
    elif len(t) == 6:
        node.insertChild(t[2])
        node.insertChild(t[3])
    elif len(t) == 8:
        if t[4] == 'else':
            node.insertChild(t[2])
            node.insertChild(t[3])
            node.insertChild(Node("else"))
            node.insertChild(t[5])
        elif t[5] == 'else':
            node.insertChild(t[2])
            node.insertChild(t[3])
            node.insertChild(t[4])
            node.insertChild(Node("else"))
    elif len(t) == 7:
        if t[4] == 'else':
            node.insertChild(t[2])
            node.insertChild(t[3])
            node.insertChild(Node("else"))
        else:
            node.insertChild(t[2])
            node.insertChild(t[3])
            node.insertChild(t[4])
    elif len(t) == 9:
        node.insertChild(t[2])
        node.insertChild(t[3])
        node.insertChild(t[4])
        node.insertChild(Node("else"))
        node.insertChild(t[6])
    node.insertChild(Node("end"))
    node.insertChild(Node(";"))
    t[0] = node


def p_elseifStc(t):
    '''elseifStc : elseifStc conelseifc
    '''
    node = Node("ElseIfSt")
    node.insertChild(t[1])
    node.insertChild(t[2])
    t[0] = node


def p_elseifStc_2(t):
    '''elseifStc : conelseifc
    '''
    node = Node("ElseIfSt")
    node.insertChild(t[1])
    t[0] = node


def p_conelseiftc(t):
    '''conelseifc    : RELSEIF exp blockifc
                     | RELSEIF exp
    '''
    node = Node("ElseIfSt")
    node.insertChild(Node("elseif"))
    if len(t) == 3:
        node.insertChild(t[2])
    elif len(t) == 4:
        node.insertChild(t[2])
        node.insertChild(t[3])
    t[0] = node


# ================================CICLO WHILE
def p_whileSt(t):
    '''whileSt  : RWHILE exp blockc
    '''
    node = Node("WhileSt")
    node.insertChild(Node("while"))
    node.insertChild(t[2])
    node.insertChild(t[3])
    t[0] = node


# ================================CICLO FOR
def p_forSt(t):
    '''forSt    : RFOR parameter RIN exp DOSPT exp blockc
                | RFOR parameter RIN exp blockc
    '''
    node = Node("ForSt")
    node.insertChild(Node("for"))
    node.insertChild(t[2])
    node.insertChild(Node("in"))
    node.insertChild(t[4])
    if len(t) == 8:
        node.insertChild(Node(":"))
        node.insertChild(t[6])
        node.insertChild(t[7])
    elif len(t) == 6:
        node.insertChild(t[5])
    t[0] = node


# ================================BLOQUES DE CODIGO
def p_blockf(t):
    '''blockf   : instructionsf END PTCOMA
                | END PTCOMA
    '''
    node = Node("BlockSt")
    if len(t) == 4:
        node.insertChild(t[1])
    node.insertChild(Node("end"))
    node.insertChild(Node(";"))
    t[0] = node


def p_blockc(t):
    '''blockc   : instructionsc END PTCOMA
                | END PTCOMA
    '''
    node = Node("BlockSt")
    if len(t) == 4:
        node.insertChild(t[1])
    node.insertChild(Node("end"))
    node.insertChild(Node(";"))
    t[0] = node


def p_blockiff(t):
    '''blockiff  : instructionsf
    '''
    node = Node("BlockifSt")
    node.insertChild(t[1])
    t[0] = node


def p_blockifc(t):
    '''blockifc  : instructionsc
    '''
    node = Node("BlockifSt")
    node.insertChild(t[1])
    t[0] = node


# ================================SENTENCIAS DE TRANSFERENCIA
def p_return(t):
    '''returnST : RRETURN exp PTCOMA
                | RRETURN PTCOMA
    '''
    node = Node("ReturnSt")
    node.insertChild(Node("return"))
    if len(t) == 4:
        node.insertChild(t[2])
    node.insertChild(Node(";"))
    t[0] = node


def p_break(t):
    '''breakST  : RBREAK PTCOMA
    '''
    node = Node("BreakSt")
    node.insertChild(Node("break"))
    node.insertChild(Node(";"))
    t[0] = node


def p_continue(t):
    '''continueST  : RCONTINUE PTCOMA
    '''
    node = Node("ContinueSt")
    node.insertChild(Node("continue"))
    node.insertChild(Node(";"))
    t[0] = node


# ================================ARREGLOS
def p_list_array(t):
    '''listArray    : listArray  CORIZQ exp CORDER
                    | CORIZQ exp CORDER
    '''
    node = Node("ListArraySt")
    if len(t) == 5:
        node.insertChild(t[1])
        node.insertChild(Node("["))
        node.insertChild(t[3])
        node.insertChild(Node("]"))
    elif len(t) == 4:
        node.insertChild(Node("["))
        node.insertChild(t[2])
        node.insertChild(Node("]"))
    t[0] = node


def p_list_array2(t):
    '''listArray2   : listArray2  CORIZQ exp CORDER
                    | CORIZQ exp CORDER
    '''
    node = Node("ListArraySt")
    if len(t) == 5:
        node.insertChild(t[1])
        node.insertChild(Node("["))
        node.insertChild(t[3])
        node.insertChild(Node("]"))
    elif len(t) == 4:
        node.insertChild(Node("["))
        node.insertChild(t[2])
        node.insertChild(Node("]"))
    t[0] = node


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
    node = Node("EXP")
    if t[2] == '+':
        node.insertChild(t[1])
        node.insertChild(Node("+"))
        node.insertChild(t[3])
    elif t[2] == '-':
        node.insertChild(t[1])
        node.insertChild(Node("-"))
        node.insertChild(t[3])
    elif t[2] == '*':
        node.insertChild(t[1])
        node.insertChild(Node("*"))
        node.insertChild(t[3])
    elif t[2] == '/':
        node.insertChild(t[1])
        node.insertChild(Node("/"))
        node.insertChild(t[3])
    elif t[2] == '^':
        node.insertChild(t[1])
        node.insertChild(Node("^"))
        node.insertChild(t[3])
    elif t[2] == '%':
        node.insertChild(t[1])
        node.insertChild(Node("%"))
        node.insertChild(t[3])
    elif t[1] == '-':
        node.insertChild(Node("-"))
        node.insertChild(t[2])
    t[0] = node


def p_exp_relacional(t):
    '''exp  : exp IGUALIGUAL exp
            | exp DISTINTO exp
            | exp MAYOR exp
            | exp MENOR exp
            | exp MAYORIGUAL exp
            | exp MENORIGUAL exp
    '''
    node = Node("EXP")
    if t[2] == '==':
        node.insertChild(t[1])
        node.insertChild(Node("=="))
        node.insertChild(t[3])
    elif t[2] == '!=':
        node.insertChild(t[1])
        node.insertChild(Node("!="))
        node.insertChild(t[3])
    elif t[2] == '>':
        node.insertChild(t[1])
        node.insertChild(Node(">"))
        node.insertChild(t[3])
    elif t[2] == '<':
        node.insertChild(t[1])
        node.insertChild(Node("<"))
        node.insertChild(t[3])
    elif t[2] == '>=':
        node.insertChild(t[1])
        node.insertChild(Node(">="))
        node.insertChild(t[3])
    elif t[2] == '<=':
        node.insertChild(t[1])
        node.insertChild(Node("<="))
        node.insertChild(t[3])
    t[0] = node


def p_exp_logica(t):
    '''exp  : exp ANDD exp
            | exp ORR exp
            | NOTT exp %prec UNOT
    '''
    node = Node("EXP")
    if t[2] == '&&':
        node.insertChild(t[1])
        node.insertChild(Node("&&"))
        node.insertChild(t[3])
    elif t[2] == '||':
        node.insertChild(t[1])
        node.insertChild(Node("||"))
        node.insertChild(t[3])
    elif t[1] == '!':
        node.insertChild(t[1])
        node.insertChild(Node("!"))
        node.insertChild(t[3])
    t[0] = node


# ================================EXPRESION RETURN FUNCIONES
def p_callFuncSt2(t):
    '''exp   : ID parametersCallFunc
    '''
    node = Node("EXP")
    node.insertChild(t[1])
    node.insertChild(t[2])
    t[0] = node


# ================================FUNCIONES VARIAS
def p_exp_uppercase(t):
    'exp : UPPERCASE PARIZQ exp PARDER'
    node = Node("EXP")
    node.insertChild(Node("uppercase"))
    node.insertChild(Node("("))
    node.insertChild(t[3])
    node.insertChild(Node(")"))
    t[0] = node


def p_exp_lowercase(t):
    'exp : LOWERCASE PARIZQ exp PARDER'
    node = Node("EXP")
    node.insertChild(Node("lowercase"))
    node.insertChild(Node("("))
    node.insertChild(t[3])
    node.insertChild(Node(")"))
    t[0] = node


def p_exp_log(t):
    'exp : LOG PARIZQ exp COMA exp PARDER'
    node = Node("EXP")
    node.insertChild(Node("log"))
    node.insertChild(Node("("))
    node.insertChild(t[3])
    node.insertChild(Node(","))
    node.insertChild(t[5])
    node.insertChild(Node(")"))
    t[0] = node


def p_exp_log10(t):
    'exp : LOG10 PARIZQ exp PARDER'
    node = Node("EXP")
    node.insertChild(Node("log10"))
    node.insertChild(Node("("))
    node.insertChild(t[3])
    node.insertChild(Node(")"))
    t[0] = node


def p_exp_sin(t):
    'exp : SIN PARIZQ exp PARDER'
    node = Node("EXP")
    node.insertChild(Node("sin"))
    node.insertChild(Node("("))
    node.insertChild(t[3])
    node.insertChild(Node(")"))
    t[0] = node


def p_exp_cos(t):
    'exp : COS PARIZQ exp PARDER'
    node = Node("EXP")
    node.insertChild(Node("cos"))
    node.insertChild(Node("("))
    node.insertChild(t[3])
    node.insertChild(Node(")"))
    t[0] = node


def p_exp_tan(t):
    'exp : TAN PARIZQ exp PARDER'
    node = Node("EXP")
    node.insertChild(Node("tan"))
    node.insertChild(Node("("))
    node.insertChild(t[3])
    node.insertChild(Node(")"))
    t[0] = node


def p_exp_sqrt(t):
    'exp : SQRT PARIZQ exp PARDER'
    node = Node("EXP")
    node.insertChild(Node("sqrt"))
    node.insertChild(Node("("))
    node.insertChild(t[3])
    node.insertChild(Node(")"))
    t[0] = node


# ================================FUNCIONES VARIAS 2
def p_exp_parse(t):
    'exp : PARSE PARIZQ typeDef COMA exp PARDER'
    node = Node("EXP")
    node.insertChild(Node("parse"))
    node.insertChild(Node("("))
    node.insertChild(t[3])
    node.insertChild(Node(","))
    node.insertChild(t[5])
    node.insertChild(Node(")"))
    t[0] = node


def p_exp_trunc(t):
    '''exp  : TRUNC PARIZQ typeDef COMA exp PARDER
            | TRUNC PARIZQ exp PARDER
    '''
    node = Node("EXP")
    if len(t) == 7:
        node.insertChild(Node("trunc"))
        node.insertChild(Node("("))
        node.insertChild(t[3])
        node.insertChild(Node(","))
        node.insertChild(t[5])
        node.insertChild(Node(")"))
    else:
        node.insertChild(Node("trunc"))
        node.insertChild(Node("("))
        node.insertChild(t[3])
        node.insertChild(Node(")"))
    t[0] = node


def p_exp_float(t):
    'exp : MFLOAT PARIZQ exp PARDER'
    node = Node("EXP")
    node.insertChild(Node("float"))
    node.insertChild(Node("("))
    node.insertChild(t[3])
    node.insertChild(Node(")"))
    t[0] = node


def p_exp_string(t):
    'exp : MSTRING PARIZQ exp PARDER'
    node = Node("EXP")
    node.insertChild(Node("string"))
    node.insertChild(Node("("))
    node.insertChild(t[3])
    node.insertChild(Node(")"))
    t[0] = node


def p_exp_typeof(t):
    'exp : TYPEOF PARIZQ exp PARDER'
    node = Node("EXP")
    node.insertChild(Node("parse"))
    node.insertChild(Node("("))
    node.insertChild(t[3])
    node.insertChild(Node(")"))
    t[0] = node


def p_exp_push(t):
    '''exp  : RPUSH NOTT PARIZQ ID COMA exp PARDER
            | RPUSH NOTT PARIZQ ID COMA CORIZQ CORDER PARDER
            | RPUSH NOTT PARIZQ ID listArray2 COMA exp PARDER
            | RPUSH NOTT PARIZQ ID COMA CORIZQ exps CORDER PARDER
            | RPUSH NOTT PARIZQ ID listArray2 COMA CORIZQ CORDER PARDER
            | RPUSH NOTT PARIZQ ID listArray2 COMA CORIZQ exps CORDER PARDER
    '''
    node = Node("EXP")
    node.insertChild(Node("push"))
    node.insertChild(Node("!"))
    node.insertChild(Node("("))
    if len(t) == 8:
        node.insertChild(t[4])
        node.insertChild(Node(","))
        node.insertChild(t[6])
    elif len(t) == 9:
        if t[5] == ",":
            node.insertChild(t[4])
            node.insertChild(Node(","))
            node.insertChild(Node("["))
            node.insertChild(Node("]"))
        else:
            node.insertChild(t[4])
            node.insertChild(t[5])
            node.insertChild(Node(","))
            node.insertChild(t[7])
    elif len(t) == 10:
        if t[5] == ",":
            node.insertChild(t[4])
            node.insertChild(Node(","))
            node.insertChild(Node("["))
            node.insertChild(t[7])
            node.insertChild(Node("]"))
        else:
            node.insertChild(t[4])
            node.insertChild(t[5])
            node.insertChild(Node("["))
            node.insertChild(t[7])
            node.insertChild(Node("]"))
    elif len(t) == 11:
        node.insertChild(t[4])
        node.insertChild(t[5])
        node.insertChild(Node(","))
        node.insertChild(Node("["))
        node.insertChild(t[8])
        node.insertChild(Node("]"))
    node.insertChild(Node(")"))
    t[0] = node


def p_exp_pop(t):
    '''exp  : RPOP NOTT PARIZQ ID PARDER
            | RPOP NOTT PARIZQ ID listArray2 PARDER
    '''
    node = Node("EXP")
    node.insertChild(Node("pop"))
    node.insertChild(Node("!"))
    node.insertChild(Node("("))
    if len(t) == 6:
        node.insertChild(t[4])
    else:
        node.insertChild(t[4])
        node.insertChild(t[5])
    node.insertChild(Node(")"))
    t[0] = node


def p_exp_push2(t):
    '''push : RPUSH NOTT PARIZQ ID COMA exp PARDER PTCOMA
            | RPUSH NOTT PARIZQ ID COMA CORIZQ CORDER PARDER PTCOMA
            | RPUSH NOTT PARIZQ ID COMA CORIZQ exps CORDER PARDER PTCOMA
            | RPUSH NOTT PARIZQ ID listArray2 COMA exp PARDER PTCOMA
            | RPUSH NOTT PARIZQ ID listArray2 COMA CORIZQ CORDER PARDER PTCOMA
            | RPUSH NOTT PARIZQ ID listArray2 COMA CORIZQ exps CORDER PARDER PTCOMA

    '''
    node = Node("PushSt")
    node.insertChild(Node("push"))
    node.insertChild(Node("!"))
    node.insertChild(Node("("))
    if len(t) == 9:
        node.insertChild(t[4])
        node.insertChild(Node(","))
        node.insertChild(t[6])
    elif len(t) == 10:
        if t[5] == ",":
            node.insertChild(t[4])
            node.insertChild(Node(","))
            node.insertChild(Node("["))
            node.insertChild(Node("]"))
        else:
            node.insertChild(t[4])
            node.insertChild(t[5])
            node.insertChild(Node(","))
            node.insertChild(t[7])
    elif len(t) == 11:
        if t[5] == ",":
            node.insertChild(t[4])
            node.insertChild(Node(","))
            node.insertChild(Node("["))
            node.insertChild(t[7])
            node.insertChild(Node("]"))
        else:
            node.insertChild(t[4])
            node.insertChild(t[5])
            node.insertChild(Node("["))
            node.insertChild(t[7])
            node.insertChild(Node("]"))
    elif len(t) == 12:
        node.insertChild(t[4])
        node.insertChild(t[5])
        node.insertChild(Node(","))
        node.insertChild(Node("["))
        node.insertChild(t[8])
        node.insertChild(Node("]"))
    node.insertChild(Node(")"))
    node.insertChild(Node(";"))
    t[0] = node


def p_exp_pop2(t):
    '''pop  : RPOP NOTT PARIZQ ID PARDER PTCOMA
            | RPOP NOTT PARIZQ ID listArray2 PARDER PTCOMA
    '''
    node = Node("PopSt")
    node.insertChild(Node("pop"))
    node.insertChild(Node("!"))
    node.insertChild(Node("("))
    if len(t) == 7:
        node.insertChild(t[4])
    else:
        node.insertChild(t[4])
        node.insertChild(t[5])
    node.insertChild(Node(")"))
    t[0] = node


def p_exp_length(t):
    'exp : RLENGTH PARIZQ exp PARDER'
    node = Node("EXP")
    node.insertChild(Node("length"))
    node.insertChild(Node("("))
    node.insertChild(t[3])
    node.insertChild(Node(")"))
    t[0] = node


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
    node = Node("EXP")
    if t[1] == 'Int64':
        node.insertChild(Node("Int64"))
    elif t[1] == 'Float64':
        node.insertChild(Node("Float64"))
    elif t[1] == 'String':
        node.insertChild(Node("String"))
    elif t[1] == 'Char':
        node.insertChild(Node("Char"))
    elif t[1] == 'Bool':
        node.insertChild(Node("Bool"))
    elif t[1] == 'Array':
        node.insertChild(Node("Array"))
        node.insertChild(Node("{"))
        if t[3] == 'Int64':
            node.insertChild(Node("Int64"))
        elif t[3] == 'Float64':
            node.insertChild(Node("Float64"))
        elif t[3] == 'String':
            node.insertChild(Node("String"))
        elif t[3] == 'Char':
            node.insertChild(Node("Char"))
        elif t[3] == 'Bool':
            node.insertChild(Node("Bool"))
        node.insertChild(Node("}"))
    t[0] = node


def p_exp_agrupacion(t):
    'exp : PARIZQ exp PARDER'
    node = Node("EXP")
    node.insertChild(Node("("))
    node.insertChild(t[2])
    node.insertChild(Node(")"))
    t[0] = node


def p_exp_valor_entero(t):
    '''exp  : ENTERO
    '''
    node = Node("EXP")
    node.insertChild(t[1])
    t[0] = node


def p_exp_valor_decimal(t):
    '''exp  : DECIMAL
    '''
    node = Node("EXP")
    node.insertChild(t[1])
    t[0] = node


def p_exp_valor_string(t):
    '''exp  : STRING
    '''
    node = Node("EXP")
    node.insertChild(t[1])
    t[0] = node


def p_exp_valor_char(t):
    '''exp  : CHAR
    '''
    node = Node("EXP")
    node.insertChild(t[1])
    t[0] = node


def p_exp_valor_verdadero(t):
    '''exp  : VERDADERO
    '''
    node = Node("EXP")
    node.insertChild(t[1])
    t[0] = node


def p_exp_valor_falnso(t):
    '''exp  : FALSO
    '''
    node = Node("EXP")
    node.insertChild(t[1])
    t[0] = node


def p_exp_valor_nulo(t):
    '''exp  : NULO
    '''
    node = Node("EXP")
    node.insertChild(t[1])
    t[0] = node


def p_exp_variable(t):
    '''exp  : ID
            | ID listArray
    '''
    node = Node("EXP")
    if len(t) == 2:
        node.insertChild(t[1])
    elif len(t) == 3:
        node.insertChild(t[1])
        node.insertChild(t[2])
    t[0] = node


def p_exp_array(t):
    '''exp  : CORIZQ listValues CORDER
            | CORIZQ listValues CORDER DOSPT DOSPT typeDef
            | CORIZQ CORDER
    '''
    node = Node("EXP")
    if len(t) == 4:
        node.insertChild(Node("["))
        node.insertChild(t[2])
        node.insertChild(Node("]"))
    elif len(t) == 3:
        node.insertChild(Node("["))
        node.insertChild(Node("]"))
    else:
        node.insertChild(Node("["))
        node.insertChild(t[2])
        node.insertChild(Node("]"))
        node.insertChild(Node(":"))
        node.insertChild(Node(":"))
        node.insertChild(t[6])
    t[0] = node


# ====================================================
def p_error(t):
    print("Error sintáctico en '%s'" % t.value)


import Analyzer.ply.yacc as yacc

parser2 = yacc.yacc()
