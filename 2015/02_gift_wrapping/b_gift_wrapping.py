import sys
sys.path.insert(0, '../..')
from utils.math import two_min
from utils.reader import read_lines
from utils.string import parse_ints_from_string

dimensions_list: list[str] = read_lines('./02.txt')

ribbon: int = 0
for dimensions in dimensions_list:
  length, width, height = parse_ints_from_string(dimensions)
  minA, minB = two_min(length, width, height)
  ribbon += 2*minA + 2*minB + length*width*height

print(ribbon)
