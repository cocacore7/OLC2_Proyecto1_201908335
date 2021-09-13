from Instruction.Parameter import Parameter
from Instruction.Function import Function
from Abstract.Instruction import Instruction
from Environment.Environment import Environment
from Enum.TransferSentence import TransferSentence


class CallFuncSt(Instruction):

    def __init__(self, id, parameters) -> None:
        self.id = id
        self.parameters = parameters

    def execute(self, environment: Environment):
        tempFunc: Function = environment.getGlobal().getFunction(self.id)

        if len(self.parameters) == len(tempFunc.parameters):
            for x in range(0, len(tempFunc.parameters)):
                tempPar: Parameter = tempFunc.parameters[x]
                tempPar.setValue(self.parameters[x])

            temp = tempFunc.executeFunction(environment)
            if temp is not None:
                if temp.type == TransferSentence.RETURN:
                    return temp.exp
                elif temp.type == TransferSentence.BREAK:
                    print("Sentencias Break Incorrecta, No Se Permite En Funciones")
                    return
                elif temp.type == TransferSentence.CONTINUE:
                    print("Sentencias Continue Incorrecta, No Se Permite En Funciones")
                    return
        else:
            print("Cantidad De Parametros Y Valores Enviados No Es Igual")
            return

