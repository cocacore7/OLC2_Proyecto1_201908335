from Enum.typeExpresionC3D import typeExpression
from Enum.typeInstructionC3D import typeInstruction
from OptimizacionC3D.ArithmeticC3D import ArithmeticC3D
from Globales.Tablas import Optimizacion


class Mirilla:

    def __init__(self) -> None:
        self.instructionsRule1 = []
        self.instructionsRule2 = []
        self.instructionsRule3 = []
        self.instructionsRule6 = []
        self.saltoRule2 = None
        self.salto1Rule3 = None
        self.salto2Rule3 = None
        self.Label1Rule3 = None

    def rule1(self, C3D):
        for ins in C3D:
            if ins.getType() == typeInstruction.ASSIGNMENT and ins.value.getType() == typeExpression.PRIMITIVE:
                if len(self.instructionsRule1) > 0:
                    for assig in self.instructionsRule1:
                        if ins.target == assig.value.value:
                            if ins.value.value == assig.target:
                                Optimizacion.append({
                                    'Tipo': "Mirilla",
                                    'Regla': "1",
                                    'ExpOr': assig.writeC3D() + " - " + ins.writeC3D(),
                                    'ExpOp': assig.writeC3D(),
                                    'Fila': assig.line
                                })
                                ins.write = False
                                self.instructionsRule1.remove(assig)
                            else:
                                self.instructionsRule1.remove(assig)
                    self.instructionsRule1.append(ins)
                else:
                    self.instructionsRule1.append(ins)
            else:
                if ins.getType() == typeInstruction.LABEL:
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
                    org = ""
                    for ins2 in self.instructionsRule2:
                        org = org + ins2.writeC3D() + "\n"
                    Optimizacion.append({
                        'Tipo': "Mirilla",
                        'Regla': "2",
                        'ExpOr': self.saltoRule2.writeC3D() + " - " + org + ins.writeC3D(),
                        'ExpOp': self.saltoRule2.writeC3D() + " - " + ins.writeC3D(),
                        'Fila': self.saltoRule2.line
                    })
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

    def rule3(self, C3D):
        for ins in C3D:
            if ins.getType() == typeInstruction.IF and self.salto1Rule3 is None:
                self.salto1Rule3 = ins
            elif ins.getType() == typeInstruction.GOTO and self.salto1Rule3 is not None:
                self.salto2Rule3 = ins
            elif ins.getType() == typeInstruction.LABEL and self.salto1Rule3 is not None and self.salto2Rule3 is not None:
                if self.salto1Rule3 is not None and self.salto2Rule3 is None:
                    self.salto1Rule3 = None
                    self.salto2Rule3 = None
                    self.Label1Rule3 = None

                elif self.salto1Rule3 is not None and self.salto2Rule3 is not None:
                    if self.salto1Rule3.goto.value == ins.value and self.Label1Rule3 is None:
                        self.Label1Rule3 = ins
                    elif self.salto2Rule3.value == ins.value and self.Label1Rule3 is not None:
                        exporg = self.salto1Rule3.writeC3D() + " - " + self.salto2Rule3.writeC3D() + " - " + self.Label1Rule3.writeC3D() + " - " + ins.writeC3D()
                        # Aqui va el valor para Reporte
                        self.salto1Rule3.goto.value = ins.value
                        self.salto2Rule3.write = False
                        if self.salto1Rule3.exp.operation == typeExpression.IGUAL:
                            self.salto1Rule3.exp.operation = typeExpression.DISTINTO
                        elif self.salto1Rule3.exp.operation == typeExpression.DISTINTO:
                            self.salto1Rule3.exp.operation = typeExpression.IGUAL
                        elif self.salto1Rule3.exp.operation == typeExpression.MENOR:
                            self.salto1Rule3.exp.operation = typeExpression.MAYOR
                        elif self.salto1Rule3.exp.operation == typeExpression.MAYOR:
                            self.salto1Rule3.exp.operation = typeExpression.MENOR
                        elif self.salto1Rule3.exp.operation == typeExpression.MENORIGUAL:
                            self.salto1Rule3.exp.operation = typeExpression.MAYORIGUAL
                        elif self.salto1Rule3.exp.operation == typeExpression.MAYORIGUAL:
                            self.salto1Rule3.exp.operation = typeExpression.MENORIGUAL
                        self.Label1Rule3.write = False
                        expopt = self.salto1Rule3.writeC3D() + " - " + ins.writeC3D()
                        Optimizacion.append({
                            'Tipo': "Mirilla",
                            'Regla': "3",
                            'ExpOr': exporg,
                            'ExpOp': expopt,
                            'Fila': self.salto1Rule3.line
                        })
                    else:
                        self.salto1Rule3 = None
                        self.salto2Rule3 = None
                        self.Label1Rule3 = None
        return C3D

    def rule6(self, C3D):
        for ins in C3D:
            if ins.getType() == typeInstruction.ASSIGNMENT:
                if type(ins.value) == ArithmeticC3D:
                    if ins.target == ins.value.left.value:
                        if ins.value.getType() == typeExpression.PLUS:
                            if ins.value.rigth.value == "0":
                                Optimizacion.append({
                                    'Tipo': "Mirilla",
                                    'Regla': "6",
                                    'ExpOr': ins.writeC3D(),
                                    'ExpOp': "Eliminada",
                                    'Fila': ins.line
                                })
                                ins.write = False
                        elif ins.value.getType() == typeExpression.MINUS:
                            if ins.value.rigth.value == "0":
                                Optimizacion.append({
                                    'Tipo': "Mirilla",
                                    'Regla': "6",
                                    'ExpOr': ins.writeC3D(),
                                    'ExpOp': "Eliminada",
                                    'Fila': ins.line
                                })
                                ins.write = False
                        elif ins.value.getType() == typeExpression.MULTIPLY:
                            if ins.value.rigth.value == "1":
                                Optimizacion.append({
                                    'Tipo': "Mirilla",
                                    'Regla': "6",
                                    'ExpOr': ins.writeC3D(),
                                    'ExpOp': "Eliminada",
                                    'Fila': ins.line
                                })
                                ins.write = False
                        elif ins.value.getType() == typeExpression.DIV:
                            if ins.value.rigth.value == "1":
                                Optimizacion.append({
                                    'Tipo': "Mirilla",
                                    'Regla': "6",
                                    'ExpOr': ins.writeC3D(),
                                    'ExpOp': "Eliminada",
                                    'Fila': ins.line
                                })
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
                                exporg = ins.writeC3D()
                                ins.value.operation = typeExpression.PRIMITIVE
                                expopt = ins.writeC3D()
                                Optimizacion.append({
                                    'Tipo': "Mirilla",
                                    'Regla': "7",
                                    'ExpOr': exporg,
                                    'ExpOp': expopt,
                                    'Fila': ins.line
                                })
                        elif ins.value.getType() == typeExpression.MINUS:
                            if ins.value.rigth.value == "0":
                                exporg = ins.writeC3D()
                                ins.value.operation = typeExpression.PRIMITIVE
                                expopt = ins.writeC3D()
                                Optimizacion.append({
                                    'Tipo': "Mirilla",
                                    'Regla': "7",
                                    'ExpOr': exporg,
                                    'ExpOp': expopt,
                                    'Fila': ins.line
                                })
                        elif ins.value.getType() == typeExpression.MULTIPLY:
                            if ins.value.rigth.value == "1":
                                exporg = ins.writeC3D()
                                ins.value.operation = typeExpression.PRIMITIVE
                                expopt = ins.writeC3D()
                                Optimizacion.append({
                                    'Tipo': "Mirilla",
                                    'Regla': "7",
                                    'ExpOr': exporg,
                                    'ExpOp': expopt,
                                    'Fila': ins.line
                                })
                        elif ins.value.getType() == typeExpression.DIV:
                            if ins.value.rigth.value == "1":
                                exporg = ins.writeC3D()
                                ins.value.operation = typeExpression.PRIMITIVE
                                expopt = ins.writeC3D()
                                Optimizacion.append({
                                    'Tipo': "Mirilla",
                                    'Regla': "7",
                                    'ExpOr': exporg,
                                    'ExpOp': expopt,
                                    'Fila': ins.line
                                })
                self.instructionsRule6.append(ins)
        return C3D

    def rule8(self, C3D):
        for ins in C3D:
            if ins.getType() == typeInstruction.ASSIGNMENT:
                if type(ins.value) == ArithmeticC3D:
                    if ins.value.getType() == typeExpression.MULTIPLY:
                        if ins.value.rigth.value == "2":
                            exporg = ins.writeC3D()
                            ins.value.operation = typeExpression.PLUS
                            ins.value.rigth.value = ins.value.left.value
                            expopt = ins.writeC3D()
                            Optimizacion.append({
                                'Tipo': "Mirilla",
                                'Regla': "8",
                                'ExpOr': exporg,
                                'ExpOp': expopt,
                                'Fila': ins.line
                            })
                        elif ins.value.rigth.value == "0":
                            exporg = ins.writeC3D()
                            ins.value.operation = typeExpression.PRIMITIVE
                            ins.value.left.value = "0"
                            expopt = ins.writeC3D()
                            Optimizacion.append({
                                'Tipo': "Mirilla",
                                'Regla': "8",
                                'ExpOr': exporg,
                                'ExpOp': expopt,
                                'Fila': ins.line
                            })
                    elif ins.value.getType() == typeExpression.DIV:
                        if ins.value.left.value == "0":
                            exporg = ins.writeC3D()
                            ins.value.operation = typeExpression.PRIMITIVE
                            expopt = ins.writeC3D()
                            Optimizacion.append({
                                'Tipo': "Mirilla",
                                'Regla': "8",
                                'ExpOr': exporg,
                                'ExpOp': expopt,
                                'Fila': ins.line
                            })
                self.instructionsRule6.append(ins)
        return C3D
