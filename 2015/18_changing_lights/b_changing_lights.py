import sys
sys.path.insert(0, '../..')
from data_structures.matrix import Matrix
from utils.reader import read_lines

matrix_data: list[str] = read_lines('./18.txt')

light_grid: Matrix[bool] = Matrix(len(matrix_data), len(matrix_data[0]), False)
light_grid.fill(matrix_data, lambda light: light == '#')

def get_next_state(y: int, x: int) -> bool:
  if light_grid.is_corner(y, x): return True
  current_state: bool = light_grid.get(y, x)
  neighbors: list[bool] = light_grid.get_neighbors(y, x)
  on_neighbors_count: int = len(list(filter(lambda neighbor: neighbor, neighbors)))
  return on_neighbors_count == 2 or on_neighbors_count == 3 if current_state else on_neighbors_count == 3

def animate(light_grid: Matrix[bool]) -> Matrix[bool]:
  animated_light_grid: Matrix[bool] = Matrix(len(matrix_data), len(matrix_data[0]), False)
  for y, row in enumerate(light_grid.values):
    for x, _ in enumerate(row):
      animated_light_grid.set(y, x, get_next_state(y, x))
  return animated_light_grid

for _ in range(100):
  light_grid = animate(light_grid)
print(light_grid.count(True))
