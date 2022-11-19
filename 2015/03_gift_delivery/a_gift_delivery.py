import sys
sys.path.insert(0, '../..')
from utils.coordinate import Coordinate
from utils.grid import Grid
from utils.reader import read_line

instructions: str = read_line('./03.txt')

grid: Grid[Coordinate] = Grid()
coordinate: Coordinate = Coordinate()
grid.visit(coordinate)

for instruction in instructions:
  if instruction == '^':
    coordinate = coordinate.moveUp()
  elif instruction == '>':
    coordinate = coordinate.moveRight()
  elif instruction == 'v':
    coordinate = coordinate.moveDown()
  elif instruction == '<':
    coordinate = coordinate.moveLeft()
  
  grid.visit(coordinate)

print(grid.size())
