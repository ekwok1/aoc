import sys
sys.path.insert(0, '../..')
from utils.reader import read_lines
from utils.string import find_matches

strings: list[str] = read_lines('./08.txt')

encoded_character_total_count: int = 0
string_literal_character_total_count: int = 0
for string in strings:
  literal_character_count: int = len(string)
  string_literal_character_total_count += literal_character_count

  matches: list[str] = find_matches(r'\\|"', string)
  encoded_character_total_count += literal_character_count + len(matches) + 2

print(encoded_character_total_count - string_literal_character_total_count)
