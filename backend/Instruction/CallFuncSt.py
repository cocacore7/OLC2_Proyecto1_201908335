from Instruction.Parameter import Parameter
from Instruction.Function import Function
from Abstract.Instruction import Instruction
from Environment.Environment import Environment


class CallFuncSt(Instruction):

    def __init__(self, id, parameters) -> None:
        self.id = id
        self.parameters = parameters

    def execute(self, environment: Environment):
        tempFunc: Function = environment.getFunction(self.id)
        newEnvironment = Environment(environment.getGlobal())

        for x in range(0, len(tempFunc.parameters)):
            tempPar: Parameter = tempFunc.parameters[x]
            tempPar.setValue(self.parameters[x])

        tempFunc.executeFunction(newEnvironment)
