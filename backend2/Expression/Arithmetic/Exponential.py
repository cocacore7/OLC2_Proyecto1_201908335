from Abstract.Expression import Expression
from Environment.Environment import Environment
from Environment.Value import Value
from Enum.typeExpression import typeExpression


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
                if int(rightValue.getValue()) == 0:
                    self.generator.addExpression(newTemp, leftValue.getValue(), "1", "*")
                    return Value(newTemp, True, leftValue.type)
                elif int(rightValue.getValue()) == 1:
                    self.generator.addExpression(newTemp, leftValue.getValue(), "1", "*")
                    return Value(newTemp, True, leftValue.type)
                elif int(rightValue.getValue()) == 2:
                    self.generator.addExpression(newTemp, leftValue.getValue(), leftValue.getValue(), "*")
                    return Value(newTemp, True, leftValue.type)
                elif int(rightValue.getValue()) > 2:
                    self.generator.addExpression(newTemp, leftValue.getValue(), leftValue.getValue(), "*")
                    ant = None
                    for x in range(int(rightValue.getValue())-2):
                        tmp2 = self.generator.newTemp()
                        if x == 0:
                            self.generator.addExpression(tmp2, newTemp, leftValue.getValue(), "*")
                            ant = tmp2
                        else:
                            self.generator.addExpression(tmp2, ant, leftValue.getValue(), "*")
                            ant = tmp2
                    return Value(ant, True, leftValue.type)
                else:
                    print("Error en exponencial")
                    return Value("0", False, typeExpression.INTEGER)
            else:
                print("Error en exponencial")
                return Value("0", False, typeExpression.INTEGER)

        elif leftValue.type == typeExpression.STRING:
            if rightValue.type == typeExpression.INTEGER:
                tmpr = self.generator.newTemp()
                tmp = self.generator.newTemp()
                tmp2 = self.generator.newTemp()
                LabelTrue = self.generator.newLabel()
                LabelFalse = self.generator.newLabel()

                self.generator.addExpression(tmp, rightValue.getValue(), "", "")

                self.generator.addActHeap(tmpr)
                self.generator.addLabel(LabelTrue)
                self.generator.addExpression(tmp, tmp, "1", "-")
                self.generator.getPointerP(tmp2)
                self.generator.setPointerP(leftValue.getValue())
                self.generator.addCallFunc("concatenate_strings_proc")
                self.generator.setPointerP(tmp2)
                self.generator.addIf(tmp, "0", "==", LabelFalse)
                self.generator.addGoto(LabelTrue)
                self.generator.addLabel(LabelFalse)
                self.generator.addSetHeap("H", str(-1))
                self.generator.addNextHeap()

                return Value(tmpr, True, leftValue.type)

        else:
            print("Error en exponencial")
            return Value("0", False, typeExpression.INTEGER)
