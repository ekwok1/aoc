import sys
sys.path.insert(0, '../..')
from utils.math import two_min
from utils.reader import read_lines
from utils.string import parse_ints_from_string

dimensionsList: 'list[str]' = read_lines('./02.txt')

wrap: int = 0
for dimensions in dimensionsList:
  length, width, height = parse_ints_from_string(dimensions)
  minA, minB = two_min(length, width, height)
  wrap += 2*length*width + 2*width*height + 2*length*height + minA*minB

print(wrap)
