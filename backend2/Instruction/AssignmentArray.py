from Abstract.Expression import Expression
from Abstract.Instruction import Instruction
from Environment.Environment import Environment
from Environment.Value import Value
from Enum.typeExpression import typeExpression
from Expression.Primitive.VariableCall import VariableCall
from Globales.Tablas import Errores
from datetime import datetime


class AssignmentArray(Instruction):

    def __init__(self, id: str, llamada: VariableCall, indices, exp: Expression, type: typeExpression, isArray: bool, tipoD: str, entorno: str) -> None:
        super().__init__()
        self.id = id
        self.llamada = llamada
        self.indices = indices
        self.exp = exp
        self.type = type
        self.isArray = isArray
        self.tipoD = tipoD
        self.entorno = entorno

    def compile(self, environment: Environment) -> Value:
        # Calcular Expresion Y Llamada A Variable
        self.llamada.generator = self.generator
        callValue: Value = self.llamada.compile(environment)
        self.exp.generator = self.generator
        exp: Value = self.exp.compile(environment)
        if callValue.type != typeExpression.NULO:
            # Calcular Indices
            indices = []
            for i in self.indices:
                indiceTmp = self.generator.newTemp()
                i.generator = self.generator
                tmpValue: Value = i.compile(environment)
                self.generator.addExpression(indiceTmp, tmpValue.getValue(), "", "")
                indices.append(indiceTmp)

            # Calcular Dos Inicios
            tmpini1 = self.generator.newTemp()
            tmpini2 = self.generator.newTemp()
            self.generator.addExpression(tmpini1, callValue.getValue(), "", "")
            self.generator.addExpression(tmpini2, callValue.getValue(), "", "")

            # Procesar Indices en Out of Bounds
            tmpini3 = self.generator.newTemp()
            tmpini4 = self.generator.newTemp()
            for i in indices:
                Label1 = self.generator.newLabel()
                Label2 = self.generator.newLabel()
                Label3 = self.generator.newLabel()
                Label4 = self.generator.newLabel()
                Label5 = self.generator.newLabel()
                # Comprobar Out Of Bounds
                self.generator.addExpression(tmpini1, tmpini1, "1", "+")
                self.generator.addGetHeap(tmpini3, tmpini1)
                self.generator.addIf(i, tmpini3, ">", Label1)
                self.generator.addIf(i, "1", "<", Label1)
                self.generator.addGoto(Label2)
                self.generator.addLabel(Label1)
                self.generator.addCallFunc("bounds_error_proc")
                self.generator.addGoto(Label5)
                # Codigo Para Cambiar Referencia Nueva De Expresion
                self.generator.addLabel(Label2)
                self.generator.addExpression(tmpini2, tmpini2, "2", "+")
                self.generator.addExpression(tmpini2, tmpini2, i, "+")
                self.generator.addGetHeap(tmpini4, tmpini2)
                self.generator.addIf(tmpini4, "-0.000001", "==", Label3)
                self.generator.addGoto(Label4)
                self.generator.addLabel(Label3)
                self.generator.addExpression(tmpini1, tmpini1, tmpini3, "+")
                self.generator.addExpression(tmpini1, tmpini1, "2", "+")
                self.generator.addExpression(tmpini2, tmpini1, "", "")
                self.generator.addGoto(Label5)
                self.generator.addLabel(Label4)
                self.generator.addSetHeap(tmpini2, exp.getValue())
                self.generator.addLabel(Label5)

        else:
            Errores.append({'Descripcion': "Error En AssignmentArray, No existe La Variable A Llamar", 'Linea': "0", 'Columna': "0", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})


def obtenerPosNormal(arr, num):
    num = num + 2
    for i in arr:
        if i.type == typeExpression.INTEGERA:
            num = num + obtenerPosNormal(arr, num)
        else:
            num = num + 1
    return num


def obtenerPosString(arr, num):
    num = num + 2
    for i in arr:
        if i.type == typeExpression.STRINGA:
            num = num + obtenerPosNormal(arr, num)
        else:
            num = num + len(i)
    return num
