import sys
sys.path.insert(0, '../..')
from utils.reader import read_line, read_lines

data: str = read_line('./01.txt')
lines: list[str] = read_lines('./01.txt')

max_cal: int = 0
second_max: int = 0
third_max: int = 0
cal: int = 0
for line in lines:
  if line == '':
    print("line is empty")
    print("cal:", cal)
    if cal > max_cal:
      third_max = second_max
      second_max = max_cal
      max_cal = cal
    elif cal > second_max:
      third_max = second_max
      second_max = cal
    elif cal > third_max:
      third_max = cal
    cal = 0
  else:
    print("cal before adding:", cal)
    cal += int(line)
    print("cal after adding")

print(max_cal + second_max + third_max)
