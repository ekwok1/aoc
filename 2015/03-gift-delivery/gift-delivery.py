import sys
sys.path.insert(0, '../..')
from utils.reader import readline
from utils.grid import Grid, Location

instructions: str = readline('./03.txt')

grid: Grid = Grid(set())
location: Location = Location()
grid.visit(location)

for instruction in instructions:
  if instruction == '^':
    location = location.moveUp()
  elif instruction == '>':
    location = location.moveRight()
  elif instruction == 'v':
    location = location.moveDown()
  elif instruction == '<':
    location = location.moveLeft()
  
  grid.visit(location)

print(grid.count)
