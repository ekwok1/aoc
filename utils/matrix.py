from dataclasses import dataclass, field
from typing import Generic, TypeVar

T = TypeVar('T')

@dataclass
class Matrix(Generic[T]):
  _height: int
  _width: int
  _values: 'list[list[T]]' = field(default_factory=list)

  def __init__(self, height: int, width: int, defaultValue: T) -> None:
    self._height = height
    self._width = width
    self._values = []
    for _ in range(height):
      self._values.append([defaultValue for _ in range(width)])

  def get(self, height: int, width: int) -> T:
    return self._values[height][width]
  
  def set(self, height: int, width: int, value: T) -> None:
    self._values[height][width] = value

  def count(self, value: T) -> int:
    count: int = 0
    for row in range(self._height):
      for col in range(self._width):
        if self._values[row][col] == value:
          count += 1
    return count
  
  def sum(self: 'Matrix[int]') -> int:
    sum: int = 0
    for row in range(self._height):
      for col in range(self._width):
        sum += int(self._values[row][col])
    return sum
