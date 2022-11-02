import sys
sys.path.insert(0, '../..')
from utils.reader import read_lines
from utils.string import is_vowel

strings: 'list[str]' = read_lines('./05.txt')

def has_repeated_pair(string: str) -> bool:
  for index, char in enumerate(string):
    if index < len(string) - 1:
      pair: str = char + string[index + 1]
      if string.find(pair, index + 2) > -1:
        return True
  return False

def has_letter_sandwich(string: str) -> bool:
  for index, char in enumerate(string):
    if index < len(string) - 2:
      if char == string[index + 2]:
        return True
  return False

nice: int = 0
for string in strings:
  if has_repeated_pair(string) and has_letter_sandwich(string):
    nice += 1

print(nice)
