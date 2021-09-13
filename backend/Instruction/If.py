from Environment.Symbol import Symbol
from Environment.Environment import Environment
from Abstract.Instruction import Instruction
from Abstract.Expression import Expression
from Enum.typeExpression import typeExpression
from Enum.TransferSentence import TransferSentence


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
                temp = self.block.execute(environment)
                if temp is not None:
                    if temp.type == TransferSentence.RETURN:
                        return temp
                    elif temp.type == TransferSentence.BREAK:
                        return temp
                    elif temp.type == TransferSentence.CONTINUE:
                        return temp
            else:
                if len(self.elifBlock) > 0:
                    verdadero = False
                    for i in range(len(self.elifBlock)):
                        tempCondition: Symbol = self.elifBlock[i].condition.execute(environment)
                        if tempCondition.getType() == typeExpression.BOOL:
                            if tempCondition.getValue():
                                temp = self.elifBlock[i].block.execute(environment)
                                if temp is not None:
                                    if temp.type == TransferSentence.RETURN:
                                        return temp
                                    elif temp.type == TransferSentence.BREAK:
                                        return temp
                                    elif temp.type == TransferSentence.CONTINUE:
                                        return temp
                                verdadero = True
                                break
                    if not verdadero:
                        temp = self.elseBlock.execute(environment)
                        if temp is not None:
                            if temp.type == TransferSentence.RETURN:
                                return temp
                            elif temp.type == TransferSentence.BREAK:
                                return temp
                            elif temp.type == TransferSentence.CONTINUE:
                                return temp
                else:
                    temp = self.elseBlock.execute(environment)
                    if temp is not None:
                        if temp.type == TransferSentence.RETURN:
                            return temp
                        elif temp.type == TransferSentence.BREAK:
                            return temp
                        elif temp.type == TransferSentence.CONTINUE:
                            return temp
        else:
            print("Condicion Incorrecta, No es Booleana")
