from re import M
from Abstract.Instruction import Instruction
from Environment.Environment import Environment
from Abstract.Expression import Expression
from Environment.Symbol import Symbol
from Globales.Salida import contenido


class Print(Instruction):

    def __init__(self, expression: Expression) -> None:
        self.expression = expression

    def execute(self, environment: Environment):
        mensaje = ""
        for ins in self.expression:
            tempExp = ins.execute(environment)
            if not tempExp.isArray():
                if type(tempExp.value) is Symbol:
                    tempExp.value = tempExp.value.getValue()
                mensaje = mensaje + str(tempExp.getValue())
            else:
                mensaje = mensaje + str(self.printArray(tempExp.getValue(), "", False))
        contenido.append("P," + mensaje)

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
        mensaje = ""
        for ins in self.expression:
            tempExp = ins.execute(environment)
            if not tempExp.isArray():
                if type(tempExp.value) is Symbol:
                    tempExp.value = tempExp.value.getValue()
                mensaje = mensaje + str(tempExp.getValue())
            else:
                mensaje = mensaje + str(self.printArray(tempExp.getValue(), "", False))
        contenido.append("L," + mensaje)

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

