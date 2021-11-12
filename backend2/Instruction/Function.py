from Abstract.Instruction import Instruction
from Environment.Environment import Environment
from Environment.Value import Value
from Enum.typeExpression import typeExpression
from Generator.Generator import Generator
from Instruction.If import If
from Instruction.For import For
from Instruction.While import While
from Instruction.Return import Return


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
        posReturn = newEnv.size
        newEnv.size = newEnv.size + 1
        newEnv.localSize = newEnv.localSize + 1
        tmpReturn = generator.newTemp()
        environment.saveFunction(self.id, tmpReturn, self.type)
        LabelSalir = generator.newLabel()

        # Pasar Parametros
        for param in self.parameters:
            newEnv.saveParameter(param.id, param.type, param.array, "")

        # Instrucciones De Funcion En  Nuevo Generador
        for ins in self.block:
            ins.generator = generator
            if type(ins) == If:
                ins.funtioncReturn = tmpReturn
                ins.LabelSalir = LabelSalir
            elif type(ins) == For:
                ins.funtioncReturn = tmpReturn
                ins.LabelSalir = LabelSalir
            elif type(ins) == While:
                ins.funtioncReturn = tmpReturn
                ins.LabelSalir = LabelSalir
            elif type(ins) == Return:
                ins.funtioncReturn = tmpReturn
                ins.espacioReturn = posReturn
                ins.tmpSalir = LabelSalir
            ins.compile(newEnv)
        generator.addLabel(LabelSalir)
        generator.addCloseFunction()

        # Regresando Valores Nuevos De Generador Funcion a Global + Codigo De Funcion
        self.generator.temporal = generator.temporal
        self.generator.label = generator.label
        self.generator.tempList = generator.tempList
        self.generator.functions.append(generator.code)

        return Value(tmpReturn, True, self.type)

