
def ascends(password):
  for index in range(1, len(password)):
    if password[index - 1] > password[index]:
      return False
  return True

def has_double(password):
  for index in range(1, len(password)):
    if password[index - 1] == password[index]:
      return True
  return False

def check(password):
  return ascends(password) and has_double(password)
