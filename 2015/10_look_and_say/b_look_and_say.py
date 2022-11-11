import sys
sys.path.insert(0, '../..')
from utils.reader import read_line

initial_sequence: str = read_line('./10.txt')

def look_and_say(sequence: str) -> str:
  new_sequence: str = ''
  counter: int = 1
  for index, char in enumerate(sequence):
    if index < len(sequence) - 1 and char == sequence[index + 1]:
      counter += 1
    else:
      new_sequence += str(counter) + char
      counter = 1
  return new_sequence

sequence: str = initial_sequence
for _ in range(50):
  sequence = look_and_say(sequence)

print(len(sequence))

# 828xxxx was too high
