from dataclasses import dataclass

@dataclass
class Coordinate:
  x: int = 0
  y: int = 0

  def moveRight(self) -> "Coordinate":
    return Coordinate(self.x + 1, self.y)

  def moveDown(self) -> "Coordinate":
    return Coordinate(self.x, self.y - 1)

  def moveLeft(self) -> "Coordinate":
    return Coordinate(self.x - 1, self.y)

  def moveUp(self) -> "Coordinate":
    return Coordinate(self.x, self.y + 1)

  def __hash__(self) -> int:
    return hash((self.x, self.y))