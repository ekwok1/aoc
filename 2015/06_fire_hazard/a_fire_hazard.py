import sys
sys.path.insert(0, '../..')
from utils.reader import read_lines
from utils.string import parse_ints_from_string
from utils.matrix import Matrix

instructions: 'list[str]' = read_lines('./06.txt')

matrix: Matrix[bool] = Matrix(1000, 1000, False)

for instruction in instructions:
  action: str = instruction.split()[0]
  x1, y1, x2, y2 = parse_ints_from_string(instruction)

  for y in range(y1, y2+1):
    for x in range(x1, x2+1):
      if action == 'on':
        matrix.set(y, x, True)
      elif action == 'off':
        matrix.set(y, x, False)
      elif action == 'toggle':
        matrix.set(y, x, not matrix.get(y, x))

print(matrix.count(True))
