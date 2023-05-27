#!/usr/bin/python3

from int_comp import parse, execute, dump

def nounverb(noun, verb):
  return (100 * noun) + verb


GOAL = 19690720

def main():
  noun = 4 
  verb = 0
  program = open("./program.txt").readline()
  memory = parse(program)

  # These bits were for working out how complex the program is
  vartable = {
    0: "OUT",
    1: "A",
    2: "B",
  }
  # dump(memory, vartable)
  # Not really necessary.. 
  # All the possible inputs are already in the program (because it has no
  # literals, only pointers) so you can bruteforce it

  for noun in range(len(memory)):
    for verb in range(len(memory)):
      memory = parse(program)
      memory[1] = noun
      memory[2] = verb
      output, _ = execute(memory)
      if output == GOAL:
        # This is the real answer
        print(nounverb(noun, verb))
        return


main()


