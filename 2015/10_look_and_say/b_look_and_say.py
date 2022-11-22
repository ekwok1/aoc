import sys
sys.path.insert(0, '../..')
from utils.itertools import groupby
from utils.reader import read_line

initial_sequence: str = read_line('./10.txt')

def look_and_say(sequence: str) -> str:
  new_sequence: str = ''
  for key, group in groupby(sequence):
    new_sequence += str(len(list(group))) + key
  return new_sequence

sequence: str = initial_sequence
for _ in range(50):
  sequence = look_and_say(sequence)

print(len(sequence))
