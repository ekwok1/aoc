import sys
sys.path.insert(0, '../..')
from utils.reader import read_lines
from utils.math import two_min

gifts: 'list[str]' = read_lines('./02.txt')

wrap: int = 0
for gift in gifts:
  length, width, height = list(map(lambda dimension: int(dimension), gift.split('x')))
  minA, minB = two_min(length, width, height)
  wrap += 2*length*width + 2*width*height + 2*length*height + minA*minB
print(wrap)
