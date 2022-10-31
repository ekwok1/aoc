import sys
sys.path.insert(0, '../../utils')
from utils.reader import readline

instructions: str = readline('./01.txt')

floor: int = 0
for instruction in instructions:
  floor = floor + 1 if instruction == '(' else floor - 1
print(floor)
