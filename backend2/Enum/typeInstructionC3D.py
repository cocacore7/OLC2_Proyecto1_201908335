import enum


class typeInstruction(enum.Enum):
    ASSIGNMENT = 0
    LABEL = 1
    GOTO = 2
    IF = 3
    HEAPA = 4
    HEAPG = 5
    STACKA = 6
    STACKG = 7
    PRINT = 8
    FUNCCALL = 9
    PACKAGE = 10
    IMPORT = 11
    VAR = 12
    FUNCTION = 13
    CLOSE = 14
