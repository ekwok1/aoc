from xmlrpc.client import MAXINT

def is_even(number: int) -> bool:
  return number % 2 == 0

def is_odd(number: int) -> bool:
  return number % 2 != 0

def two_min(*numbers: int) -> 'tuple[int, int]':
  x: int = MAXINT
  y: int = MAXINT
  for number in numbers:
    if number < x:
      y = x
      x = number
    elif number < y:
      y = number
  return x, y
