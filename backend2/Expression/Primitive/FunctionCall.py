from Environment.Symbol import Symbol
from Abstract.Expression import Expression
from Environment.Environment import Environment
from Environment.Value import Value
from Enum.typeExpression import typeExpression


class FunctionCall(Expression):

    def __init__(self, id: str, parameters) -> None:
        super().__init__()
        self.id = id
        self.parameters = parameters

    def compile(self, environment: Environment) -> Value:
        # Faltan Calcular Parametros
        self.generator.addFunctionCall(self.id, self.parameters)
