import sys
sys.path.insert(0, '../..')
from utils import readlines, two_min

gifts: "list[str]" = readlines('./02.txt')

wrap: int = 0
ribbon: int = 0
for gift in gifts:
  length, width, height = list(map(lambda dimension: int(dimension), gift.split('x')))
  minA, minB = two_min(length, width, height)
  wrap += 2*length*width + 2*width*height + 2*length*height + minA*minB
  ribbon += 2*minA + 2*minB + length*width*height
print(wrap, ribbon)
