import sys
sys.path.insert(0, '../..')
from utils.matrix import Matrix
from utils.reader import read_lines
from utils.string import parse_ints_from_string

matrix: Matrix[int] = Matrix(1000, 1000, 0)

instructions: list[str] = read_lines('./06.txt')

for instruction in instructions:
  action: str = instruction.split()[0]
  x1, y1, x2, y2 = parse_ints_from_string(instruction)

  for y in range(y1, y2+1):
    for x in range(x1, x2+1):
      if action == 'on':
        matrix.set(y, x, matrix.get(y, x) + 1)
      elif action == 'off':
        curr: int = matrix.get(y, x)
        matrix.set(y, x, curr - 1 if curr > 0 else 0)
      elif action == 'toggle':
        matrix.set(y, x, matrix.get(y, x) + 2)

print(matrix.sum())
