from Abstract.Expression import Expression
from Environment.Environment import Environment
from Environment.Value import Value
from Enum.typeExpression import typeExpression


class Division(Expression):

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
                if self.falseLabel == "":
                    self.falseLabel = self.generator.newLabel()
                if rightValue.getValue() == "0":
                    self.zero = True

                TempRigth = self.generator.newTemp()
                self.generator.addExpression(TempRigth, "float64("+rightValue.getValue()+")", "", "")
                self.generator.addIf(TempRigth, "0", "==", self.falseLabel)
                # Division entre 0
                newLabel = self.generator.newLabel()
                self.generator.addExpression(newTemp, "float64("+leftValue.getValue()+")", TempRigth, "/")
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
                print("Error en division")
                return Value("0", False, typeExpression.INTEGER)

        else:
            print("Error en resta")
            return Value("0", False, typeExpression.INTEGER)
