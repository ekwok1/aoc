import sys
sys.path.insert(0, '../..')
from sue_utils import find_sue, get_identifiers, Identifiers
from utils.reader import read_lines

ticker_tape: list[str] = read_lines('./16a.txt')
sues: list[str] = read_lines('./16b.txt')

identifiers_dict: dict[Identifiers, int] = get_identifiers(ticker_tape)

def is_sue(sue_info: str) -> bool:
  identifiers: list[str] = sue_info.split(', ')
  for identifier in identifiers:
    key, value = identifier.split(' ')
    if identifiers_dict[Identifiers[key]] != int(value):
      return False
  return True

print(find_sue(sues, is_sue))
