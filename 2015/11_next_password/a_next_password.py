import sys
sys.path.insert(0, '../..')
from utils.string import has_forbidden_characters, has_pairs, has_three_sequence, increment_string

initial_password: str = 'cqjxjnds'

def get_next_password(password: str) -> str:
  next_password = password
  while True:
    next_password: str = increment_string(next_password)
    if has_forbidden_characters(next_password, 'iol') or not has_pairs(next_password, 2) or not has_three_sequence(next_password):
      continue
    return next_password

print(get_next_password(initial_password))
