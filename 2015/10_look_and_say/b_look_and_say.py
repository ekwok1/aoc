import sys
sys.path.insert(0, '../..')
from utils.itertools import groupby

initial_sequence: str = '3113322113'

def look_and_say(sequence: str) -> str:
  new_sequence: str = ''
  for key, group in groupby(sequence):
    new_sequence += str(len(list(group))) + key
  return new_sequence

sequence: str = initial_sequence
for _ in range(50):
  sequence = look_and_say(sequence)

print(len(sequence))
