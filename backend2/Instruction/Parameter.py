from Environment.Value import Value
from Environment.Environment import Environment
from Environment.Symbol import Symbol
from Enum.typeExpression import typeExpression
from Abstract.Instruction import Instruction


class Parameter(Instruction):

    def __init__(self, id: str, type: typeExpression, line: str, col: str) -> None:
        super().__init__()
        self.id = id
        self.type = type
        self.value = ""
        self.array = False
        self.line = line
        self.col = col

    def compile(self, environment: Environment) -> Value:
        tempVar: Symbol = environment.saveParameter(self.id, self.type, self.array, "", self.line, self.col)
        self.generator.addSetStack(str(tempVar.position), self.value)

    def getId(self):
        return self.id

    def getType(self):
        return self.type

    def isArray(self):
        return self.array
