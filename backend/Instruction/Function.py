from Abstract.Instruction import Instruction
from Environment.Environment import Environment
from Enum.TransferSentence import TransferSentence
from Globales.Tablas import Errores
from datetime import datetime


class Function(Instruction):

    def __init__(self, id: str, parameters, block) -> None:
        self.id = id
        self.parameters = parameters
        self.block = block

    def execute(self, environment: Environment):
        environment.saveFunction(self.id, self)

    def executeFunction(self, environment: Environment):

        newEnv = Environment(environment)
        for parameter in self.parameters:
            parameter.execute(newEnv)

        newEnv2 = Environment(newEnv)
        for ins in self.block:
            temp = ins.execute(newEnv2)
            if temp is not None:
                if temp.type == TransferSentence.RETURN:
                    temp.funcion = True
                    return temp
                elif temp.type == TransferSentence.BREAK:
                    Errores.append({'Descripcion': "Sentencias Break Incorrecta, No Se Permite En Funciones", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                    return
                elif temp.type == TransferSentence.CONTINUE:
                    Errores.append({'Descripcion': "Sentencias Continue Incorrecta, No Se Permite En Funciones", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                    return
