import sys
sys.path.insert(0, '../..')
from utils.reader import read_lines

lines: list[str] = read_lines('./02.txt')
## A rock, B paper, C scissor
## X rock, Y paper, Z scissor
D: dict[str, str] = dict()
D.setdefault('A X', 'draw')
D.setdefault('A Y', 'win')
D.setdefault('A Z', 'loss')
D.setdefault('B X', 'loss')
D.setdefault('B Y', 'draw')
D.setdefault('B Z', 'win')
D.setdefault('C X', 'win')
D.setdefault('C Y', 'loss')
D.setdefault('C Z', 'draw')

score: int = 0
for line in lines:
  if D[line] == 'loss': score += 0
  elif D[line] == 'draw': score += 3
  elif D[line] == 'win': score += 6
  if line[2] == 'X': score += 1
  elif line[2] == 'Y': score += 2
  elif line[2] == 'Z': score += 3
print(score)
