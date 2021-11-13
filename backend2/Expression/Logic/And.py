from Abstract.Expression import Expression
from Environment.Environment import Environment
from Environment.Value import Value
from Enum.typeExpression import typeExpression
from Globales.Tablas import Errores
from datetime import datetime


class And(Expression):

    def __init__(self, left: Expression, right: Expression, line: str, col: str) -> None:
        super().__init__()
        self.leftExpression = left
        self.rightExpression = right
        self.line = line
        self.col = col

    def compile(self, environment: Environment) -> Value:

        self.leftExpression.generator = self.generator
        self.rightExpression.generator = self.generator

        leftValue: Value = self.leftExpression.compile(environment)
        rightValue: Value = self.rightExpression.compile(environment)

        if leftValue.type == typeExpression.BOOL:
            if rightValue.type == typeExpression.BOOL:

                newValue = Value("", False, typeExpression.BOOL)

                newLabelTrue = self.generator.newLabel()
                newLabelFalse = self.generator.newLabel()

                self.generator.addIf(leftValue.value, "1", "!=", newLabelFalse)
                self.generator.addIf(rightValue.value, "1", "!=", newLabelFalse)
                self.generator.addGoto(newLabelTrue)

                self.generator.addLabel(newLabelFalse)
                tmp = self.generator.newTemp()
                self.generator.addExpression(tmp, "0", "", "")
                newLabel = self.generator.newLabel()
                self.generator.addGoto(newLabel)
                self.generator.addLabel(newLabelTrue)
                self.generator.addExpression(tmp, "1", "", "")
                self.generator.addLabel(newLabel)

                newValue.value = tmp
                return newValue
            else:
                Errores.append({'Descripcion': "Error en And", 'Linea': self.line, 'Columna': self.col, 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                return Value("0", False, typeExpression.INTEGER)
        else:
            Errores.append({'Descripcion': "Error en And", 'Linea': self.line, 'Columna': self.col, 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            return Value("0", False, typeExpression.INTEGER)
