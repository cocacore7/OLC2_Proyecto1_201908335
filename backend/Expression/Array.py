from Environment.Environment import Environment
from Environment.Symbol import Symbol
from Abstract.Expression import Expression
from Enum.typeExpression import typeExpression
from Globales.Tablas import Errores
from datetime import datetime


class Array(Expression):

    def __init__(self, listExp, type: typeExpression) -> None:
        self.listExp = listExp
        self.type = type

    def execute(self, environment: Environment) -> Symbol:
        tempExp = []
        cualquiera = typeExpression.NULO
        for exp in self.listExp:
            if type(exp) != Symbol:
                exp = exp.execute(environment)
            if self.type == typeExpression.ANY:
                if cualquiera == typeExpression.NULO:
                    cualquiera = tipoExpR1(exp.type)
                else:
                    cualquiera = tipoExpR2(cualquiera, exp.type)
            else:
                if self.type == typeExpression.INTEGERA:
                    if exp.type != typeExpression.INTEGER:
                        Errores.append({'Descripcion': "Los tipos no coinciden, Se obtuvo un " + obtener(exp.type.value) + ", Se Esperaba Un Int64", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                        break
                    else:
                        cualquiera = typeExpression.INTEGERA
                elif self.type == typeExpression.FLOATA:
                    if exp.type != typeExpression.FLOAT:
                        
                        Errores.append({'Descripcion': "Los tipos no coinciden, Se obtuvo un " + obtener(exp.type.value) + ", Se Esperaba Un Float64", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                        break
                    else:
                        cualquiera = typeExpression.FLOATA
                elif self.type == typeExpression.STRINGA:
                    if exp.type != typeExpression.STRING:
                        Errores.append({'Descripcion': "Los tipos no coinciden, Se obtuvo un " + obtener(exp.type.value) + ", Se Esperaba Un String", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                        break
                    else:
                        cualquiera = typeExpression.STRINGA
                elif self.type == typeExpression.CHARA:
                    if exp.type != typeExpression.CHAR:
                        Errores.append({'Descripcion': "Los tipos no coinciden, Se obtuvo un " + obtener(exp.type.value) + ", Se Esperaba Un Char", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                        break
                    else:
                        cualquiera = typeExpression.CHARA
                elif self.type == typeExpression.BOOLA:
                    if exp.type != typeExpression.BOOL:
                        Errores.append({'Descripcion': "Los tipos no coinciden, Se obtuvo un " + obtener(exp.type.value) + ", Se Esperaba Un Bool", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                        break
                    else:
                        cualquiera = typeExpression.BOOLA
                else:
                    Errores.append({'Descripcion': "Declaracion Incorrecta: " + obtener(self.type.value) + ", No es Tipo Array", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                    break
            tempExp.append(exp)

        tempSymbol: Symbol = Symbol('', tempExp, cualquiera)
        tempSymbol.array = True

        return tempSymbol


def tipoExpR1(type: typeExpression):
    if type == typeExpression.INTEGER:
        return typeExpression.INTEGERA
    elif type == typeExpression.FLOAT:
        return typeExpression.FLOATA
    elif type == typeExpression.STRING:
        return typeExpression.STRINGA
    elif type == typeExpression.CHAR:
        return typeExpression.CHARA
    elif type == typeExpression.BOOL:
        return typeExpression.BOOLA
    elif type == typeExpression.INTEGERA:
        return typeExpression.INTEGERA
    elif type == typeExpression.FLOATA:
        return typeExpression.FLOATA
    elif type == typeExpression.STRINGA:
        return typeExpression.STRINGA
    elif type == typeExpression.CHARA:
        return typeExpression.CHARA
    elif type == typeExpression.BOOLA:
        return typeExpression.BOOLA
    else:
        return typeExpression.NULO


def tipoExpR2(cond: typeExpression, type: typeExpression):
    if cond == typeExpression.INTEGER:
        if type != typeExpression.INTEGER:
            return typeExpression.ANY
    elif cond == "Float64":
        if type != typeExpression.FLOAT:
            return typeExpression.ANY
    elif cond == "String":
        if type != typeExpression.STRING:
            return typeExpression.ANY
    elif cond == "Char":
        if type != typeExpression.CHAR:
            return typeExpression.ANY
    elif cond == "Bool":
        if type != typeExpression.BOOL:
            return typeExpression.ANY
    elif cond == "Nothing":
        if type != typeExpression.NULO:
            return typeExpression.ANY
    else:
        return cond


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
