from Environment.Symbol import Symbol
from Environment.Environment import Environment
from Abstract.Instruction import Instruction
from Abstract.Expression import Expression
from Enum.typeExpression import typeExpression


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
                print("Los tipos De Dato Especificados No Son Iguales: " + obtener(lefthExp.type) + " y " + obtener(
                    rigthExp.type))
                return
        else:
            self.parameter.type = lefthExp.type

        if rigthExp.type != typeExpression.NULO:
            if lefthExp.type == typeExpression.INTEGER:
                if rigthExp.type == typeExpression.INTEGER:
                    if lefthExp.value < rigthExp.value:
                        for i in range(lefthExp.value, rigthExp.value + 1):
                            self.parameter.setValue(i)
                            newEnvP.saveParameter(self.parameter.id, self.parameter, self.parameter.type,
                                                  self.parameter.isArray)
                            newEnv = Environment(newEnvP)
                            for ins in self.block:
                                ins.execute(newEnv)
                    else:
                        print("El Valor Izquierdo Es Menor Al Derecho: " + str(lefthExp.value) + " y " + str(
                            rigthExp.value))
                        return
                else:
                    print("Los tipos De Dato Especificados No Son Validos: " + obtener(lefthExp.type) + " y " + obtener(
                        rigthExp.type))
                    return
            else:
                print("Los tipos De Dato Especificados No Son Validos: " + obtener(lefthExp.type) + " y " + obtener(
                    rigthExp.type))
                return
        else:
            if lefthExp.type == typeExpression.STRING:
                for i in lefthExp.value:
                    self.parameter.setValue(i)
                    newEnvP.saveParameter(self.parameter.id, self.parameter, self.parameter.type,
                                          self.parameter.isArray)
                    newEnv = Environment(newEnvP)
                    for ins in self.block:
                        ins.execute(newEnv)
            # Aqui Va El De Arreglos Tambien
            else:
                print("El tipo De Dato Especificado No Es Valido: " + obtener(lefthExp.type))
                return


def obtener(a: typeExpression):
    if a == typeExpression.INTEGER:
        return "Int64"
    elif a == typeExpression.FLOAT:
        return "Float64"
    elif a == typeExpression.STRING:
        return "String"
    elif a == typeExpression.CHAR:
        return "Char"
    elif a == typeExpression.BOOL:
        return "Bool"
    elif a == typeExpression.NULO:
        return "Nothing"
    elif a == typeExpression.ERROR:
        return "Error"
