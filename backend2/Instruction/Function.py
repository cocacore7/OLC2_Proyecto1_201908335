from Abstract.Instruction import Instruction
from Environment.Environment import Environment
from Environment.Value import Value
from Enum.typeExpression import typeExpression
from Generator.Generator import Generator


class Function(Instruction):

    def __init__(self, id: str, parameters, type: typeExpression, block) -> None:
        super().__init__()
        self.id = id
        self.parameters = parameters
        self.block = block
        self.type = type

    def compile(self, environment: Environment) -> Value:
        # Generador Nuevo Para La Funcion, Copiando Valores Del Global
        generator: Generator = Generator()
        generator.addFunction(self.id)
        generator.temporal = self.generator.temporal
        generator.label = self.generator.label
        generator.tempList = self.generator.tempList
        newEnv = Environment(environment)
        newEnv.size = newEnv.size + 1
        newEnv.localSize = newEnv.localSize + 1

        # Pasar Parametros
        cont = environment.size + 1
        for param in self.parameters:
            newtmp = generator.newTemp()
            generator.addActStack(newtmp, str(cont))
            cont = cont + 1
            newEnv.saveParameter(param.id, param.type, param.array, "")

        # Instrucciones De Funcion En  Nuevo Generador
        for ins in self.block:
            ins.generator = generator
            value = ins.compile(newEnv)
            if value is not None:
                environment.saveFunction(self.id, value.value, value.type)
        generator.addCloseFunction()

        # Regresando Valores Nuevos De Generador Funcion a Global + Codigo De Funcion
        self.generator.temporal = generator.temporal
        self.generator.label = generator.label
        self.generator.tempList = generator.tempList
        self.generator.functions.append(generator.code)

