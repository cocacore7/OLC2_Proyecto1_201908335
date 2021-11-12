from Enum.typeExpresionC3D import typeExpression
from Enum.typeInstructionC3D import typeInstruction
from OptimizacionC3D.ArithmeticC3D import ArithmeticC3D


class Mirilla:

    def __init__(self) -> None:
        self.instructionsRule1 = []
        self.instructionsRule2 = []
        self.instructionsRule6 = []
        self.saltoRule2 = None

    def rule1(self, C3D):
        for ins in C3D:
            if ins.getType() == typeInstruction.ASSIGNMENT and ins.value.getType() == typeExpression.PRIMITIVE:
                if len(self.instructionsRule1) > 0:
                    for assig in self.instructionsRule1:
                        if ins.target == assig.value.value:
                            if ins.value.value == assig.target:
                                ins.write = False
                                self.instructionsRule1.remove(assig)
                            else:
                                self.instructionsRule1.remove(assig)
                    self.instructionsRule1.append(ins)
                else:
                    self.instructionsRule1.append(ins)
            elif ins.getType() == typeInstruction.LABEL:
                self.instructionsRule1.clear()
        return C3D

    def rule2(self, C3D):
        for ins in C3D:
            if ins.getType() == typeInstruction.GOTO and self.saltoRule2 is None:
                self.instructionsRule2.clear()
                self.saltoRule2 = ins
                continue
            elif ins.getType() == typeInstruction.LABEL and self.saltoRule2 is not None:
                if ins.value == self.saltoRule2.value:
                    for ins2 in self.instructionsRule2:
                        ins2.write = False
                    self.instructionsRule2.clear()
                    self.saltoRule2 = None
                else:
                    self.instructionsRule2.clear()
                    self.saltoRule2 = None
            if self.saltoRule2 is not None:
                self.instructionsRule2.append(ins)
        return C3D

    def rule6(self, C3D):
        for ins in C3D:
            if ins.getType() == typeInstruction.ASSIGNMENT:
                if type(ins.value) == ArithmeticC3D:
                    if ins.target == ins.value.left.value:
                        if ins.value.getType() == typeExpression.PLUS:
                            if ins.value.rigth.value == "0":
                                ins.write = False
                        elif ins.value.getType() == typeExpression.MINUS:
                            if ins.value.rigth.value == "0":
                                ins.write = False
                        elif ins.value.getType() == typeExpression.MULTIPLY:
                            if ins.value.rigth.value == "1":
                                ins.write = False
                        elif ins.value.getType() == typeExpression.DIV:
                            if ins.value.rigth.value == "1":
                                ins.write = False
                self.instructionsRule6.append(ins)
        return C3D

    def rule7(self, C3D):
        for ins in C3D:
            if ins.getType() == typeInstruction.ASSIGNMENT:
                if type(ins.value) == ArithmeticC3D:
                    if ins.target != ins.value.left.value:
                        if ins.value.getType() == typeExpression.PLUS:
                            if ins.value.rigth.value == "0":
                                ins.value.operation = typeExpression.PRIMITIVE
                        elif ins.value.getType() == typeExpression.MINUS:
                            if ins.value.rigth.value == "0":
                                ins.value.operation = typeExpression.PRIMITIVE
                        elif ins.value.getType() == typeExpression.MULTIPLY:
                            if ins.value.rigth.value == "1":
                                ins.value.operation = typeExpression.PRIMITIVE
                        elif ins.value.getType() == typeExpression.DIV:
                            if ins.value.rigth.value == "1":
                                ins.value.operation = typeExpression.PRIMITIVE
                self.instructionsRule6.append(ins)
        return C3D
