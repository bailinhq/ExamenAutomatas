from parse import parserAnalysis, getAST
from AST import *

list = []
def semanticAnalysis():
    parserAnalysis()
    ast = getAST()
    analyze(ast.instructions)

def analyze(instructions):
    for instruction in instructions:
        if type(instruction) is Print:
            if lookup(instruction.parameter):
                pass
            else:
                print(instruction.parameter, " no está asignada o declarada")

        if type(instruction) is Metodo:
            if len(instruction.parameters) == instruction.size and instruction.size <= 5 or instruction.size >= 1:
                list.extend(instruction.parameters)
            else:
                if not len(instruction.parameters) == instruction.size:
                    print("Tamano de asignaciones es diferente al numero de variables")
                if instruction.size > 5 or instruction.size < 1:
                    print("Tamano de asignaciones es no esta entre 1 y 5")

def lookup(parameter):
    encontrado = False
    for value in list:
        if value == parameter:
            encontrado = True
    return encontrado

def getList():
    return list

semanticAnalysis()