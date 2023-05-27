
def ascends(password):
  for index in range(1, len(password)):
    if password[index - 1] > password[index]:
      return False
  return True

def has_double(password):
  digit_count = {}
  for index in range(1, len(password)):
    if password[index - 1] == password[index]:
      if not password[index] in digit_count:
        digit_count[password[index]] = 2
      else:
        digit_count[password[index]] = digit_count[password[index]] + 1

  for v in digit_count.values():
    if v == 2:
      return True

  return False

def check(password):
  return ascends(password) and has_double(password)
