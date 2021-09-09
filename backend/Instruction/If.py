from Environment.Symbol import Symbol
from Environment.Environment import Environment
from Abstract.Instruction import Instruction
from Abstract.Expression import Expression
from Enum.typeExpression import typeExpression


class If(Instruction):

    def __init__(self, condition: Expression, block, elifBlock, elseBlock) -> None:
        self.condition = condition
        self.block = block
        self.elifBlock = elifBlock
        self.elseBlock = elseBlock

    def execute(self, environment: Environment):

        tempCondition: Symbol = self.condition.execute(environment)

        if tempCondition.getType() == typeExpression.BOOL:
            if tempCondition.getValue():
                self.block.execute(environment)
            else:
                if len(self.elifBlock) > 0:
                    verdadero = False
                    for i in range(len(self.elifBlock)):
                        tempCondition: Symbol = self.elifBlock[i].condition.execute(environment)
                        if tempCondition.getType() == typeExpression.BOOL:
                            if tempCondition.getValue():
                                self.elifBlock[i].block.execute(environment)
                                verdadero = True
                                break
                    if not verdadero:
                        self.elseBlock.execute(environment)
                else:
                    self.elseBlock.execute(environment)
        else:
            print("Evaluar Elseifs y else")
