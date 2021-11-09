from Environment.Symbol import Symbol
from Abstract.Expression import Expression
from Abstract.Instruction import Instruction
from Environment.Environment import Environment
from Environment.Value import Value
from Enum.typeExpression import typeExpression


class Declaration(Instruction):

    def __init__(self, id: str, exp: Expression, type: typeExpression, isArray: bool, tipoD: str, entorno: str) -> None:
        super().__init__()
        self.id = id
        self.exp = exp
        self.type = type
        self.isArray = isArray
        self.tipoD = tipoD
        self.entorno = entorno

    def compile(self, environment: Environment) -> Value:
        self.exp.generator = self.generator
        newValue: Value = self.exp.compile(environment)
        if not self.isArray:
            tempVar: Symbol = environment.saveVariable(self.id, newValue.type, self.isArray, self.tipoD,
                                                       self.entorno, "")
        else:
            tempVar: Symbol = environment.saveVariable(self.id, newValue.type, self.isArray, self.tipoD,
                                                       self.entorno, self.id)
        if newValue.type != typeExpression.NULO:
            self.generator.addSetStack(str(tempVar.position), newValue.getValue())


