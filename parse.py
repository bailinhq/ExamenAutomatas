import ply.yacc as yacc
from lex import tokens
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def p_INSTRUCTION(p):
    'instruction : metodo'

def p_METODO(p):
    'metodo : number_assignations ASSIGNATION METODO LEFTPAR INT RIGHTPAR'
#
# def p_METODO2(p):
#     'metodo : NAME ASSIGNATION METODO LEFTPAR INT RIGHTPAR'

def p_METODO_error(p):
    'metodo : NAME ASSIGNATION METODO LEFTPAR INT error'
    print("Found ", p[6].value , " Expected )")


def p_NUMBER_ASSIGNATIONS1(p):
    'number_assignations : NAME'

def p_NUMBER_ASSIGNATIONS2(p):
    'number_assignations : NAME COMMA NAME'

def p_NUMBER_ASSIGNATIONS3(p):
    'number_assignations : NAME COMMA NAME COMMA NAME'

def p_NUMBER_ASSIGNATIONS4(p):
    'number_assignations : NAME COMMA NAME COMMA NAME COMMA NAME COMMA'

def p_NUMBER_ASSIGNATIONS5(p):
    'number_assignations : NAME COMMA NAME COMMA NAME COMMA NAME COMMA NAME'

def p_NUMBER_ASSIGNATIONS5_error(p):
    'number_assignations : NAME error NAME COMMA NAME COMMA NAME COMMA NAME'
#
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

parser = yacc.yacc()
parserAnalysis()