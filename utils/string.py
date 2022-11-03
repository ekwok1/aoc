import re

def is_vowel(char: str) -> bool:
  vowels: 'set[str]' = set(['a', 'e', 'i', 'o', 'u'])
  return char in vowels

def parse_ints_from_string(string: str) -> 'list[int]':
  return [int(s) for s in re.findall(r'\d+', string)]
