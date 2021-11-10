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

            # Calcular y obtener posicion del valor deseado

            # Generar Nuevo Arreglo en Heap y Guardar nuevo tmp en stack y variables, la nueva variable y el arreglo referenciado si es que hay
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


