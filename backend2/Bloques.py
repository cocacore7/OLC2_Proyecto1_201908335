from Enum.typeExpresionC3D import typeExpression
from Enum.typeInstructionC3D import typeInstruction


class Bloques:

    def __init__(self) -> None:
        self.bloquesBasicos = []

    def crearBloques(self, C3D):
        bloqueTemp = []
        bloqueTemp2 = []
        for ins in C3D:
            if ins.getType() == typeInstruction.LABEL:
                bloqueTemp2 = []
                for ins2 in bloqueTemp:
                    bloqueTemp2.append(ins2)
                self.bloquesBasicos.append(bloqueTemp2)

                bloqueTemp = []
            elif ins.getType() == typeInstruction.GOTO:
                bloqueTemp2 = []
                for ins2 in bloqueTemp:
                    bloqueTemp2.append(ins2)
                self.bloquesBasicos.append(bloqueTemp2)

                bloqueTemp = []
            bloqueTemp.append(ins)
        for ins2 in bloqueTemp:
            bloqueTemp2 = [ins2]
            self.bloquesBasicos.append(bloqueTemp2)

    def imprimirBloques(self):
        outText = ""
        for bloque in self.bloquesBasicos:
            for ins in bloque:
                if ins.write:
                    outText = outText + ins.writeC3D() + "\n"
            outText = outText + "\n"
        print(outText)
