from Abstract.Expression import Expression
from Environment.Environment import Environment
from Environment.Value import Value
from Enum.typeExpression import typeExpression


class Equal(Expression):

    def __init__(self, left: Expression, right: Expression) -> None:
        super().__init__()
        self.leftExpression = left
        self.rightExpression = right

    def compile(self, environment: Environment) -> Value:

        self.leftExpression.generator = self.generator
        self.rightExpression.generator = self.generator

        leftValue: Value = self.leftExpression.compile(environment)
        rightValue: Value = self.rightExpression.compile(environment)

        if leftValue.type == typeExpression.INTEGER or leftValue.type == typeExpression.FLOAT:
            if rightValue.type == typeExpression.INTEGER or rightValue.type == typeExpression.FLOAT:
                if self.trueLabel == "":
                    self.trueLabel = self.generator.newLabel()
                if self.falseLabel == "":
                    self.falseLabel = self.generator.newLabel()

                self.generator.addIf(leftValue.value, rightValue.value, "==", self.trueLabel)
                self.generator.addGoto(self.falseLabel)

                self.generator.addLabel(self.trueLabel)
                tmp = self.generator.newTemp()
                self.generator.addExpression(tmp, "1", "", "")
                newLabel = self.generator.newLabel()
                self.generator.addGoto(newLabel)
                self.generator.addLabel(self.falseLabel)
                self.generator.addExpression(tmp, "0", "", "")
                self.generator.addLabel(newLabel)

                return Value(tmp, True, typeExpression.BOOL)
            else:
                print("Error en igualdad")
                return Value("0", False, typeExpression.BOOL)

        elif leftValue.type == typeExpression.STRING:
            if rightValue.type == typeExpression.STRING:
                # Declaraciones
                str1 = self.generator.newTemp()
                str2 = self.generator.newTemp()
                str1c = self.generator.newTemp()
                str2c = self.generator.newTemp()
                valid1 = self.generator.newTemp()
                valid2 = self.generator.newTemp()
                labelCiclo = self.generator.newLabel()
                label1 = self.generator.newLabel()
                label2 = self.generator.newLabel()
                label3 = self.generator.newLabel()
                label4 = self.generator.newLabel()
                label5 = self.generator.newLabel()
                label6 = self.generator.newLabel()
                labelSalida = self.generator.newLabel()

                # Obtener H De Cadenas En Nuevos Temporales
                self.generator.addExpression(str1, leftValue.getValue(), "", "")
                self.generator.addExpression(str2, rightValue.getValue(), "", "")

                # L0
                self.generator.addLabel(labelCiclo)
                self.generator.addGetHeap(str1c, str1)
                self.generator.addGetHeap(str2c, str2)
                self.generator.addIf(str1c, "-1", "==", label1)
                self.generator.addGoto(label2)

                # L1
                self.generator.addLabel(label1)
                self.generator.addExpression(valid1, "1", "", "")
                self.generator.addGoto(label3)

                # L2
                self.generator.addLabel(label2)
                self.generator.addExpression(valid1, "0", "", "")

                # L3
                self.generator.addLabel(label3)
                self.generator.addIf(str2c, "-1", "==", label4)
                self.generator.addGoto(label5)

                # L4
                self.generator.addLabel(label4)
                self.generator.addExpression(valid2, "1", "", "")
                self.generator.addIf(valid1, "1", "==", labelSalida)
                self.generator.addExpression(valid2, "0", "", "")
                self.generator.addGoto(labelSalida)

                # L5
                self.generator.addLabel(label5)
                self.generator.addExpression(valid2, "0", "", "")
                self.generator.addIf(valid1, "1", "==", labelSalida)
                # Aqui va (==, !=, <, >, <=, >=) ----------------------
                self.generator.addIf(str1c, str2c, "==", label6)
                # -----------------------------------------------------
                self.generator.addGoto(labelSalida)

                # L6
                self.generator.addLabel(label6)
                self.generator.addExpression(str1, str1, "1", "+")
                self.generator.addExpression(str2, str2, "1", "+")
                self.generator.addGoto(labelCiclo)
                self.generator.addLabel(labelSalida)

                return Value(valid2, True, typeExpression.BOOL)
            else:
                print("Error en igualdad")
                return Value("0", False, typeExpression.BOOL)

        else:
            print("Error en igualdad")
            return Value("0", False, typeExpression.BOOL)
