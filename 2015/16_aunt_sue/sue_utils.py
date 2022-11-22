from enum import Enum
from typing import Callable

class Identifiers(Enum):
  akitas = 0
  cars = 1
  cats = 2
  children = 3
  goldfish = 4
  perfumes = 5
  pomeranians = 6
  samoyeds = 7
  trees = 8
  vizslas = 9

def get_identifiers(ticker_tape: list[str]) -> dict[Identifiers, int]:
  identifiers: dict[Identifiers, int] = dict()
  for identifier in ticker_tape:
    k, v = identifier.split(' ')
    identifiers[Identifiers[k]] = int(v)
  return identifiers

def find_sue(sues: list[str], func: Callable[[str], bool]) -> int:
  for index, sue in enumerate(sues):
    if func(sue):
      return index + 1
  return -1