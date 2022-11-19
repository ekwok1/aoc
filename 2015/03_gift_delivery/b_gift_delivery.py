import sys
sys.path.insert(0, '../..')
from utils.coordinate import Coordinate
from utils.grid import Grid
from utils.math import is_even, is_odd
from utils.reader import read_line

instructions: str = read_line('./03.txt')

grid: Grid[Coordinate] = Grid()
santa_coordinate: Coordinate = Coordinate()
robo_coordinate: Coordinate = Coordinate()
grid.visit(santa_coordinate)
grid.visit(robo_coordinate)

for index, instruction in enumerate(instructions):
  if instruction == '^':
    santa_coordinate = santa_coordinate.moveUp() if is_even(index) else santa_coordinate
    robo_coordinate = robo_coordinate.moveUp() if is_odd(index) else robo_coordinate
  elif instruction == '>':
    santa_coordinate = santa_coordinate.moveRight() if is_even(index) else santa_coordinate
    robo_coordinate = robo_coordinate.moveRight() if is_odd(index) else robo_coordinate
  elif instruction == 'v':
    santa_coordinate = santa_coordinate.moveDown() if is_even(index) else santa_coordinate
    robo_coordinate = robo_coordinate.moveDown() if is_odd(index) else robo_coordinate
  elif instruction == '<':
    santa_coordinate = santa_coordinate.moveLeft() if is_even(index) else santa_coordinate
    robo_coordinate = robo_coordinate.moveLeft() if is_odd(index) else robo_coordinate
  
  grid.visit(santa_coordinate if is_even(index) else robo_coordinate)

print(grid.size())
