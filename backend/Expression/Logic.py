from Enum.LogicOperation import logicOperation
from Enum.typeExpression import typeExpression
from Environment.Environment import Environment
from Environment.Symbol import Symbol
from Abstract.Expression import Expression
from Instruction.Parameter import Parameter
from Globales.Tablas import Errores
from datetime import datetime


class Logic(Expression):

    def __init__(self, leftExp: Expression, rightExp: Expression, operation: logicOperation) -> None:
        self.leftExp = leftExp
        self.rightExp = rightExp
        self.operation = operation

    def execute(self, environment: Environment) -> Symbol:

        leftValue = self.leftExp.execute(environment)
        if type(leftValue) is Parameter:
            if type(leftValue.value) is Symbol:
                leftValue = leftValue.value
        rightValue = self.rightExp.execute(environment)
        if type(rightValue) is Parameter:
            if type(rightValue.value) is Symbol:
                rightValue.value = rightValue.value.getValue()

        if self.operation == logicOperation.AND:
            if leftValue.getType() == typeExpression.BOOL:
                if rightValue.getType() == typeExpression.BOOL:
                    return Symbol(
                        "",
                        leftValue.getValue() and rightValue.getValue(),
                        typeExpression.BOOL
                    )
                else:
                    Errores.append({'Descripcion': "No Se Permite Evaluar And De " + str(rightValue.getValue()) + " y " + str(leftValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            else:
                Errores.append({'Descripcion': "No Se Permite Evaluar And De " + str(rightValue.getValue()) + " y " + str(leftValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})

        elif self.operation == logicOperation.OR:
            if leftValue.getType() == typeExpression.BOOL:
                if rightValue.getType() == typeExpression.BOOL:
                    return Symbol(
                        "",
                        leftValue.getValue() or rightValue.getValue(),
                        typeExpression.BOOL
                    )
                else:
                    Errores.append({'Descripcion': "No Se Permite Evaluar Or De " + str(rightValue.getValue()) + " y " + str(leftValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            else:
                Errores.append({'Descripcion': "No Se Permite Evaluar Or De " + str(rightValue.getValue()) + " y " + str(leftValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})

        elif self.operation == logicOperation.NOT:
            if leftValue.getType() == typeExpression.BOOL:
                return Symbol(
                    "",
                    not leftValue.getValue(),
                    typeExpression.BOOL
                )
            else:
                Errores.append({'Descripcion': "No Se Permite Evaluar Not De " + str(leftValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})

        return Symbol("", 'nothing', typeExpression.NULO)
