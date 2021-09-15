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
        return "Array{String}"
    elif numero == 7:
        return "Array{Int64}"
    elif numero == 8:
        return "Array{Float64}"
    elif numero == 9:
        return "Array{Bool}"
    elif numero == 10:
        return "Array{Char}"
    elif numero == 11:
        return "Array{Any}"


class FuncionVaria2(Expression):

    def __init__(self, type: typeExpression, rigthExp: Expression, operation: operacionVaria) -> None:
        self.type = type
        self.rigthExp = rigthExp
        self.operation = operation

    def execute(self, environment: Environment) -> Symbol:

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
                    print("Dato a Parsear Incorrecto " + str(rigthValue.getValue()) + ", Se Esperaba String")
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
                    print("Dato a Parsear Incorrecto " + str(rigthValue.getValue()) + ", Se Esperaba String")
            else:
                print("Tipo De Dato A Parsear Incorrecto: " + obtener(Tipo.value) + ", Se Esperaba Int64 o Float64")

        elif self.operation == operacionVaria.TRUNC:
            if Tipo == typeExpression.INTEGER:
                if rigthValue.getType() == typeExpression.FLOAT:
                    return Symbol(
                        "",
                        math.trunc(rigthValue.getValue()),
                        typeExpression.INTEGER
                    )
                else:
                    print("Dato a Parsear Incorrecto " + str(rigthValue.getValue()) + ", Se Esperaba Float64")
            else:
                print("Tipo De Dato A Truncar Incorrecto: " + obtener(Tipo.value) + ", Se Esperaba Int64")

        elif self.operation == operacionVaria.FLOAT:
            if rigthValue.getType() == typeExpression.INTEGER:
                return Symbol(
                    "",
                    float(rigthValue.getValue()),
                    typeExpression.FLOAT
                )
            else:
                print("Dato A Convertir Float Incorrecto: " + str(rigthValue.getValue()) + ", Se Esperaba Int64")

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
                print("Dato A Convertir String Incorrecto: " + str(rigthValue.getValue()))

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
                print("Dato A Convertir String Incorrecto: " + str(rigthValue.getValue()))

        elif self.operation == operacionVaria.LENGTH:
            if rigthValue.getType() == typeExpression.ANY:
                return Symbol(
                    "",
                    len(rigthValue.value),
                    typeExpression.INTEGER
                )
            elif rigthValue.getType() == typeExpression.INTEGERA:
                return Symbol(
                    "",
                    len(rigthValue.value),
                    typeExpression.INTEGER
                )
            elif rigthValue.getType() == typeExpression.FLOATA:
                return Symbol(
                    "",
                    len(rigthValue.value),
                    typeExpression.INTEGER
                )
            elif rigthValue.getType() == typeExpression.STRINGA:
                return Symbol(
                    "",
                    len(rigthValue.value),
                    typeExpression.INTEGER
                )
            elif rigthValue.getType() == typeExpression.CHARA:
                return Symbol(
                    "",
                    len(rigthValue.value),
                    typeExpression.INTEGER
                )
            elif rigthValue.getType() == typeExpression.BOOLA:
                return Symbol(
                    "",
                    len(rigthValue.value),
                    typeExpression.INTEGER
                )
            else:
                print("Funcion Length Invalida Para: " + str(rigthValue.getValue()))

        return Symbol("", 'nothing', typeExpression.NULO)
