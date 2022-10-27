import sys

def readline(filepath: str) -> str:
  return open(filepath, 'r').read()

def readlines(filepath: str) -> "list[str]":
  with open(filepath) as file:
    return [line.rstrip() for line in file]

def two_min(*numbers: int) -> "tuple[int, int]":
  x: int = sys.maxsize * 2 + 1
  y: int = sys.maxsize * 2 + 1
  for number in numbers:
    if number < x:
      y = x
      x = number
    elif number < y:
      y = number
  return x, y
