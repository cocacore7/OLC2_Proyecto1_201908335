from abc import ABC, abstractclassmethod
from Enum.typeExpression import typeExpression


class Expression(ABC):

    def __init__(self) -> None:
        super().__init__()

    @abstractclassmethod
    def getType(self) -> typeExpression:
        pass

    @abstractclassmethod
    def writeC3D(self) -> str:
        pass
