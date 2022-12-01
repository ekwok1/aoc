import sys
sys.path.insert(0, '../..')
from utils.reader import read_lines

lines: list[str] = read_lines('./01.txt')

max_calories: int = 0
second_max_calories: int = 0
third_max_calories: int = 0
cal: int = 0
for line in lines:
  if line == '':
    if cal > max_calories:
      third_max_calories = second_max_calories
      second_max_calories = max_calories
      max_calories = cal
    elif cal > second_max_calories:
      third_max_calories = second_max_calories
      second_max_calories = cal
    elif cal > third_max_calories:
      third_max_calories = cal
    cal = 0
  else:
    cal += int(line)

print(max_calories)
print(max_calories + second_max_calories + third_max_calories)
