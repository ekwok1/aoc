import sys
sys.path.insert(0, '../..')
from utils.itertools import get_all_combinations
from utils.reader import read_lines_as_int

sizes: list[int] = read_lines_as_int('./17.txt')

def count_combinations(total_size: int) -> int:
  count: int = 0
  for combination in get_all_combinations(sizes, 1):
    count = count + 1 if sum(combination) == total_size else count
  return count

print(count_combinations(150))
