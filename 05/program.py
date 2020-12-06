from queue import Queue

from intcomp import parse, execute

program = parse(open("./program.txt").readline())

input = Queue()
output = Queue()

input.put(1)
result, memory = execute(program, input, output)

r = output.get()
while not output.empty():
  if r != 0:
    print("Brainfart")
  r = output.get()

print("Output:", r)
