from Abstract.Expression import Expression
from Environment.Environment import Environment
from Environment.Value import Value


class FunctionCall(Expression):

    def __init__(self, id: str, parameters) -> None:
        super().__init__()
        self.id = id
        self.parameters = parameters

    def compile(self, environment: Environment) -> Value:
        self.generator.addNextStack(str(environment.size))
        cont = environment.size + 1
        for ins in self.parameters:
            ins.generator = self.generator
            val = ins.compile(environment)
            self.generator.addSetStack(str(cont), val.value)
            cont = cont + 1
        returnValue = environment.getFunction(self.id)
        self.generator.addFunctionCall(self.id, self.parameters)
        self.generator.addBackStack(str(environment.size))
        return returnValue
