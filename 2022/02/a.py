import sys
sys.path.insert(0, '../..')
from utils.reader import read_line, read_lines

data: str = read_line('./.txt')
lines: list[str] = read_lines('./.txt')

print(data)

for line in lines:
  print(line)
