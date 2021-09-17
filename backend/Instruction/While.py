from Environment.Symbol import Symbol
from Environment.Environment import Environment
from Abstract.Instruction import Instruction
from Abstract.Expression import Expression
from Enum.TransferSentence import TransferSentence
from Globales.Tablas import Errores
from datetime import datetime


class While(Instruction):

    def __init__(self, condition: Expression, block) -> None:
        self.condition = condition
        self.block = block

    def execute(self, environment: Environment):

        tempCondition: Symbol = self.condition.execute(environment)

        if tempCondition.getValue() != 'nothing':
            while tempCondition.getValue():
                newEnv = Environment(environment)

                for ins in self.block:
                    temp = ins.execute(newEnv)
                    if temp is not None:
                        if temp.type == TransferSentence.RETURN:
                            temp.ciclo = True
                            return temp
                        elif temp.type == TransferSentence.BREAK:
                            return
                        elif temp.type == TransferSentence.CONTINUE:
                            break

                tempCondition = self.condition.execute(environment)
        else:
            Errores.append({'Descripcion': "Condicion While Invalida", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
