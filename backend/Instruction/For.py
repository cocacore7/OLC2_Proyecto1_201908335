from Environment.Symbol import Symbol
from Environment.Environment import Environment
from Abstract.Instruction import Instruction
from Abstract.Expression import Expression
from Enum.typeExpression import typeExpression
from Enum.TransferSentence import TransferSentence


class For(Instruction):

    def __init__(self, parameter, lefthExp: Expression, rigthExp: Expression, block) -> None:
        self.parameter = parameter
        self.lefthExp = lefthExp
        self.rigthExp = rigthExp
        self.block = block

    def execute(self, environment: Environment):

        lefthExp: Symbol = self.lefthExp.execute(environment)
        rigthExp: Symbol = self.rigthExp.execute(environment)

        newEnvP = Environment(environment)
        if self.parameter.type is not None:
            if self.parameter.type != lefthExp.type:
                print("Los tipos De Dato Especificados No Son Iguales: " + obtener(lefthExp.type.value) + " y " + obtener(
                    rigthExp.type.value))
                return
        else:
            self.parameter.type = lefthExp.type

        if rigthExp.type != typeExpression.NULO:
            if lefthExp.type == typeExpression.INTEGER:
                if rigthExp.type == typeExpression.INTEGER:
                    if lefthExp.value <= rigthExp.value:
                        for i in range(lefthExp.value, rigthExp.value + 1):
                            self.parameter.setValue(i)
                            newEnvP.saveParameter(self.parameter.id, self.parameter, self.parameter.type,
                                                  self.parameter.isArray)
                            newEnv = Environment(newEnvP)
                            for ins in self.block:
                                temp = ins.execute(newEnv)
                                if temp is not None:
                                    if temp.type == TransferSentence.RETURN:
                                        temp.ciclo = True
                                        return temp
                                    elif temp.type == TransferSentence.BREAK:
                                        return
                                    elif temp.type == TransferSentence.CONTINUE:
                                        break
                    else:
                        print("El Valor Izquierdo Es Menor Al Derecho: " + str(lefthExp.value) + " y " + str(
                            rigthExp.value))
                        return
                else:
                    print("Los tipos De Dato Especificados No Son Validos: " + obtener(lefthExp.type.value) + " y " + obtener(
                        rigthExp.type.value))
                    return
            else:
                print("Los tipos De Dato Especificados No Son Validos: " + obtener(lefthExp.type.value) + " y " + obtener(
                    rigthExp.type.value))
                return
        else:
            if lefthExp.type == typeExpression.STRING:
                for i in lefthExp.value:
                    self.parameter.setValue(i)
                    newEnvP.saveParameter(self.parameter.id, self.parameter, self.parameter.type,
                                          self.parameter.isArray)
                    newEnv = Environment(newEnvP)
                    for ins in self.block:
                        temp = ins.execute(newEnv)
                        if temp is not None:
                            if temp.type == TransferSentence.RETURN:
                                temp.ciclo = True
                                return temp
                            elif temp.type == TransferSentence.BREAK:
                                return
                            elif temp.type == TransferSentence.CONTINUE:
                                break
            # Aqui Va El De Arreglos Tambien
            else:
                print("El tipo De Dato Especificado No Es Valido: " + obtener(lefthExp.type.value))
                return


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
