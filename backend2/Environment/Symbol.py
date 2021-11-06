class Symbol:
    # Nuestros simbolos poseen un id, un valor y un tipo
    def __init__(self, id: str, type, position):
        self.id = id
        self.type = type
        self.position = position
        self.array = False
        self.ref = ""

    def getId(self):
        return self.id

    def getType(self):
        return self.type

    def isArray(self):
        return self.array
