from Abstract.Expression import Expression
from Environment.Environment import Environment
from Environment.Value import Value
from Enum.typeExpression import typeExpression
from Globales.Tablas import Errores
from datetime import datetime


class Multiply(Expression):

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
                self.generator.addExpression(newTemp, leftValue.getValue(), rightValue.getValue(), "*")
                return Value(newTemp, True, rightValue.type)
            else:
                Errores.append({'Descripcion': "Error en Multiplicacion", 'Linea': "0", 'Columna': "0", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                return Value("0", False, typeExpression.INTEGER)

        elif leftValue.type == typeExpression.FLOAT:
            if rightValue.type == typeExpression.INTEGER or rightValue.type == typeExpression.FLOAT:
                self.generator.addExpression(newTemp, leftValue.getValue(), rightValue.getValue(), "*")
                return Value(newTemp, True, typeExpression.FLOAT)
            else:
                Errores.append({'Descripcion': "Error en Multiplicacion", 'Linea': "0", 'Columna': "0", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                return Value("0", False, typeExpression.INTEGER)

        elif leftValue.type == typeExpression.STRING:
            if rightValue.type == typeExpression.STRING:
                # String Derecha Izquierda Procesado = right + lefth
                self.generator.addActHeap(newTemp)

                # String 1
                self.generator.addExpression("t12", leftValue.getValue(), "", "")
                self.generator.addCallFunc("concatenate_strings_proc")

                # String 2
                self.generator.addExpression("t12", rightValue.getValue(), "", "")
                self.generator.addCallFunc("concatenate_strings_proc")
                self.generator.addSetHeap("H", str(-1))
                self.generator.addNextHeap()

                return Value(newTemp, False, typeExpression.STRING)

            else:
                Errores.append({'Descripcion': "Error en Concatenacion", 'Linea': "0", 'Columna': "0", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                return Value("0", False, typeExpression.INTEGER)

        else:
            Errores.append({'Descripcion': "Error en Multiplicacion", 'Linea': "0", 'Columna': "0", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            return Value("0", False, typeExpression.INTEGER)
