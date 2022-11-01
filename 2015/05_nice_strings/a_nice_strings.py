import sys
sys.path.insert(0, '../..')
from utils.reader import read_lines
from utils.string import is_vowel

strings: 'list[str]' = read_lines('./05.txt')

forbidden: 'set[str]' = set(['ab', 'cd', 'pq', 'xy'])

def has_forbidden(string: str) -> bool:
  for f in forbidden:
    if string.find(f) > -1:
      return True

  return False

def has_three_vowels(string: str) -> bool:
  count: int = 0

  for char in string:
    if is_vowel(char):
      count += 1

  return count >= 3

def has_repeated_char(string: str) -> bool:
  for index, char in enumerate(string):
    if index != len(string)-1 and char == string[index + 1]:
      return True

  return False

nice: int = 0
for string in strings:
  if not has_forbidden(string) and has_three_vowels(string) and has_repeated_char(string):
    nice += 1

print(nice)
