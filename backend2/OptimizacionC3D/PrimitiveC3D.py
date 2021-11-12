from AbstractC3D.ExpressionC3D import Expression
from Enum.typeExpresionC3D import typeExpression


class PrimitiveC3D(Expression):

    def __init__(self, value: str) -> None:
        super().__init__()
        self.value = value

    def getType(self) -> typeExpression:
        return typeExpression.PRIMITIVE

    def writeC3D(self) -> str:
        return str(self.value)
