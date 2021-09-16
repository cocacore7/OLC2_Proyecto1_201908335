from Expression.Primitive import Primitive
from Abstract.Instruction import Instruction
from Environment.Environment import Environment
from Abstract.Expression import Expression
from Enum.typeExpression import typeExpression
from Environment.Symbol import Symbol
from Expression.VariableCall import VariableCall
from Expression.ArrayCall import ArrayCall
from Instruction.Parameter import Parameter


class Declaration(Instruction):

    def __init__(self, id: str, value: Expression, type: typeExpression, isArray: bool, tipoD: str, entorno: str) -> None:
        self.id = id
        self.value = value
        self.type = type
        self.isArray = isArray
        self.tipoD = tipoD
        self.entorno = entorno

    def execute(self, environment: Environment):

        if self.value is not None:
            if not isinstance(self.value, list):
                tempValue = self.value.execute(environment)
                if self.type is not None:
                    if self.type != typeExpression.NULO:
                        if self.type.value != tempValue.getType().value:
                            print("Los tipos no coinciden, Se obtuvo un " + obtener(
                                tempValue.getType().value) + ", Se Esperaba Un " + obtener(self.type.value))
                            environment.saveVariable(self.id, Primitive('nothing', typeExpression.NULO).execute(environment), typeExpression.NULO, False, self.tipoD, self.entorno, "")
                            return
                        if tempValue.isArray():
                            if type(self.value) == VariableCall:
                                environment.saveVariable(self.id, tempValue, self.type, self.isArray, self.tipoD, self.entorno, self.value.id)
                                environment.saveVariable(self.value.id, tempValue, self.type, self.isArray, "", "", self.value.id)
                            elif type(self.value) == ArrayCall:
                                environment.saveVariable(self.id, tempValue, self.type, self.isArray, self.tipoD, self.entorno, obtenerID(self.value))
                                environment.saveVariable(obtenerID(self.value), tempValue, self.type, self.isArray, "", "", obtenerID(self.value))
                        else:
                            environment.saveVariable(self.id, tempValue, self.type, self.isArray, self.tipoD, self.entorno, "")
                    else:
                        if tempValue.isArray():
                            if type(self.value) == VariableCall:
                                environment.saveVariable(self.id, tempValue, tempValue.getType(), self.isArray, self.tipoD, self.entorno, self.value.id)
                                environment.saveVariable(self.value.id, tempValue, tempValue.getType(), self.isArray, "", "", self.value.id)
                            elif type(self.value) == ArrayCall:
                                environment.saveVariable(self.id, tempValue, tempValue.getType(), self.isArray, "", "", obtenerID(self.value))
                                environment.saveVariable(obtenerID(self.value), tempValue, tempValue.getType(), self.isArray, "", "", obtenerID(self.value))
                        else:
                            environment.saveVariable(self.id, tempValue, tempValue.getType(), self.isArray, self.tipoD, self.entorno, "")
                else:
                    print("Tipo De Dato Incorrecto, Se Esperaba: String, Int64, Float64, Bool o Char")
                    environment.saveVariable(self.id, Primitive('nothing', typeExpression.NULO).execute(environment),
                                             typeExpression.NULO, False, self.tipoD, self.entorno, "")
            else:
                tempExp = []
                for i in self.value:
                    tempExp.append(i.execute(environment))
                if self.type != typeExpression.ANY:
                    for i in tempExp:
                        if self.type == typeExpression.INTEGERA:
                            if i.getType() != typeExpression.INTEGER:
                                print("Los tipos no coinciden, Se obtuvo un " + obtener(
                                    i.getType().value) + ", Se Esperaba Un Int64")

                                tempSymbol: Symbol = Symbol('', [], typeExpression.ANY)
                                tempSymbol.array = True
                                environment.saveVariable(self.id, tempSymbol, typeExpression.ANY, True, self.tipoD,
                                                         self.entorno, "")
                                return
                        elif self.type == typeExpression.FLOATA:
                            if i.getType() != typeExpression.FLOAT:
                                print("Los tipos no coinciden, Se obtuvo un " + obtener(
                                    i.getType().value) + ", Se Esperaba Un Float64")

                                tempSymbol: Symbol = Symbol('', [], typeExpression.ANY)
                                tempSymbol.array = True
                                environment.saveVariable(self.id, tempSymbol, typeExpression.ANY, True, self.tipoD,
                                                         self.entorno, "")
                                return
                        elif self.type == typeExpression.STRINGA:
                            if i.getType() != typeExpression.STRING:
                                print("Los tipos no coinciden, Se obtuvo un " + obtener(
                                    i.getType().value) + ", Se Esperaba Un String")

                                tempSymbol: Symbol = Symbol('', [], typeExpression.ANY)
                                tempSymbol.array = True
                                environment.saveVariable(self.id, tempSymbol, typeExpression.ANY, True, self.tipoD,
                                                         self.entorno, "")
                                return
                        elif self.type == typeExpression.BOOLA:
                            if i.getType() != typeExpression.BOOL:
                                print("Los tipos no coinciden, Se obtuvo un " + obtener(
                                    i.getType().value) + ", Se Esperaba Un Bool")

                                tempSymbol: Symbol = Symbol('', [], typeExpression.ANY)
                                tempSymbol.array = True
                                environment.saveVariable(self.id, tempSymbol, typeExpression.ANY, True, self.tipoD,
                                                         self.entorno, "")
                                return
                        elif self.type == typeExpression.CHARA:
                            if i.getType() != typeExpression.CHAR:
                                print("Los tipos no coinciden, Se obtuvo un " + obtener(
                                    i.getType().value) + ", Se Esperaba Un Char")

                                tempSymbol: Symbol = Symbol('', [], typeExpression.ANY)
                                tempSymbol.array = True
                                environment.saveVariable(self.id, tempSymbol, typeExpression.ANY, True, self.tipoD,
                                                         self.entorno, "")
                                return
                        else:
                            print("Declaracion Incorrecta: " + obtener(self.type.value) + ", No es Tipo Array")

                            tempSymbol: Symbol = Symbol('', [], typeExpression.ANY)
                            tempSymbol.array = True
                            environment.saveVariable(self.id, tempSymbol, typeExpression.ANY, True, self.tipoD,
                                                     self.entorno, "")
                            return

                    tempSymbol: Symbol = Symbol('', tempExp, self.type)
                    tempSymbol.array = True
                    environment.saveVariable(self.id, tempSymbol, self.type, self.isArray, self.tipoD, self.entorno, "")
                else:
                    tempSymbol: Symbol = Symbol('', tempExp, self.type)
                    tempSymbol.array = True
                    environment.saveVariable(self.id, tempSymbol, self.type, self.isArray, self.tipoD, self.entorno, "")
        else:

            environment.saveVariable(self.id, Primitive('nothing', typeExpression.NULO).execute(environment),
                                     typeExpression.NULO, False, self.tipoD, self.entorno, "")


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


def obtenerID(i):
    if type(i) == ArrayCall:
        a = obtenerID(i.array)
        return a
    else:
        return i.id
