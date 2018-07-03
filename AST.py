class Metodo:
    def __init__(self, parameters, size):
        self.parameters = parameters
        self.size = size

class Print:
    def __init__(self, parameter):
        self.parameter = parameter

class InstructionList:
    def __init__(self):
        self.instructions = []

    def addInstructions(self, instruction):
        self.instructions.insert(0, instruction)