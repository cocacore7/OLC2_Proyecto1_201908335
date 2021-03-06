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


class For(Instruction):

    def __init__(self, param: Instruction, ExpIzq: Expression, ExpDer: Expression, block, line: str, col: str) -> None:
        super().__init__()
        self.param = param
        self.ExpIzq = ExpIzq
        self.ExpDer = ExpDer
        self.block = block
        self.LabelSalir = ""
        self.funtioncReturn = ""
        self.espacioReturn = 0
        self.line = line
        self.col = col

    def compile(self, environment: Environment) -> Value:
        self.ExpIzq.generator = self.generator
        self.ExpDer.generator = self.generator

        leftValue = self.ExpIzq.compile(environment)
        rigthValue = self.ExpDer.compile(environment)

        if leftValue.type == typeExpression.INTEGER:
            if rigthValue.type == typeExpression.INTEGER:
                if leftValue.trueLabel == "":
                    leftValue.trueLabel = self.generator.newLabel()
                if leftValue.falseLabel == "":
                    leftValue.falseLabel = self.generator.newLabel()

                newTemp = self.generator.newTemp()
                self.generator.addExpression(newTemp, leftValue.getValue(), "", "")

                newLabel = self.generator.newLabel()
                self.generator.addLabel(newLabel)
                EnvParam = Environment(environment)
                self.param.value = newTemp
                self.param.type = leftValue.type
                self.param.generator = self.generator
                self.param.compile(EnvParam)

                self.generator.addIf(newTemp, str(rigthValue.value), "<=", leftValue.trueLabel)
                self.generator.addGoto(leftValue.falseLabel)

                self.generator.addLabel(leftValue.trueLabel)
                newEnv = Environment(EnvParam)
                newLabelFalse = self.generator.newLabel()
                ContinueSentence = False
                for ins in self.block:
                    ins.generator = self.generator
                    if type(ins) == If:
                        ins.funtioncReturn = self.funtioncReturn
                        ins.LabelSalir = self.LabelSalir
                        ins.truelabel = newLabelFalse
                        ins.falselabel = leftValue.falseLabel
                        ins.espacioReturn = self.espacioReturn
                    elif type(ins) == Break:
                        ins.labelFalse = leftValue.falseLabel
                    elif type(ins) == Continue:
                        ins.labelFalse = newLabelFalse
                        ContinueSentence = True
                    ins.compile(newEnv)
                if not ContinueSentence:
                    self.generator.addGoto(newLabelFalse)
                self.generator.addLabel(newLabelFalse)
                self.generator.addExpression(newTemp, newTemp, "1", "+")
                self.generator.addGoto(newLabel)

                self.generator.addLabel(leftValue.falseLabel)
            else:
                Errores.append({'Descripcion': "Tipo De Dato Exp Derecha De For Incorrecta", 'Linea': self.line, 'Columna': self.col, 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})

        elif leftValue.type == typeExpression.STRING:
            if leftValue.trueLabel == "":
                leftValue.trueLabel = self.generator.newLabel()
            if leftValue.falseLabel == "":
                leftValue.falseLabel = self.generator.newLabel()

            newTemp = self.generator.newTemp()
            self.generator.addExpression(newTemp, leftValue.getValue(), "", "")

            newLabel = self.generator.newLabel()
            self.generator.addLabel(newLabel)
            EnvParam = Environment(environment)
            self.param.value = newTemp
            self.param.type = typeExpression.CHAR
            self.param.generator = self.generator
            self.param.compile(EnvParam)

            tmpizq = self.generator.newTemp()
            self.generator.addExpression(tmpizq, "heap[int("+newTemp+")]", "", "")
            self.generator.addIf(tmpizq, "-1", "!=", leftValue.trueLabel)
            self.generator.addGoto(leftValue.falseLabel)

            self.generator.addLabel(leftValue.trueLabel)
            newEnv = Environment(EnvParam)
            newLabelFalse = self.generator.newLabel()
            ContinueSentence = False
            for ins in self.block:
                ins.generator = self.generator
                if type(ins) == If:
                    ins.truelabel = newLabelFalse
                    ins.falselabel = leftValue.falseLabel
                elif type(ins) == Break:
                    ins.labelFalse = leftValue.falseLabel
                elif type(ins) == Continue:
                    ins.labelFalse = newLabelFalse
                    ContinueSentence = True
                ins.compile(newEnv)
            if not ContinueSentence:
                self.generator.addGoto(newLabelFalse)
            self.generator.addLabel(newLabelFalse)
            self.generator.addExpression(newTemp, newTemp, "1", "+")
            self.generator.addGoto(newLabel)

            self.generator.addLabel(leftValue.falseLabel)
        else:
            Errores.append({'Descripcion': "Tipo De Dato Exp Izquierda De For Incorrecta", 'Linea': self.line, 'Columna': self.col, 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
