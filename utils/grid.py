from dataclasses import dataclass, field
from typing import Generic, TypeVar

T = TypeVar('T')

@dataclass
class Grid(Generic[T]):
  _visited: "set[T]" = field(default_factory=set)

  def size(self) -> int:
    return len(self._visited)

  def visited(self, obj: T) -> bool:
    return obj in self._visited
  
  def visit(self, obj: T) -> None:
    if not self.visited(obj):
      self._visited.add(obj)
