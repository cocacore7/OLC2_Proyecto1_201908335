from Abstract.Instruction import Instruction
from Environment.Environment import Environment
from Abstract.Expression import Expression
from Globales.Salida import contenido


class Print(Instruction):

    def __init__(self, expression: Expression) -> None:
        self.expression = expression

    def execute(self, environment: Environment):
        for ins in self.expression:
            tempExp = ins.execute(environment)
            if not tempExp.isArray():
                contenido.append("P," + str(tempExp.getValue()))
                print(str(tempExp.getValue()))
            else:
                contenido.append("P," + str(self.printArray(tempExp.getValue(), "")))
                print(str(self.printArray(tempExp.getValue(), "")))


class Println(Instruction):

    def __init__(self, expression: Expression) -> None:
        self.expression = expression

    def execute(self, environment: Environment):
        for ins in self.expression:
            tempExp = ins.execute(environment)
            if not tempExp.isArray():
                contenido.append("L," + str(tempExp.getValue()))
                print(str(tempExp.getValue()))
            else:
                contenido.append("L," + str(self.printArray(tempExp.getValue(), "")))
                print(str(self.printArray(tempExp.getValue(), "")))

    def printArray(self, arr, mensaje: str):
        mensaje = mensaje + "["
        for i in range(len(arr) - 1):
            if arr[i].isArray():
                mensaje = self.printArray2(arr[i].getValue(), mensaje)
            else:
                mensaje += str(arr[i].getValue()) + ", "
        if len(arr) != 0:
            if arr[len(arr) - 1].isArray():
                mensaje = self.printArray2(arr[len(arr) - 1].getValue(), mensaje)
                mensaje = mensaje + "] "
            else:
                mensaje += str(arr[len(arr) - 1].getValue())
                mensaje = mensaje + "] "
        return mensaje

    def printArray2(self, arr, mensaje: str):
        mensaje = mensaje + "["
        for i in range(len(arr) - 1):
            if arr[i].isArray():
                mensaje = self.printArray2(arr[i].getValue(), mensaje)
            else:
                mensaje += str(arr[i].getValue()) + ", "
        if len(arr) != 0:
            if arr[len(arr) - 1].isArray():
                mensaje = self.printArray2(arr[len(arr) - 1].getValue(), mensaje)
                mensaje = mensaje + "], "
            else:
                mensaje += str(arr[len(arr) - 1].getValue())
                mensaje = mensaje + "] "
        return mensaje
