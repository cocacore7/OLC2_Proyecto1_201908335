from Enum.OperacionVaria import operacionVaria
from Enum.typeExpression import typeExpression
from Environment.Environment import Environment
from Environment.Symbol import Symbol
from Abstract.Expression import Expression
import math


def obtener(numero):
    if numero == 0:
        return "String"
    elif numero == 1:
        return "Int64"
    elif numero == 2:
        return "Float64"
    elif numero == 3:
        return "Bool"
    elif numero == 4:
        return "Char"
    elif numero == 5:
        return "Nothing"
    elif numero == 6:
        return "Error"


def Error():
    return Symbol(
        "",
        'nothing',
        typeExpression.NULO
    )


class FuncionVaria2(Expression):

    def __init__(self, type: typeExpression, rigthExp: Expression, operation: operacionVaria) -> None:
        self.type = type
        self.rigthExp = rigthExp
        self.operation = operation

    def execute(self, environment: Environment) -> Symbol:

        if self.type is None:
            Tipo = typeExpression.ERROR
        else:
            Tipo = self.type
        rigthValue = self.rigthExp.execute(environment)

        if self.operation == operacionVaria.PARSE:
            if Tipo == typeExpression.INTEGER:
                if rigthValue.getType() == typeExpression.STRING:
                    try:
                        return Symbol(
                            "",
                            int(rigthValue.getValue()),
                            typeExpression.INTEGER
                        )
                    except ValueError:
                        print("String Incorrecto, No Es Un Numero Int64: " + rigthValue.getValue())
                else:
                    print("Dato a Parsear Incorrecto " + rigthValue.getType() + ", Se Esperaba String")
            elif Tipo == typeExpression.FLOAT:
                if rigthValue.getType() == typeExpression.STRING:
                    try:
                        return Symbol(
                            "",
                            float(rigthValue.getValue()),
                            typeExpression.FLOAT
                        )
                    except ValueError:
                        print("String Incorrecto, No Es Un Numero Float64: " + rigthValue.getValue())
                else:
                    print("Dato a Parsear Incorrecto " + rigthValue.getType() + ", Se Esperaba String")
            else:
                if Tipo == typeExpression.ERROR:
                    print("Tipo De Dato A Parsear Incorrecto: Error, Se Esperaba Int64 o Float64")
                    return Error()
                else:
                    print("Tipo De Dato A Parsear Incorrecto: " + obtener(Tipo.value) + ", Se Esperaba Int64 o Float64")
                    return Error()

        elif self.operation == operacionVaria.TRUNC:
            if Tipo == typeExpression.INTEGER:
                if rigthValue.getType() == typeExpression.FLOAT:
                    return Symbol(
                        "",
                        math.trunc(rigthValue.getValue()),
                        typeExpression.INTEGER
                    )
                else:
                    print("Dato a Parsear Incorrecto " + rigthValue.getType() + ", Se Esperaba Float64")
            else:
                if Tipo == typeExpression.ERROR:
                    print("Tipo De Dato A Truncar Incorrecto: Error, Se Esperaba Int64")
                    return Error()
                else:
                    print("Tipo De Dato A Truncar Incorrecto: " + obtener(Tipo.value) + ", Se Esperaba Int64")
                    return Error()

        elif self.operation == operacionVaria.FLOAT:
            if rigthValue.getType() == typeExpression.INTEGER:
                return Symbol(
                    "",
                    float(rigthValue.getValue()),
                    typeExpression.FLOAT
                )
            else:
                print("Dato A Convertir Float Incorrecto: " + rigthValue.getType() + ", Se Esperaba Int64")

        elif self.operation == operacionVaria.STRING:
            if rigthValue.getType() == typeExpression.STRING:
                return Symbol(
                    "",
                    rigthValue.getValue(),
                    typeExpression.STRING
                )
            elif rigthValue.getType() == typeExpression.INTEGER:
                return Symbol(
                    "",
                    str(rigthValue.getValue()),
                    typeExpression.STRING
                )
            elif rigthValue.getType() == typeExpression.FLOAT:
                return Symbol(
                    "",
                    str(rigthValue.getValue()),
                    typeExpression.STRING
                )
            elif rigthValue.getType() == typeExpression.BOOL:
                return Symbol(
                    "",
                    str(rigthValue.getValue()),
                    typeExpression.STRING
                )
            elif rigthValue.getType() == typeExpression.CHAR:
                return Symbol(
                    "",
                    str(rigthValue.getValue()),
                    typeExpression.STRING
                )
            else:
                print("Dato A Convertir String Incorrecto: " + rigthValue.getType())

        elif self.operation == operacionVaria.TYPEOF:
            if rigthValue.getType() == typeExpression.STRING:
                return Symbol(
                    "",
                    "String",
                    typeExpression.STRING
                )
            elif rigthValue.getType() == typeExpression.INTEGER:
                return Symbol(
                    "",
                    "Int64",
                    typeExpression.STRING
                )
            elif rigthValue.getType() == typeExpression.FLOAT:
                return Symbol(
                    "",
                    "Float64",
                    typeExpression.STRING
                )
            elif rigthValue.getType() == typeExpression.BOOL:
                return Symbol(
                    "",
                    "Bool",
                    typeExpression.STRING
                )
            elif rigthValue.getType() == typeExpression.CHAR:
                return Symbol(
                    "",
                    "Char",
                    typeExpression.STRING
                )
            else:
                print("Dato A Convertir String Incorrecto: " + rigthValue.getType())
