def read_line(filepath: str) -> str:
  return open(filepath, 'r').read()

def read_lines(filepath: str) -> 'list[str]':
  with open(filepath) as file:
    return [line.rstrip() for line in file]
