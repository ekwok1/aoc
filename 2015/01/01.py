import sys
sys.path.insert(0, '../..')
from utils import readline

instructions = readline('./01.txt')

floor = 0

for instruction in instructions:
  if instruction == '(':
    floor += 1
  else:
    floor -= 1

print(floor)
