from Abstract.Expression import Expression
from Environment.Environment import Environment
from Environment.Value import Value
from Enum.typeExpression import typeExpression
from Globales.Tablas import Errores
from datetime import datetime


class Division(Expression):

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

        newTemp = self.generator.newTemp()

        if leftValue.type == typeExpression.INTEGER or leftValue.type == typeExpression.FLOAT:
            if rightValue.type == typeExpression.INTEGER or rightValue.type == typeExpression.FLOAT:
                if self.falseLabel == "":
                    self.falseLabel = self.generator.newLabel()
                if rightValue.getValue() == "0":
                    self.zero = True

                self.generator.addIf(rightValue.getValue(), "0", "==", self.falseLabel)
                # Division entre 0
                tmpizq = self.generator.newTemp()
                newLabel = self.generator.newLabel()
                self.generator.addExpression(tmpizq, "float64("+rightValue.getValue()+")", "", "")
                self.generator.addExpression(newTemp, "float64("+leftValue.getValue()+")", tmpizq, "/")
                self.generator.addGoto(newLabel)
                self.generator.addLabel(self.falseLabel)
                self.generator.addCallFunc("math_error_proc")
                self.generator.addLabel(newLabel)

                retorno = Value(newTemp, True, typeExpression.FLOAT)
                retorno.trueLabel = self.trueLabel
                retorno.falseLabel = self.falseLabel
                retorno.zero = self.zero
                return retorno
            else:
                Errores.append({'Descripcion': "Error en Division", 'Linea': self.line, 'Columna': self.col, 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                return Value("0", False, typeExpression.INTEGER)

        else:
            Errores.append({'Descripcion': "Error en Division", 'Linea': self.line, 'Columna': self.col, 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            return Value("0", False, typeExpression.INTEGER)
