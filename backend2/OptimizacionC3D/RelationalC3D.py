from AbstractC3D.ExpressionC3D import Expression
from Enum.typeExpresionC3D import typeExpression


class RelationalC3D(Expression):

    def __init__(self, lefth: Expression, rigth: Expression, operation: typeExpression) -> None:
        super().__init__()
        self.left = lefth
        self.rigth = rigth
        self.operation = operation

    def getType(self) -> typeExpression:
        return self.operation

    def writeC3D(self) -> str:
        operator = ""
        if self.operation == typeExpression.IGUAL:
            operator = "=="
        elif self.operation == typeExpression.DISTINTO:
            operator = "!="
        elif self.operation == typeExpression.MAYOR:
            operator = ">"
        elif self.operation == typeExpression.MAYORIGUAL:
            operator = ">="
        elif self.operation == typeExpression.MENOR:
            operator = "<"
        elif self.operation == typeExpression.MENORIGUAL:
            operator = "<="

        return self.left.writeC3D() + " " + operator + " " + self.rigth.writeC3D()
