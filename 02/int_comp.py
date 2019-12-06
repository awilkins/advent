#!/usr/bin/python3


ADD = 1
MUL = 2
END = 99

ERR = -99

memory = []

def op(pc):

  opcode = memory[pc]

  if opcode == END:
    return -1
  
  ptra = memory[pc+1]
  ptrb = memory[pc+2]
  ptrc = memory[pc+3]

  a = memory[ptra]
  b = memory[ptrb]
  
  if opcode == ADD:
    memory[ptrc] = a + b
    return pc + 4
  
  if opcode == MUL:
    memory[ptrc] = a * b
    return pc + 4
  
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


def execute(program):
  global memory
  memory = program

  pc = 0
  while pc >= 0:
    pc = op(pc)
  
  if pc == ERR:
    return "ERROR", memory
  
  return memory[0], memory

def run(program):
  return execute(parse(program))