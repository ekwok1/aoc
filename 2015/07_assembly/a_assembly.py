import sys
sys.path.insert(0, '../..')
from functools import cache
from utils.reader import read_lines
from utils.string import parse_int

instructions: list[str] = read_lines('./07.txt')

id_inputs_dictionary: dict[str, list[str]] = dict()

for instruction in instructions:
  signal, identifier = instruction.split(' -> ')
  id_inputs_dictionary[identifier] = signal.split(' ')

@cache
def get_signal(wire_id: str) -> int:
  int_signal: int | None = parse_int(wire_id)
  if int_signal is not None:
    return int_signal
  else:
    split_signal: list[str] = id_inputs_dictionary[wire_id]
    if len(split_signal) == 1:
      signal: int = get_signal(split_signal[0])
    else:
      gate: str = split_signal[-2]
      if gate == 'AND':
        signal = get_signal(split_signal[0]) & get_signal(split_signal[2])
      elif gate == 'OR':
        signal = get_signal(split_signal[0]) | get_signal(split_signal[2])
      elif gate == 'NOT':
        signal = ~get_signal(split_signal[1]) & 0xffff
      elif gate == 'RSHIFT':
        signal = get_signal(split_signal[0]) >> get_signal(split_signal[2])
      else: ## 'LSHIFT'
        signal = get_signal(split_signal[0]) << get_signal(split_signal[2])
    return signal

print(get_signal('a'))
print(get_signal.cache_info())
