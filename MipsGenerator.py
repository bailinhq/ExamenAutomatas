from semantic import *

def generateCode():
    file = open('code.asm', 'w')
    semanticAnalysis()
    ast = getAST()
    generate(ast, file)
    file.close()

def generate(ast, file):
    file.write(".data \n")
    file.write('strInput: .asciiz "Inserte un valor" \n')
    for instruction in ast.instructions:
        if type(instruction) is Metodo:
            for parameter in instruction.parameters:
                file.write(parameter + ': .word ?' +'\n')
    file.write(".text \n")
    file.write(".globl main \n")
    file.write("main: \n")
    for instruction in ast.instructions:
        if type(instruction) is Metodo:
            file.write('la $a0, strInput \n')
            for parameter in instruction.parameters:
                file.write('li $v0, 4 \nsyscall\n')
                file.write('li $v0, 5 \nsyscall\n')
                file.write('sw $v0, ' + parameter + '\n')

        if type(instruction) is Print:
            file.write('li $v0, 1\nlw $a0, ' + instruction.parameter + '\nsyscall\n')

    file.write('li $v0, 10 \nsyscall')
generateCode()