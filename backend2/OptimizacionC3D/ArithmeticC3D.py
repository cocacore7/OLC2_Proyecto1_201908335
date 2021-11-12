from AbstractC3D.ExpressionC3D import Expression
from Enum.typeExpresionC3D import typeExpression


class ArithmeticC3D(Expression):

    def __init__(self, lefth: Expression, rigth: Expression, operation: typeExpression) -> None:
        super().__init__()
        self.left = lefth
        self.rigth = rigth
        self.operation = operation

    def getType(self) -> typeExpression:
        return self.operation

    def writeC3D(self) -> str:
        operator = ""
        if self.operation == typeExpression.PLUS:
            operator = "+"
        elif self.operation == typeExpression.MINUS:
            operator = "-"
        elif self.operation == typeExpression.MULTIPLY:
            operator = "*"
        elif self.operation == typeExpression.DIV:
            operator = "/"
        elif self.operation == typeExpression.MOD:
            return "math.Mod( " + self.left.writeC3D() + ", " + self.rigth.writeC3D() + " )"
        elif self.operation == typeExpression.NEG:
            return "-" + self.left.writeC3D()
        elif self.operation == typeExpression.PRIMITIVE:
            return self.left.writeC3D()

        return self.left.writeC3D() + " " + operator + " " + self.rigth.writeC3D()
