from Globales.Tablas import Modulo


class Generator:

    def __init__(self) -> None:
        self.generator = None
        self.temporal = 3
        self.label = 0
        self.code = []
        self.tempList = []
        self.nativas = []

    # Obtener los temporales usados
    def getUsedTemps(self) -> str:
        return ",".join(self.tempList)

    # Obtener el codigo generado
    def getCode(self) -> str:
        tempCode: str = 'package main;\n'
        tempCode = tempCode + 'import ( "fmt" ); \n'
        if len(Modulo) > 0:
            tempCode = tempCode + 'import ( "math" ); \n'
        tempCode = tempCode + "var stack [10000]float64;\n"
        tempCode = tempCode + "var heap [10000]float64;\n"
        tempCode = tempCode + "var P, H float64;\n"
        tempCode = tempCode + "var t0,t1,t2,"

        if len(self.tempList) > 0:
            tempCode = tempCode + self.getUsedTemps()
        else:
            tempCode = tempCode + "t3"

        tempCode = tempCode + " float64;\n"

        tempCode = tempCode + '\nfunc math_error_proc(){\n'
        tempCode = tempCode + 'fmt.Printf("%c", 77);\n'
        tempCode = tempCode + 'fmt.Printf("%c", 97);\n'
        tempCode = tempCode + 'fmt.Printf("%c", 116);\n'
        tempCode = tempCode + 'fmt.Printf("%c", 104);\n'
        tempCode = tempCode + 'fmt.Printf("%c", 69); \n'
        tempCode = tempCode + 'fmt.Printf("%c", 114);\n'
        tempCode = tempCode + 'fmt.Printf("%c", 114);\n'
        tempCode = tempCode + 'fmt.Printf("%c", 111);\n'
        tempCode = tempCode + 'fmt.Printf("%c", 114);\n'
        tempCode = tempCode + 'fmt.Printf("%c", 10);\n'
        tempCode = tempCode + '}\n'

        tempCode = tempCode + '\nfunc print_true_proc(){\n'
        tempCode = tempCode + 'fmt.Printf("%c", int(116));\n'
        tempCode = tempCode + 'fmt.Printf("%c", int(114));\n'
        tempCode = tempCode + 'fmt.Printf("%c", int(117));\n'
        tempCode = tempCode + 'fmt.Printf("%c", int(101));\n'
        tempCode = tempCode + '}\n'

        tempCode = tempCode + '\nfunc print_false_proc(){\n'
        tempCode = tempCode + 'fmt.Printf("%c", int(102));\n'
        tempCode = tempCode + 'fmt.Printf("%c", int(97));\n'
        tempCode = tempCode + 'fmt.Printf("%c", int(108));\n'
        tempCode = tempCode + 'fmt.Printf("%c", int(115));\n'
        tempCode = tempCode + 'fmt.Printf("%c", int(101));\n'
        tempCode = tempCode + '}\n'

        tempCode = tempCode + '\nfunc print_nothing_proc(){\n'
        tempCode = tempCode + 'fmt.Printf("%c", int(78));\n'
        tempCode = tempCode + 'fmt.Printf("%c", int(111));\n'
        tempCode = tempCode + 'fmt.Printf("%c", int(116));\n'
        tempCode = tempCode + 'fmt.Printf("%c", int(104));\n'
        tempCode = tempCode + 'fmt.Printf("%c", int(105));\n'
        tempCode = tempCode + 'fmt.Printf("%c", int(110));\n'
        tempCode = tempCode + 'fmt.Printf("%c", int(103));\n'
        tempCode = tempCode + '}\n'

        tempCode = tempCode + '\nfunc print_String_proc(){\n'
        tempCode = tempCode + 't0=P+1;\n'
        tempCode = tempCode + 't1=stack[int(t0)];\n'
        tempCode = tempCode + 'L1:\n'
        tempCode = tempCode + 't2=heap[int(t1)];\n'
        tempCode = tempCode + 'if t2 == -1 {goto L0;}\n'
        tempCode = tempCode + 'fmt.Printf("%c", int(t2));\n'
        tempCode = tempCode + 't1=t1+1;\n'
        tempCode = tempCode + 'goto L1;\n'
        tempCode = tempCode + 'L0:\n'
        tempCode = tempCode + 'return;\n'
        tempCode = tempCode + '}\n'

        tempCode = tempCode + '\nfunc main(){\n'
        tempCode = tempCode + "\n".join(self.code)
        tempCode = tempCode + '\n}\n'

        return tempCode

    # Generar un nuevo temporal
    def newTemp(self) -> str:
        temp = "t" + str(self.temporal)
        self.temporal = self.temporal + 1

        # Lo guardamos para declararlo
        self.tempList.append(temp)
        return temp

    # Generador de label
    def newLabel(self) -> str:
        temp = self.label
        self.label = self.label + 1
        return "L" + str(temp)

    # Añade un printf
    def addPrintf(self, typePrint: str, value: str):
        self.code.append("fmt.Printf(\"%" + typePrint + "\"," + value + ");")

    # Obtener Posicion Actual Heap
    def addActHeap(self, temp: str):
        self.code.append(temp + "= H;")

    # Obtener Posicion Actual Stack
    def addActStack(self, temp: str, index: str):
        self.code.append(temp + "= P+" + index + ";")

    # Obtener Siguiente Temporal String
    def addNextTmp(self, temp: str):
        self.code.append(temp + " = " + temp + "+1;")

    def addCallFunc(self, name: str):
        self.code.append(name + "();")

    # Añade label al codigo
    def addLabel(self, label: str):
        self.code.append(label + ":")

    def addExpression(self, target: str, left: str, right: str, operator: str):
        self.code.append(target + " = " + left + " " + operator + " " + right + ";")

    def addExpressionMod(self, target: str, left: str, right: str):
        self.code.append(target + " = math.Mod(" + left + ", " + right + ");")

    def addIf(self, left: str, rigth: str, operator: str, label: str):
        self.code.append("if " + left + " " + operator + " " + rigth + " {goto " + label + ";}")

    def addGoto(self, label: str):
        self.code.append("goto " + label + ";")

    # Salto de linea
    def addNewLine(self):
        self.code.append('fmt.Printf(\"%c\",10);')

    # Se mueve hacia la posicion siguiente del heap
    def addNextHeap(self):
        self.code.append("H = H + 1;")

    # Se mueve hacia la posicion siguiente del stack
    def addNextStack(self, index: str):
        self.code.append("P = P + " + index + ";")

    # Se mueve hacia la posicion anterior del stack
    def addBackStack(self, index: str):
        self.code.append("P = P - " + index + ";")

    # Obtiene el valor del heap en cierta posicion
    def addGetHeap(self, target: str, index: str):
        self.code.append(target + " = heap[int(" + index + ") ];")

    # Inserta valor en el heap
    def addSetHeap(self, index: str, value: str):
        self.code.append("heap[int(" + index + ")] = " + value + ";")

    # Obtiene valor del stack en cierta posicion
    def addGetStack(self, target: str, index: str):
        self.code.append(target + " = stack[int(" + index + ")];")

    # INserta valor al stack
    def addSetStack(self, index: str, value: str):
        self.code.append("stack[int(" + index + ")] = " + value + ";")
