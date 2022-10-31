import sys
sys.path.insert(0, '../..')
from utils.reader import readline
from utils.grid import Grid
from utils.coordinate import Coordinate

instructions: str = readline('./03.txt')

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
