from Enum.typeExpression import typeExpression
from Enum.arithmeticOperation import arithmeticOperation
from Environment.Environment import Environment
from Environment.Symbol import Symbol
from Abstract.Expression import Expression
from Instruction.Parameter import Parameter
from Globales.Tablas import Errores
from datetime import datetime


class Arithmetic(Expression):

    def __init__(self, leftExp: Expression, rightExp: Expression, operation: arithmeticOperation):
        self.leftExp = leftExp
        self.rightExp = rightExp
        self.operation = operation

    def execute(self, environment: Environment) -> Symbol:
        leftValue = self.leftExp.execute(environment)
        if type(leftValue) is Parameter:
            if type(leftValue.value) is Symbol:
                leftValue = leftValue.value
        rightValue = self.rightExp.execute(environment)
        if type(rightValue) is Parameter:
            if type(rightValue.value) is Symbol:
                rightValue.value = rightValue.value.getValue()

        if self.operation == arithmeticOperation.PLUS:
            if leftValue.getType() == typeExpression.INTEGER:
                if rightValue.getType() == typeExpression.INTEGER:
                    return Symbol(
                        "",
                        int(leftValue.getValue()) + int(rightValue.getValue()),
                        typeExpression.INTEGER
                    )
                elif rightValue.getType() == typeExpression.FLOAT:
                    return Symbol(
                        "",
                        int(leftValue.getValue()) + float(rightValue.getValue()),
                        typeExpression.FLOAT
                    )
                else:
                    Errores.append({'Descripcion': "No es posible sumar " + str(leftValue.getValue()) + " y " + str(rightValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            elif leftValue.getType() == typeExpression.FLOAT:
                if rightValue.getType() == typeExpression.INTEGER:
                    return Symbol(
                        "",
                        float(leftValue.getValue()) + int(rightValue.getValue()),
                        typeExpression.FLOAT
                    )
                elif rightValue.getType() == typeExpression.FLOAT:
                    return Symbol(
                        "",
                        float(leftValue.getValue()) + float(rightValue.getValue()),
                        typeExpression.FLOAT
                    )
                else:
                    Errores.append({'Descripcion': "No es posible sumar " + str(leftValue.getValue()) + " y " + str(rightValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            else:
                Errores.append({'Descripcion': "No es posible sumar " + str(leftValue.getValue()) + " y " + str(rightValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})

        elif self.operation == arithmeticOperation.MINUS:
            if leftValue.getType() == typeExpression.INTEGER:
                if rightValue.getType() == typeExpression.INTEGER:
                    return Symbol(
                        "",
                        int(leftValue.getValue()) - int(rightValue.getValue()),
                        typeExpression.INTEGER
                    )
                elif rightValue.getType() == typeExpression.FLOAT:
                    return Symbol(
                        "",
                        int(leftValue.getValue()) - float(rightValue.getValue()),
                        typeExpression.FLOAT
                    )
                else:
                    Errores.append({'Descripcion': "No es posible restar " + str(leftValue.getValue()) + " y " + str(rightValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            elif leftValue.getType() == typeExpression.FLOAT:
                if rightValue.getType() == typeExpression.INTEGER:
                    return Symbol(
                        "",
                        float(leftValue.getValue()) - int(rightValue.getValue()),
                        typeExpression.FLOAT
                    )
                elif rightValue.getType() == typeExpression.FLOAT:
                    return Symbol(
                        "",
                        float(leftValue.getValue()) - float(rightValue.getValue()),
                        typeExpression.FLOAT
                    )
                else:
                    Errores.append({'Descripcion': "No es posible restar " + str(leftValue.getValue()) + " y " + str(rightValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            else:
                    Errores.append({'Descripcion': "No es posible restar " + str(leftValue.getValue()) + " y " + str(rightValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})

        elif self.operation == arithmeticOperation.MULTIPLY:
            if leftValue.getType() == typeExpression.INTEGER:
                if rightValue.getType() == typeExpression.INTEGER:
                    return Symbol(
                        "",
                        int(leftValue.getValue()) * int(rightValue.getValue()),
                        typeExpression.INTEGER
                    )
                elif rightValue.getType() == typeExpression.FLOAT:
                    return Symbol(
                        "",
                        int(leftValue.getValue()) * float(rightValue.getValue()),
                        typeExpression.FLOAT
                    )
                else:
                    Errores.append({'Descripcion': "No es posible multiplicar " + str(leftValue.getValue()) + " y " + str(rightValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            elif leftValue.getType() == typeExpression.FLOAT:
                if rightValue.getType() == typeExpression.INTEGER:
                    return Symbol(
                        "",
                        float(leftValue.getValue()) * int(rightValue.getValue()),
                        typeExpression.FLOAT
                    )
                elif rightValue.getType() == typeExpression.FLOAT:
                    return Symbol(
                        "",
                        float(leftValue.getValue()) * float(rightValue.getValue()),
                        typeExpression.FLOAT
                    )
                else:
                    Errores.append({'Descripcion': "No es posible multiplicar " + str(leftValue.getValue()) + " y " + str(rightValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            elif leftValue.getType() == typeExpression.STRING:
                if rightValue.getType() == typeExpression.STRING:
                    return Symbol(
                        "",
                        leftValue.getValue() + rightValue.getValue(),
                        typeExpression.STRING
                    )
                else:
                    
                    Errores.append({'Descripcion': "No es posible Concatenar " + str(leftValue.getValue()) + " y " + str(rightValue.getValue())+", Se esperaban Strings", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            else:
                Errores.append({'Descripcion': "No es posible multiplicar " + str(leftValue.getValue()) + " y " + str(rightValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})

        elif self.operation == arithmeticOperation.DIV:
            if leftValue.getType() == typeExpression.INTEGER:
                if rightValue.getType() == typeExpression.INTEGER:
                    if int(rightValue.getValue()) != 0:
                        return Symbol(
                            "",
                            int(leftValue.getValue()) / int(rightValue.getValue()),
                            typeExpression.FLOAT
                        )
                    else:
                        Errores.append({'Descripcion': "No es posible dividir " + str(leftValue.getValue()) + " Entre 0", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                elif rightValue.getType() == typeExpression.FLOAT:
                    if float(rightValue.getValue()) != 0:
                        return Symbol(
                            "",
                            int(leftValue.getValue()) / float(rightValue.getValue()),
                            typeExpression.FLOAT
                        )
                    else:
                        Errores.append({'Descripcion': "No es posible dividir " + str(leftValue.getValue()) + " Entre 0", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                else:
                    Errores.append({'Descripcion': "No es posible dividir " + str(leftValue.getValue()) + " y " + str(rightValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            elif leftValue.getType() == typeExpression.FLOAT:
                if rightValue.getType() == typeExpression.INTEGER:
                    if int(rightValue.getValue()) != 0:
                        return Symbol(
                            "",
                            float(leftValue.getValue()) / int(rightValue.getValue()),
                            typeExpression.FLOAT
                        )
                    else:
                        Errores.append({'Descripcion': "No es posible dividir " + str(leftValue.getValue()) + " Entre 0", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                elif rightValue.getType() == typeExpression.FLOAT:
                    if float(rightValue.getValue()) != 0:
                        return Symbol(
                            "",
                            float(leftValue.getValue()) / float(rightValue.getValue()),
                            typeExpression.FLOAT
                        )
                    else:
                        Errores.append({'Descripcion': "No es posible dividir " + str(leftValue.getValue()) + " Entre 0", 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
                        print()
                else:
                    Errores.append({'Descripcion': "No es posible multiplicar " + str(leftValue.getValue()) + " y " + str(rightValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            else:
                    Errores.append({'Descripcion': "No es posible multiplicar " + str(leftValue.getValue()) + " y " + str(rightValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})

        elif self.operation == arithmeticOperation.POT:
            if leftValue.getType() == typeExpression.INTEGER:
                if rightValue.getType() == typeExpression.INTEGER:
                    return Symbol(
                        "",
                        int(leftValue.getValue()) ** int(rightValue.getValue()),
                        typeExpression.INTEGER
                    )
                elif rightValue.getType() == typeExpression.FLOAT:
                    return Symbol(
                        "",
                        int(leftValue.getValue()) ** float(rightValue.getValue()),
                        typeExpression.FLOAT
                    )
                else:
                    Errores.append({'Descripcion': "No es posible elevar " + str(leftValue.getValue()) + " y " + str(rightValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            elif leftValue.getType() == typeExpression.FLOAT:
                if rightValue.getType() == typeExpression.INTEGER:
                    return Symbol(
                        "",
                        float(leftValue.getValue()) ** int(rightValue.getValue()),
                        typeExpression.FLOAT
                    )
                elif rightValue.getType() == typeExpression.FLOAT:
                    return Symbol(
                        "",
                        float(leftValue.getValue()) ** float(rightValue.getValue()),
                        typeExpression.FLOAT
                    )
                else:
                    Errores.append({'Descripcion': "No es posible elevar " + str(leftValue.getValue()) + " y " + str(rightValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            elif leftValue.getType() == typeExpression.STRING:
                if rightValue.getType() == typeExpression.INTEGER:
                    tmp = ""
                    for i in range(int(rightValue.getValue())):
                        tmp = tmp + leftValue.getValue()
                    return Symbol(
                        "",
                        tmp,
                        typeExpression.STRING
                    )
                else:
                    Errores.append({'Descripcion': "No es posible elevar " + str(leftValue.getValue()) + " y " + str(rightValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            else:
                Errores.append({'Descripcion': "No es posible elevar " + str(leftValue.getValue()) + " y " + str(rightValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})

        elif self.operation == arithmeticOperation.MOD:
            if leftValue.getType() == typeExpression.INTEGER:
                if rightValue.getType() == typeExpression.INTEGER:
                    return Symbol(
                        "",
                        int(leftValue.getValue()) % int(rightValue.getValue()),
                        typeExpression.INTEGER
                    )
                elif rightValue.getType() == typeExpression.FLOAT:
                    return Symbol(
                        "",
                        int(leftValue.getValue()) % float(rightValue.getValue()),
                        typeExpression.FLOAT
                    )
                else:
                    Errores.append({'Descripcion': "No es posible Obtener El Modulo De " + str(leftValue.getValue()) + " y " + str(rightValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            elif leftValue.getType() == typeExpression.FLOAT:
                if rightValue.getType() == typeExpression.INTEGER:
                    return Symbol(
                        "",
                        float(leftValue.getValue()) % int(rightValue.getValue()),
                        typeExpression.FLOAT
                    )
                elif rightValue.getType() == typeExpression.FLOAT:
                    return Symbol(
                        "",
                        float(leftValue.getValue()) % float(rightValue.getValue()),
                        typeExpression.FLOAT
                    )
                else:
                    Errores.append({'Descripcion': "No es posible Obtener El Modulo De " + str(leftValue.getValue()) + " y " + str(rightValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
            else:
                Errores.append({'Descripcion': "No es posible Obtener El Modulo De " + str(leftValue.getValue()) + " y " + str(rightValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})

        elif self.operation == arithmeticOperation.NEG:
            if leftValue.getType() == typeExpression.INTEGER:
                return Symbol(
                    "",
                    int(leftValue.getValue()) * -1,
                    typeExpression.INTEGER
                )
            elif leftValue.getType() == typeExpression.FLOAT:
                return Symbol(
                    "",
                    float(leftValue.getValue()) * - 1,
                    typeExpression.FLOAT
                )
            else:
                Errores.append({'Descripcion': "No es posible negativo De: " + str(leftValue.getValue()), 'Linea': "", 'Columna': "", 'Fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})

        return Symbol("", 'nothing', typeExpression.NULO)
