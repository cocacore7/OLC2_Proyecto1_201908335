from Environment.Symbol import Symbol
from Abstract.Expression import Expression
from Abstract.Instruction import Instruction
from Environment.Environment import Environment
from Environment.Value import Value
from Enum.typeExpression import typeExpression
from Expression.Primitive.VariableCall import VariableCall


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
        self.llamada.generator = self.generator
        self.exp.generator = self.generator
        callValue: Value = self.llamada.compile(environment)
        newValue: Value = self.exp.compile(environment)
        if callValue.type != typeExpression.NULO:
            # Generar Out Of Bounds De Todos Los Indices
            label3 = self.generator.newLabel()
            for i in self.indices:
                i.generator = self.generator
                tmpValue: Value = i.compile(environment)
                newtmp = i.generator.newTemp()
                label1 = i.generator.newLabel()
                label2 = i.generator.newLabel()
                i.generator.addExpression(newtmp, tmpValue.getValue())
                i.generator.addIf(newtmp, len(callValue.array), ">", label1)
                i.generator.addIf(newtmp, "1", "<", label1)
                i.generator.addGoto(label2)
                i.generator.addLabel(label1)
                i.generator.addCallFunc("bounds_error_proc")
                i.generator.addGoto(label3)
                i.generator.addLabel(label2)

            # Calcular y obtener posicion del valor deseado
            pos = 0
            if callValue.type == typeExpression.STRINGA:
                pos = obtenerPosString(callValue.array, pos)
            else:
                pos = obtenerPosNormal(callValue.array, pos)
            newpos = self.generator.newTemp()
            self.generator.addExpression(newpos, callValue.getValue(), str(pos), "+")

            # Generar Nuevo Arreglo en Heap y Guardar nuevo tmp en stack y variables, la nueva variable y el arreglo referenciado si es que hay

            self.generator.addLabel(label3)
            if not self.isArray:
                tempVar: Symbol = environment.saveVariable(self.id, newValue.type, self.isArray, self.tipoD,
                                                           self.entorno, "")
            else:
                tempVar: Symbol = environment.saveVariable(self.id, newValue.type, self.isArray, self.tipoD,
                                                           self.entorno, self.id)
            if newValue.type != typeExpression.NULO:
                self.generator.addSetStack(str(tempVar.position), newValue.getValue())
        else:
            print("Error En AssignmentArray, No existe La Variable A Llamar")


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
