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
                contenido.append("P," + str(self.printArray(tempExp.getValue(), "", False)))
                print(str(self.printArray(tempExp.getValue(), "", False)))

    def printArray(self, arr, mensaje: str, sig: bool):
        mensaje = mensaje + "[ "
        for i in range(len(arr)):
            if arr[i].isArray():
                if (i+1) >= len(arr):
                    mensaje = self.printArray(arr[i].getValue(), mensaje, False)
                else:
                    mensaje = self.printArray(arr[i].getValue(), mensaje, True)
            else:
                if i == (len(arr)-1):
                    mensaje += str(arr[i].getValue()) + " "
                else:
                    mensaje += str(arr[i].getValue()) + ", "
        if sig:
            mensaje = mensaje + "], "
        else:
            mensaje = mensaje + "] "
        return mensaje


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
                contenido.append("L," + str(self.printArray(tempExp.getValue(), "", False)))
                print(str(self.printArray(tempExp.getValue(), "", False)))

    def printArray(self, arr, mensaje: str, sig: bool):
        mensaje = mensaje + "[ "
        for i in range(len(arr)):
            if arr[i].isArray():
                if (i+1) >= len(arr):
                    mensaje = self.printArray(arr[i].getValue(), mensaje, False)
                else:
                    mensaje = self.printArray(arr[i].getValue(), mensaje, True)
            else:
                if i == (len(arr)-1):
                    mensaje += str(arr[i].getValue()) + " "
                else:
                    mensaje += str(arr[i].getValue()) + ", "
        if sig:
            mensaje = mensaje + "], "
        else:
            mensaje = mensaje + "] "
        return mensaje

