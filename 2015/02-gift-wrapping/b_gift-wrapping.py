import sys
sys.path.insert(0, '../../utils')
from utils.reader import read_lines
from utils.math import two_min

gifts: "list[str]" = read_lines('./02.txt')

ribbon: int = 0
for gift in gifts:
  length, width, height = list(map(lambda dimension: int(dimension), gift.split('x')))
  minA, minB = two_min(length, width, height)
  ribbon += 2*minA + 2*minB + length*width*height
print(ribbon)
