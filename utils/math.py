from xmlrpc.client import MAXINT

def two_min(*numbers: int) -> "tuple[int, int]":
  x: int = MAXINT
  y: int = MAXINT
  for number in numbers:
    if number < x:
      y = x
      x = number
    elif number < y:
      y = number
  return x, y
