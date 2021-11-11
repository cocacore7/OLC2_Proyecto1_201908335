from Abstract.Expression import Expression
from Environment.Environment import Environment
from Environment.Value import Value
from Enum.typeExpression import typeExpression
from Globales.Tablas import Errores
from datetime import datetime


class Mod(Expression):

    def __init__(self, left: Expression, right: Expression) -> None:
        super().__init__()
        self.leftExpression = left
        self.rightExpression = right

    def compile(self, environment: Environment) -> Value:

        self.leftExpression.generator = self.generator
        self.rightExpression.generator = self.generator

        leftValue: Value = self.leftExpression.compile(environment)
        rightValue: Value = self.rightExpression.compile(environment)

        newTemp = self.generator.newTemp()

        if leftValue.type == typeExpression.INTEGER:
            if rightValue.type == typeExpression.INTEGER or rightValue.type == typeExpression.FLOAT:
                self.generator.addExpressionMod(newTemp, leftValue.getValue(), rightValue.getValue())
                return Value(newTemp, True, rightValue.type)
            else:
                Errores.append({'Descripcion': "Error en Modulo", 'Linea': "0", 'Columna': "0", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                return Value("0", False, typeExpression.INTEGER)

        elif leftValue.type == typeExpression.FLOAT:
            if rightValue.type == typeExpression.INTEGER or rightValue.type == typeExpression.FLOAT:
                self.generator.addExpressionMod(newTemp, leftValue.getValue(), rightValue.getValue())
                return Value(newTemp, True, typeExpression.FLOAT)
            else:
                Errores.append({'Descripcion': "Error en Modulo", 'Linea': "0", 'Columna': "0", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                return Value("0", False, typeExpression.INTEGER)

        else:
            Errores.append({'Descripcion': "Error en Modulo", 'Linea': "0", 'Columna': "0", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            return Value("0", False, typeExpression.INTEGER)
