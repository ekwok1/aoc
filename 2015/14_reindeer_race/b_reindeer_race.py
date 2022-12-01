import sys
sys.path.insert(0, '../..')
from data_structures.matrix import Matrix
from utils.reader import read_lines
from utils.string import parse_ints_from_string

## Name Speed (km/s) Time (s) Rest (s)
reindeers: list[str] = read_lines('./14.txt')
race_time: int = 2503

matrix: Matrix[int] = Matrix(len(reindeers), race_time, 0)
points: dict[int, int] = dict()

for time in range(race_time):
  furthest_distance: int = 0
  furthest_reindeer: list[int] = []

  for index, reindeer in enumerate(reindeers):
    speed, max_speed_time, rest_time = parse_ints_from_string(reindeer)
    full_cycle_time: int = max_speed_time + rest_time
    current_cycle: int = (time + 1) % full_cycle_time
    is_resting: bool = current_cycle == 0 or current_cycle > max_speed_time
    previous_distance: int = matrix.get(index, time - 1)
    new_distance: int = previous_distance if is_resting else previous_distance + speed

    matrix.set(index, time, new_distance)
    if new_distance > furthest_distance:
      furthest_distance = new_distance
      furthest_reindeer = [index]
    elif new_distance == furthest_distance:
      furthest_reindeer.append(index)

  for reindeer in furthest_reindeer:
    current_points: int | None = points.get(reindeer)
    points[reindeer] = current_points + 1 if current_points != None else 1

print(max(points.values()))
