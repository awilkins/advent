
from int_comp import run, parse, execute

programFile = open("./program.txt")

program = programFile.readline()

memory = parse(program)
memory[1] = 0
memory[2] = 0

output, memory = execute(memory)

print(output)