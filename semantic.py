from parse import parserAnalysis, getAST
from AST import *

list = []
def semanticAnalysis():
    correct = parserAnalysis()
    if correct:
        ast = getAST()
        correcto = analyze(ast.instructions)
        return correcto

def analyze(instructions):
    correcto = True
    for instruction in instructions:
        if type(instruction) is Print:
            if lookup(instruction.parameter):
                pass
            else:
                print(instruction.parameter, " no está asignada o declarada")
                correcto = False

        if type(instruction) is Metodo:
            if len(instruction.parameters) == instruction.size and instruction.size <= 5 and instruction.size >= 1:
                list.extend(instruction.parameters)
            else:
                #revisar mayor a 6
                correcto = False
                if not len(instruction.parameters) == instruction.size:
                    print("Tamano de asignaciones es diferente al numero de variables")
                if instruction.size > 5 or instruction.size < 1:
                    print("Tamano de asignaciones no esta entre 1 y 5")
    return correcto

def lookup(parameter):
    encontrado = False
    for value in list:
        if value == parameter:
            encontrado = True
    return encontrado

def getList():
    return list
