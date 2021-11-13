from Abstract.Expression import Expression
from Abstract.Instruction import Instruction
from Environment.Environment import Environment
from Environment.Value import Value
from Enum.typeExpression import typeExpression
from Instruction.If import If
from Instruction.Break import Break
from Instruction.Continue import Continue
from Globales.Tablas import Errores
from datetime import datetime


class While(Instruction):

    def __init__(self, condition: Expression, block, line: str, col: str) -> None:
        super().__init__()
        self.condition = condition
        self.block = block
        self.funtioncReturn = ""
        self.LabelSalir = ""
        self.espacioReturn = 0
        self.line = line
        self.col = col

    def compile(self, environment: Environment) -> Value:
        self.condition.generator = self.generator

        newLabel = self.generator.newLabel()
        self.generator.addLabel(newLabel)

        valueCondition = self.condition.compile(environment)
        if valueCondition.trueLabel == "":
            valueCondition.trueLabel = self.generator.newLabel()
        if valueCondition.falseLabel == "":
            valueCondition.falseLabel = self.generator.newLabel()

        if valueCondition.type == typeExpression.BOOL:
            self.generator.addIf(str(valueCondition.value), "1", "==", valueCondition.trueLabel)
            self.generator.addGoto(valueCondition.falseLabel)
            self.generator.addLabel(valueCondition.trueLabel)

            newEnv = Environment(environment)
            ContinueSentence = False
            for ins in self.block:
                ins.generator = self.generator
                if type(ins) == If:
                    ins.funtioncReturn = self.funtioncReturn
                    ins.LabelSalir = self.LabelSalir
                    ins.truelabel = newLabel
                    ins.falselabel = valueCondition.falseLabel
                    ins.espacioReturn = self.espacioReturn
                elif type(ins) == Break:
                    ins.labelFalse = valueCondition.falseLabel
                    ContinueSentence = True
                elif type(ins) == Continue:
                    ins.labelFalse = newLabel
                    ContinueSentence = True
                ins.compile(newEnv)
            if not ContinueSentence:
                self.generator.addGoto(newLabel)
            self.generator.addLabel(valueCondition.falseLabel)
        else:
            Errores.append({'Descripcion': "Error en While", 'Linea': self.line, 'Columna': self.col, 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
