import sys
sys.path.insert(0, '../..')
from utils.reader import read_lines

lines: list[str] = read_lines('./02.txt')
## A rock, B paper, C scissor
## X lose, Y draw, Z win
D: dict[str, str] = dict()
D.setdefault('A X', 'C')
D.setdefault('A Y', 'A')
D.setdefault('A Z', 'B')
D.setdefault('B X', 'A')
D.setdefault('B Y', 'B')
D.setdefault('B Z', 'C')
D.setdefault('C X', 'B')
D.setdefault('C Y', 'C')
D.setdefault('C Z', 'A')

score: int = 0
for line in lines:
  if D[line] == 'A': score += 1
  elif D[line] == 'B': score += 2
  elif D[line] == 'C': score += 3
  if line[2] == 'X': score += 0
  elif line[2] == 'Y': score += 3
  elif line[2] == 'Z': score += 6
print(score)
