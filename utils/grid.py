from dataclasses import dataclass

@dataclass
class Grid:
  visited: "set[Location]"
  count: int = 0

  def hasVisited(self, location: "Location") -> bool:
    return location in self.visited

  def visit(self, location: "Location") -> None:
    if not self.hasVisited(location):
      self.count += 1
      self.visited.add(location)

@dataclass
class Location:
  x: int = 0
  y: int = 0

  def moveRight(self) -> "Location":
    return Location(self.x + 1, self.y)

  def moveDown(self) -> "Location":
    return Location(self.x, self.y - 1)

  def moveLeft(self) -> "Location":
    return Location(self.x - 1, self.y)

  def moveUp(self) -> "Location":
    return Location(self.x, self.y + 1)

  def __hash__(self) -> int:
    return hash((self.x, self.y))
