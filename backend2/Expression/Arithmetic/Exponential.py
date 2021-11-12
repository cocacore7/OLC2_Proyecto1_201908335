from Abstract.Expression import Expression
from Environment.Environment import Environment
from Environment.Value import Value
from Enum.typeExpression import typeExpression
from Globales.Tablas import Errores
from datetime import datetime


class Exponential(Expression):

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

        if leftValue.type == typeExpression.INTEGER or leftValue.type == typeExpression.FLOAT:
            if rightValue.type == typeExpression.INTEGER or rightValue.type == typeExpression.FLOAT:
                tmp1 = self.generator.newTemp()
                tmp2 = self.generator.newTemp()
                Label1 = self.generator.newLabel()
                Label2 = self.generator.newLabel()
                Label3 = self.generator.newLabel()
                self.generator.addExpression(tmp1, "0", "", "")
                self.generator.addExpression(tmp2, "1", "", "")
                self.generator.addLabel(Label1)
                self.generator.addIf(tmp1, rightValue.getValue(), "!=", Label2)
                self.generator.addGoto(Label3)
                self.generator.addLabel(Label2)
                self.generator.addExpression(tmp2, tmp2, leftValue.getValue(), "*")
                self.generator.addExpression(tmp1, tmp1, "1", "+")
                self.generator.addGoto(Label1)
                self.generator.addLabel(Label3)

                return Value(tmp2, True, leftValue.type)
            else:
                Errores.append({'Descripcion': "Error en Exponencial", 'Linea': "0", 'Columna': "0", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                return Value("0", False, typeExpression.INTEGER)

        elif leftValue.type == typeExpression.STRING:
            if rightValue.type == typeExpression.INTEGER:
                tmpr = self.generator.newTemp()
                tmp = self.generator.newTemp()
                LabelTrue = self.generator.newLabel()
                LabelFalse = self.generator.newLabel()

                self.generator.addExpression(tmp, rightValue.getValue(), "", "")

                self.generator.addActHeap(tmpr)
                self.generator.addLabel(LabelTrue)
                self.generator.addExpression(tmp, tmp, "1", "-")
                self.generator.addExpression("t12", leftValue.getValue(), "", "")
                self.generator.addCallFunc("concatenate_strings_proc")
                self.generator.addIf(tmp, "0", "==", LabelFalse)
                self.generator.addGoto(LabelTrue)
                self.generator.addLabel(LabelFalse)
                self.generator.addSetHeap("H", str(-1))
                self.generator.addNextHeap()

                return Value(tmpr, True, leftValue.type)
            else:
                Errores.append({'Descripcion': "Error en Concatenacion", 'Linea': "0", 'Columna': "0", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        else:
            Errores.append({'Descripcion': "Error en Exponencial", 'Linea': "0", 'Columna': "0", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            return Value("0", False, typeExpression.INTEGER)
