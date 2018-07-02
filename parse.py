import ply.yacc as yacc
from lex import tokens
from AST import *
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

ast = InstructionList()

def p_START(p):
    'start : metodo NEWLINE start'
    ast.addInstructions(p[1])
    ast.addInstructions(p[3])

def p_START2(p):
    'start : metodo NEWLINE'
    ast.addInstructions(p[1])

def p_START3(p):
    'start : print NEWLINE start'
    ast.addInstructions(p[1])
    ast.addInstructions(p[3])

def p_START4(p):
    'start : print NEWLINE'
    ast.addInstructions(p[1])

######### METODO EXAMEN
def p_METODO(p):
    'metodo : number_assignations ASSIGNATION METODO LEFTPAR INT RIGHTPAR'
    p[0] = Metodo(p[1], p[5])

def p_METODO_error(p):
    'metodo : number_assignations ASSIGNATION METODO LEFTPAR INT error'
    print("Found ", p[6].value, " Expected )")

def p_METODO_error2(p):
    'metodo : number_assignations ASSIGNATION METODO LEFTPAR error'
    print("Found ", p[5].value, " Expected int")

def p_METODO_error3(p):
    'metodo : number_assignations ASSIGNATION METODO error'
    print("Found ", p[4].value, " Expected (")

def p_METODO_error4(p):
    'metodo : number_assignations ASSIGNATION error'
    print("Found ", p[3].value, " Expected metodo")

def p_METODO_error5(p):
    'metodo : number_assignations error'
    print("Found ", p[2].value, " Expected =")

def p_NUMBER_ASSIGNATIONS1(p):
    'number_assignations : NAME'
    p[0] = [p[1]]

def p_NUMBER_ASSIGNATIONS2(p):
    'number_assignations : NAME COMMA NAME'
    p[0] = [p[1], p[3]]

def p_NUMBER_ASSIGNATIONS3(p):
    'number_assignations : NAME COMMA NAME COMMA NAME'
    p[0] = [p[1], p[3], p[5]]

def p_NUMBER_ASSIGNATIONS4(p):
    'number_assignations : NAME COMMA NAME COMMA NAME COMMA NAME COMMA'
    p[0] = [p[1], p[3], p[5], p[7]]

def p_NUMBER_ASSIGNATIONS5(p):
    'number_assignations : NAME COMMA NAME COMMA NAME COMMA NAME COMMA NAME'
    p[0] = [p[1], p[3], p[5], p[7], p[9]]


###### INSTRUCTIONS
def p_PRINT(p):
    'print : PRINT LEFTPAR NAME RIGHTPAR'
    p[0] = Print[3]

def p_PRINT_error(p):
    'print : PRINT LEFTPAR NAME error'
    print("Found ", p[4].value, ". Expected )")

def p_PRINT_error2(p):
    'print : PRINT LEFTPAR error'
    print("Found ", p[3].value, ". Expected variable")

def p_PRINT_error3(p):
    'print : PRINT error'
    print("Found ", p[2].value, ". Expected (")

# def p_error(p):
#     if p:
#         print(bcolors.FAIL+"Error:" +bcolors.ENDC ,bcolors.HEADER + p.type+ bcolors.ENDC, bcolors.BOLD + "", p.value,"" + bcolors.ENDC, bcolors.WARNING + "Sucedió en la línea:" + bcolors.ENDC, bcolors.UNDERLINE + "" ,p.lineno,"" + bcolors.ENDC)
#              # Just discard the token and tell the parser it's okay.
#         parser.errok()

def parserAnalysis():
    name = input("Escriba el nombre del archivo con el código fuente ")
    file = open(name, 'r')
    line = file.read()
    while True:
        parser.parse(line)
        break

def getAST():
    return ast

parser = yacc.yacc()
