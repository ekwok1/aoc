import sys
sys.path.insert(0, '../..')
from utils.reader import read_lines
from utils.string import parse_int

instructions: list[str] = read_lines('./07.txt')

id_inputs_dictionary: dict[str, list[str]] = dict()
id_signal_dictionary: dict[str, int] = dict()

for instruction in instructions:
  signal, identifier = instruction.split(' -> ')
  split_signal: list[str] = signal.split(' ')
  if len(split_signal) == 1 and parse_int(split_signal[0]) is not None:
    id_signal_dictionary[identifier] = int(split_signal[0])
  else:
    id_inputs_dictionary[identifier] = split_signal

def get_signal(wire_id: str) -> int:
  int_signal: int | None = parse_int(wire_id)
  if int_signal is not None:
    return int_signal
  elif wire_id in id_signal_dictionary:
    return id_signal_dictionary[wire_id]
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
    id_signal_dictionary[wire_id] = signal
    return signal

print(get_signal('a'))
