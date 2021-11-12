from Abstract.Expression import Expression
from Abstract.Instruction import Instruction
from Environment.Environment import Environment
from Environment.Value import Value
from Enum.typeExpression import typeExpression
from Globales.Tablas import Errores
from datetime import datetime


class Print(Instruction):

    def __init__(self, exp: Expression) -> None:
        super().__init__()
        self.exp = exp

    def compile(self, environment: Environment) -> Value:

        for i in self.exp:
            i.generator = self.generator
            tempValue: Value = i.compile(environment)

            if tempValue.type == typeExpression.INTEGER:
                self.generator.addPrintf("d", "int(" + str(tempValue.getValue())+")")

            elif tempValue.type == typeExpression.FLOAT:
                if tempValue.zero is not True:
                    self.generator.addPrintf("f", "float64(" + str(tempValue.getValue())+")")

            elif tempValue.type == typeExpression.CHAR:
                self.generator.addPrintf("c", "int(" + str(tempValue.getValue()) + ")")

            elif tempValue.type == typeExpression.BOOL:
                newLabel = self.generator.newLabel()
                newLabelTrue = self.generator.newLabel()
                newLabelFalse = self.generator.newLabel()
                self.generator.addIf(tempValue.value, "1", "==", newLabelTrue)
                self.generator.addGoto(newLabelFalse)
                self.generator.addLabel(newLabelTrue)
                self.generator.addCallFunc("print_true_proc")

                self.generator.addGoto(newLabel)
                self.generator.addLabel(newLabelFalse)
                self.generator.addCallFunc("print_false_proc")

                self.generator.addLabel(newLabel)

            elif tempValue.type == typeExpression.STRING:
                self.generator.addExpression("t12", tempValue.getValue(), "", "")
                self.generator.addCallFunc("print_String_proc")

            elif tempValue.type == typeExpression.INTEGERA:
                self.generator.addExpression("t11", tempValue.getValue(), "", "")
                self.generator.addCallFunc("print_Integer_Array_proc")

            elif tempValue.type == typeExpression.FLOATA:
                self.generator.addExpression("t11", tempValue.getValue(), "", "")
                self.generator.addCallFunc("print_Float_Array_proc")

            elif tempValue.type == typeExpression.CHARA:
                self.generator.addExpression("t11", tempValue.getValue(), "", "")
                self.generator.addCallFunc("print_Char_Array_proc")

            elif tempValue.type == typeExpression.BOOLA:
                self.generator.addExpression("t11", tempValue.getValue(), "", "")
                self.generator.addCallFunc("print_Bool_Array_proc")

            elif tempValue.type == typeExpression.STRINGA:
                self.generator.addExpression("t11", tempValue.getValue(), "", "")
                self.generator.addCallFunc("print_String_Array_proc")

            elif tempValue.type == typeExpression.NULO:
                self.generator.addCallFunc("print_nothing_proc")

            else:
                Errores.append({'Descripcion': "Error en Print", 'Linea': "0", 'Columna': "0", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        return Value("0", False, typeExpression.INTEGER)
