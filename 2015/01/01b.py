import sys
sys.path.insert(0, '../..')
from utils import readline

instructions: str = readline('./01.txt')

floor: int = 0
for index, instruction in enumerate(instructions):
  floor = floor + 1 if instruction == '(' else floor - 1
  if floor == -1: print(index + 1); break
