#!/usr/bin/python3

import queue

ADD = 1
MUL = 2
INP = 3
OUT = 4

IMMEDIATE = 1000

END = 99

ERR = -99

memory = []
stdin = queue.Queue()
stdout = queue.Queue()

def op(pc):

  opcode = memory[pc] % 100
  modemask = memory[pc] // 100

  modea = modemask % 10
  modemask = modemask // 10
  modeb = modemask % 10
  modemask = modemask // 10
  modec = modemask % 10
  modemask = modemask // 10

  if opcode == END:
    return -1

  ptra = memory[pc+1]
  ptrb = 0
  ptrc = 0
  if opcode < INP:
    ptrb = memory[pc+2]
    ptrc = memory[pc+3]

  a = ptra
  if not modea:
    a = memory[a]

  b = ptrb
  if not modeb:
    b = memory[b]

  if opcode == ADD:
    memory[ptrc] = a + b
    return pc + 4

  if opcode == MUL:
    memory[ptrc] = a * b
    return pc + 4

  if opcode == INP:
    memory[ptra] = stdin.get()
    return pc + 2

  if opcode == OUT:
    stdout.put(a)
    return pc + 2

  return ERR

def parse(program):
  return list([int(x) for x in program.split(",")])

vartable = {}

def var(val):
  if val in vartable:
    return vartable[val]
  return val

def dump(program, vars):
  global vartable
  vartable = vars
  pc = 0
  while pc < len(program):
    opcode = program[pc]

    opname = ""
    if opcode == ADD:
      opname = "ADD"
    if opcode == MUL:
      opname = "MUL"
    if opcode == END:
      return

    ptrA = program[pc+1]
    ptrB = program[pc+2]
    ptrC = program[pc+3]

    vartable[ptrC] = "VAR(%d)" % ptrC

    if not ptrA in vartable:
      ptrA = "CONST(%d)" % program[ptrA]

    if not ptrB in vartable:
      ptrB = "CONST(%d)" % program[ptrB]

    print(opname, var(ptrA), var(ptrB), var(ptrC))
    pc = pc + 4


def execute(program, input=None, output=None):
  global memory
  global stdin
  global stdout

  memory = program
  if not input is None:
    stdin = input
  if not output is None:
    stdout = output

  pc = 0
  while pc >= 0:
    print(pc, memory)
    pc = op(pc)

  if pc == ERR:
    return "ERROR", memory

  return memory[0], memory

def run(program):
  return execute(parse(program))



program = [1002, 4, 3, 4, 33]
# program = [1101, 100, -1, 4, 0]
execute(program)