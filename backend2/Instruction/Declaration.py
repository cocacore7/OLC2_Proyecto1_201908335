from Environment.Symbol import Symbol
from Abstract.Expression import Expression
from Abstract.Instruction import Instruction
from Environment.Environment import Environment
from Environment.Value import Value
from Enum.typeExpression import typeExpression
from Expression.Primitive.ArrayHeap import ArrayHeap


class Declaration(Instruction):

    def __init__(self, id: str, exp: Expression, type: typeExpression, isArray: bool, tipoD: str, entorno: str, line: str, col: str) -> None:
        super().__init__()
        self.id = id
        self.exp = exp
        self.type = type
        self.isArray = isArray
        self.tipoD = tipoD
        self.entorno = entorno
        self.line = line
        self.col = col

    def compile(self, environment: Environment) -> Value:
        self.exp.generator = self.generator
        newValue: Value = self.exp.compile(environment)
        if not self.isArray:
            tempVar: Symbol = environment.saveVariable(self.id, newValue.type, self.isArray, self.tipoD,
                                                       self.entorno, "", self.line, self.col)
            if newValue.type != typeExpression.NULO:
                self.generator.addSetStack(str(tempVar.position), newValue.getValue())
        else:
            crear = ArrayHeap(newValue.array, newValue.type)
            crear.generator = self.generator
            nuevo = crear.compile(environment)
            newValue.value = nuevo.array[0]
            tempVar: Symbol = environment.saveVariable(self.id, newValue.type, self.isArray, self.tipoD,
                                                       self.entorno, self.id, self.line, self.col)
            if newValue.type != typeExpression.NULO:
                self.generator.addSetStack(str(tempVar.position), newValue.getValue())
