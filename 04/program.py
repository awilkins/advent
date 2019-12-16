
from password import check


total = 0

for p in range(240920, 789857):
  if check(str(p)):
    total = total + 1

print("Count : ", total)