from typing import List

def readline(filepath: str) -> str:
  return open(filepath, 'r').read()

def readlines(filepath: str) -> List[str]:
  with open(filepath) as file:
    return [line.rstrip() for line in file]
