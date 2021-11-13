from Abstract.Instruction import Instruction
from Abstract.Expression import Expression
from Environment.Environment import Environment
from Environment.Value import Value
from Enum.typeExpression import typeExpression
from Globales.Tablas import Errores
from datetime import datetime


class LowerCase(Instruction):

    def __init__(self, value: Expression, line: str, col: str) -> None:
        super().__init__()
        self.value = value
        self.line = line
        self.col = col

    def compile(self, environment: Environment) -> Value:
        self.value.generator = self.generator
        value = self.value.compile(environment)
        tmp = self.generator.newTemp()
        tmp2 = self.generator.newTemp()
        tmp3 = self.generator.newTemp()
        trueLabel = self.generator.newLabel()
        falseLabel = self.generator.newLabel()
        Label1 = self.generator.newLabel()
        Label2 = self.generator.newLabel()
        Label3 = self.generator.newLabel()
        Label4 = self.generator.newLabel()
        if value.type == typeExpression.STRING:
            self.generator.addExpression(tmp, value.getValue(), "", "")
            self.generator.addLabel(trueLabel)
            self.generator.addExpression(tmp2, "heap[int(" + tmp + ")]", "", "")
            self.generator.addIf(tmp2, "-1", "==", falseLabel)
            self.generator.addGoto(Label1)
            self.generator.addLabel(Label1)
            self.generator.addIf(tmp2, "64", ">", Label2)
            self.generator.addGoto(Label3)
            self.generator.addLabel(Label2)
            self.generator.addIf(tmp2, "91", "<", Label4)
            self.generator.addGoto(Label3)
            self.generator.addLabel(Label4)
            self.generator.addExpression(tmp3, tmp2, "32", "+")
            self.generator.addExpression("heap[int(" + tmp + ")]", tmp3, "", "")
            self.generator.addLabel(Label3)
            self.generator.addExpression(tmp, tmp, "1", "+")
            self.generator.addGoto(trueLabel)
            self.generator.addLabel(falseLabel)
            return value
        else:
            Errores.append({'Descripcion': "Error en LowerCase", 'Linea': self.line, 'Columna': self.col, 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            return Value("0", False, typeExpression.INTEGER)

