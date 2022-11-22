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
    k, v = identifier.split(' ')
    key: Identifiers = Identifiers[k]
    value: int = int(v)
    if (key == Identifiers.cats or key == Identifiers.trees):
      if value <= identifiers_dict[key]:
        return False
    elif (key == Identifiers.pomeranians or key == Identifiers.goldfish):
      if value >= identifiers_dict[key]:
        return False
    elif identifiers_dict[key] != value:
      return False
  return True

print(find_sue(sues, is_sue))
