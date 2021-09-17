from Enum.relationalOperation import relationalOperation
from Enum.typeExpression import typeExpression
from Environment.Environment import Environment
from Environment.Symbol import Symbol
from Abstract.Expression import Expression
from Instruction.Parameter import Parameter
from Globales.Tablas import Errores
from datetime import datetime


class Relational(Expression):

    def __init__(self, leftExp: Expression, rightExp: Expression, operation: relationalOperation) -> None:
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

        if self.operation == relationalOperation.MAYOR:
            if leftValue.getType() == typeExpression.STRING:
                if rightValue.getType() == typeExpression.STRING:
                    return Symbol(
                        "",
                        leftValue.getValue() > rightValue.getValue(),
                        typeExpression.BOOL
                    )
                else:
                    Errores.append({'Descripcion': "No Se Permite Evaluar Operacion Mayor Con " + str(rightValue.getValue()) + " y " + str(leftValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            elif leftValue.getType() == typeExpression.INTEGER:
                if rightValue.getType() == typeExpression.FLOAT:
                    return Symbol(
                        "",
                        int(leftValue.getValue()) > float(rightValue.getValue()),
                        typeExpression.BOOL
                    )
                elif rightValue.getType() == typeExpression.INTEGER:
                    return Symbol(
                        "",
                        int(leftValue.getValue()) > int(rightValue.getValue()),
                        typeExpression.BOOL
                    )
                else:
                    Errores.append({'Descripcion': "No Se Permite Evaluar Operacion Mayor Con " + str(rightValue.getValue()) + " y " + str(leftValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            elif leftValue.getType() == typeExpression.FLOAT:
                if rightValue.getType() == typeExpression.FLOAT:
                    return Symbol(
                        "",
                        float(leftValue.getValue()) > float(rightValue.getValue()),
                        typeExpression.BOOL
                    )
                elif rightValue.getType() == typeExpression.INTEGER:
                    return Symbol(
                        "",
                        float(leftValue.getValue()) > int(rightValue.getValue()),
                        typeExpression.BOOL
                    )
                else:
                    Errores.append({'Descripcion': "No Se Permite Evaluar Operacion Mayor Con " + str(rightValue.getValue()) + " y " + str(leftValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            else:
                Errores.append({'Descripcion': "No Se Permite Evaluar Operacion Mayor Con " + str(rightValue.getValue()) + " y " + str(leftValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})

        elif self.operation == relationalOperation.MENOR:
            if leftValue.getType() == typeExpression.STRING:
                if rightValue.getType() == typeExpression.STRING:
                    return Symbol(
                        "",
                        leftValue.getValue() < rightValue.getValue(),
                        typeExpression.BOOL
                    )
                else:
                    Errores.append({'Descripcion': "No Se Permite Evaluar Operacion Menor Con " + str(rightValue.getValue()) + " y " + str(leftValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            elif leftValue.getType() == typeExpression.INTEGER:
                if rightValue.getType() == typeExpression.FLOAT:
                    return Symbol(
                        "",
                        int(leftValue.getValue()) < float(rightValue.getValue()),
                        typeExpression.BOOL
                    )
                elif rightValue.getType() == typeExpression.INTEGER:
                    return Symbol(
                        "",
                        int(leftValue.getValue()) < int(rightValue.getValue()),
                        typeExpression.BOOL
                    )
                else:
                    Errores.append({'Descripcion': "No Se Permite Evaluar Operacion Menor Con " + str(rightValue.getValue()) + " y " + str(leftValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            elif leftValue.getType() == typeExpression.FLOAT:
                if rightValue.getType() == typeExpression.FLOAT:
                    return Symbol(
                        "",
                        float(leftValue.getValue()) < float(rightValue.getValue()),
                        typeExpression.BOOL
                    )
                elif rightValue.getType() == typeExpression.INTEGER:
                    return Symbol(
                        "",
                        float(leftValue.getValue()) < int(rightValue.getValue()),
                        typeExpression.BOOL
                    )
                else:
                    Errores.append({'Descripcion': "No Se Permite Evaluar Operacion Menor Con " + str(rightValue.getValue()) + " y " + str(leftValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            else:
                Errores.append({'Descripcion': "No Se Permite Evaluar Operacion Menor Con " + str(rightValue.getValue()) + " y " + str(leftValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})

        elif self.operation == relationalOperation.MAYORIGUAL:
            if leftValue.getType() == typeExpression.STRING:
                if rightValue.getType() == typeExpression.STRING:
                    return Symbol(
                        "",
                        leftValue.getValue() >= rightValue.getValue(),
                        typeExpression.BOOL
                    )
                else:
                    Errores.append({'Descripcion': "No Se Permite Evaluar Operacion Mayor Igual Con " + str(rightValue.getValue()) + " y " + str(leftValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            elif leftValue.getType() == typeExpression.INTEGER:
                if rightValue.getType() == typeExpression.FLOAT:
                    return Symbol(
                        "",
                        int(leftValue.getValue()) >= float(rightValue.getValue()),
                        typeExpression.BOOL
                    )
                elif rightValue.getType() == typeExpression.INTEGER:
                    return Symbol(
                        "",
                        int(leftValue.getValue()) >= int(rightValue.getValue()),
                        typeExpression.BOOL
                    )
                else:
                    Errores.append({'Descripcion': "No Se Permite Evaluar Operacion Mayor Igual Con " + str(rightValue.getValue()) + " y " + str(leftValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            elif leftValue.getType() == typeExpression.FLOAT:
                if rightValue.getType() == typeExpression.FLOAT:
                    return Symbol(
                        "",
                        float(leftValue.getValue()) >= float(rightValue.getValue()),
                        typeExpression.BOOL
                    )
                elif rightValue.getType() == typeExpression.INTEGER:
                    return Symbol(
                        "",
                        float(leftValue.getValue()) >= int(rightValue.getValue()),
                        typeExpression.BOOL
                    )
                else:
                    Errores.append({'Descripcion': "No Se Permite Evaluar Operacion Mayor Igual Con " + rightValue.getValue() + " y " + leftValue.getValue(), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            else:
                Errores.append({'Descripcion': "No Se Permite Evaluar Operacion Mayor Con Igual " + str(rightValue.getValue()) + " y " + str(leftValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})

        elif self.operation == relationalOperation.MENORIGUAL:
            if leftValue.getType() == typeExpression.STRING:
                if rightValue.getType() == typeExpression.STRING:
                    return Symbol(
                        "",
                        leftValue.getValue() <= rightValue.getValue(),
                        typeExpression.BOOL
                    )
                else:
                    Errores.append({'Descripcion': "No Se Permite Evaluar Operacion Menor Igual Con " + str(rightValue.getValue()) + " y " + str(leftValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            elif leftValue.getType() == typeExpression.INTEGER:
                if rightValue.getType() == typeExpression.FLOAT:
                    return Symbol(
                        "",
                        int(leftValue.getValue()) <= float(rightValue.getValue()),
                        typeExpression.BOOL
                    )
                elif rightValue.getType() == typeExpression.INTEGER:
                    return Symbol(
                        "",
                        int(leftValue.getValue()) <= int(rightValue.getValue()),
                        typeExpression.BOOL
                    )
                else:
                    Errores.append({'Descripcion': "No Se Permite Evaluar Operacion Menor Igual Con " + str(rightValue.getValue()) + " y " + str(leftValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            elif leftValue.getType() == typeExpression.FLOAT:
                if rightValue.getType() == typeExpression.FLOAT:
                    return Symbol(
                        "",
                        float(leftValue.getValue()) <= float(rightValue.getValue()),
                        typeExpression.BOOL
                    )
                elif rightValue.getType() == typeExpression.INTEGER:
                    return Symbol(
                        "",
                        float(leftValue.getValue()) <= int(rightValue.getValue()),
                        typeExpression.BOOL
                    )
                else:
                    Errores.append({'Descripcion': "No Se Permite Evaluar Operacion Menor Igual Con " + str(rightValue.getValue()) + " y " + str(leftValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            else:
                Errores.append({'Descripcion': "No Se Permite Evaluar Operacion Menor Igual Con " + str(rightValue.getValue()) + " y " + str(leftValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})

        elif self.operation == relationalOperation.IGUAL:
            return Symbol(
                "",
                leftValue.getValue() == rightValue.getValue(),
                typeExpression.BOOL
            )

        elif self.operation == relationalOperation.DISTINTO:
            return Symbol(
                "",
                leftValue.getValue() != rightValue.getValue(),
                typeExpression.BOOL
            )

        return Symbol("", 'nothing', typeExpression.NULO)
