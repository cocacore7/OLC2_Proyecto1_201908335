from Abstract.Expression import Expression
from Abstract.Instruction import Instruction
from Environment.Environment import Environment
from Environment.Value import Value
from Enum.typeExpression import typeExpression
from Instruction.Break import Break
from Instruction.Return import Return
from Instruction.Continue import Continue
from Globales.Tablas import Errores
from datetime import datetime


class If(Instruction):

    def __init__(self, condition: Expression, blockif, blockelif, blockelse, line: str, col: str) -> None:
        super().__init__()
        self.condition = condition
        self.blockif = blockif
        self.blockelif = blockelif
        self.blockelse = blockelse
        self.truelabel = ""
        self.falselabel = ""
        self.LabelSalir = ""
        self.funtioncReturn = ""
        self.espacioReturn = 0
        self.line = line
        self.col = col

    def compile(self, environment: Environment) -> Value:
        self.condition.generator = self.generator
        valueCondition = self.condition.compile(environment)
        if valueCondition.trueLabel == "":
            valueCondition.trueLabel = self.generator.newLabel()
        if valueCondition.falseLabel == "":
            valueCondition.falseLabel = self.generator.newLabel()

        if valueCondition.type == typeExpression.BOOL:
            newLabel = self.generator.newLabel()
            self.generator.addIf(str(valueCondition.value), "1", "==", valueCondition.trueLabel)
            self.generator.addGoto(valueCondition.falseLabel)

            self.generator.addLabel(valueCondition.trueLabel)
            breakSentence = False
            for ins in self.blockif.block:
                ins.generator = self.generator
                if type(ins) == Continue:
                    ins.labelTrue = self.truelabel
                    breakSentence = True
                elif type(ins) == Break:
                    ins.labelFalse = self.falselabel
                    breakSentence = True
                elif type(ins) == Return:
                    ins.funtioncReturn = self.funtioncReturn
                    ins.espacioReturn = self.espacioReturn
                    if self.LabelSalir != "":
                        ins.tmpSalir = self.LabelSalir
                        breakSentence = True
                    else:
                        ins.tmpSalir = newLabel
                ins.compile(environment)
            if not breakSentence:
                self.generator.addGoto(newLabel)

            self.generator.addLabel(valueCondition.falseLabel)
            if len(self.blockelif) > 0:
                for i in self.blockelif:
                    i.condition.generator = self.generator
                    newValueCondition = i.condition.compile(environment)
                    if newValueCondition.trueLabel == "":
                        newValueCondition.trueLabel = self.generator.newLabel()
                    if newValueCondition.falseLabel == "":
                        newValueCondition.falseLabel = self.generator.newLabel()

                    if newValueCondition.type == typeExpression.BOOL:
                        self.generator.addIf(str(newValueCondition.value), "1", "==", newValueCondition.trueLabel)
                        self.generator.addGoto(newValueCondition.falseLabel)

                        self.generator.addLabel(newValueCondition.trueLabel)
                        for ins in i.blockif.block:
                            ins.generator = self.generator
                            if type(ins) == Continue:
                                ins.labelTrue = self.truelabel
                                breakSentence = True
                            elif type(ins) == Break:
                                ins.labelFalse = self.falselabel
                                breakSentence = True
                            elif type(ins) == Return:
                                ins.funtioncReturn = self.funtioncReturn
                                ins.espacioReturn = self.espacioReturn
                                if self.LabelSalir != "":
                                    ins.tmpSalir = self.LabelSalir
                                    breakSentence = True
                                else:
                                    ins.tmpSalir = newLabel
                            ins.compile(environment)
                        if not breakSentence:
                            self.generator.addGoto(newLabel)
                        self.generator.addLabel(newValueCondition.falseLabel)
                    else:
                        Errores.append({'Descripcion': "Error en Else If", 'Linea': self.line, 'Columna': self.col, 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})

            if len(self.blockelse.block) > 0:
                for ins in self.blockelse.block:
                    ins.generator = self.generator
                    if type(ins) == Continue:
                        ins.labelTrue = self.truelabel
                        breakSentence = True
                    elif type(ins) == Break:
                        ins.labelFalse = self.falselabel
                        breakSentence = True
                    elif type(ins) == Return:
                        ins.funtioncReturn = self.funtioncReturn
                        ins.espacioReturn = self.espacioReturn
                        if self.LabelSalir != "":
                            ins.tmpSalir = self.LabelSalir
                            breakSentence = True
                        else:
                            ins.tmpSalir = newLabel
                    ins.compile(environment)
            if not breakSentence:
                self.generator.addLabel(newLabel)
        else:
            Errores.append({'Descripcion': "Error en If", 'Linea': self.line, 'Columna': self.col, 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
