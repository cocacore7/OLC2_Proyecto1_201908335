from Abstract.Instruction import Instruction
from Environment.Environment import Environment
from Abstract.Expression import Expression
from Salida import contenido


class Print(Instruction):

    def __init__(self, expression: Expression) -> None:
        self.expression = expression

    def execute(self, environment: Environment):
        tempExp = self.expression.execute(environment)
        contenido.append(str(tempExp.getValue()))
