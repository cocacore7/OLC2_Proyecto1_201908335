from Abstract.Instruction import Instruction
from Environment.Environment import Environment
from Abstract.Expression import Expression
from Globales.Salida import contenido


class Print(Instruction):

    def __init__(self, expression: Expression) -> None:
        self.expression = expression

    def execute(self, environment: Environment):
        for ins in self.expression:
            tempExp = ins.execute(environment)
            contenido.append("P," + str(tempExp.getValue()))
            print(str(tempExp.getValue()))


class Println(Instruction):

    def __init__(self, expression: Expression) -> None:
        self.expression = expression

    def execute(self, environment: Environment):
        for ins in self.expression:
            tempExp = ins.execute(environment)
            contenido.append("L," + str(tempExp.getValue()))
            print(str(tempExp.getValue()))
