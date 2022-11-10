import sys
sys.path.insert(0, '../..')
from utils.reader import read_lines
from utils.string import find_matches

strings: list[str] = read_lines('./08.txt')

string_literal_character_total_count: int = 0
in_memory_character_total_count: int = 0
for string in strings:
  literal_character_count: int = len(string)
  string_literal_character_total_count += literal_character_count

  in_memory_character_count: int = literal_character_count
  matches: list[str] = find_matches(r'\\x..|\\\\|"|\\"', string)
  for match in matches:
    in_memory_character_count = in_memory_character_count - 3 if len(match) > 2 else in_memory_character_count - 1
  in_memory_character_total_count += in_memory_character_count

print(string_literal_character_total_count - in_memory_character_total_count)
