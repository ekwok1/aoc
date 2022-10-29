def readline(filepath: str) -> str:
  return open(filepath, 'r').read()

def readlines(filepath: str) -> "list[str]":
  with open(filepath) as file:
    return [line.rstrip() for line in file]
