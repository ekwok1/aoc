import sys
sys.path.insert(0, '../..')
from utils.matrix import Matrix
from utils.reader import read_lines
from utils.string import parse_ints_from_string

## Name Speed (km/s) Time (s) Rest (s)
reindeer_stats: list[str] = read_lines('./14.txt')
reindeer_count: int = len(reindeer_stats)
time_limit: int = 2503

matrix: Matrix[int] = Matrix(reindeer_count, time_limit, 0)
points: dict[int, int] = dict()

for time in range(time_limit):
  furthest_distance: int = 0
  furthest_reindeer: list[int] = []

  for reindeer_index, reindeer_stat in enumerate(reindeer_stats):
    speed, max_speed_time, rest_time = parse_ints_from_string(reindeer_stat)
    current_time: int = time + 1
    full_cycle_time: int = max_speed_time + rest_time
    is_resting: bool = current_time % full_cycle_time == 0 or current_time % full_cycle_time > max_speed_time
    previous_distance: int = matrix.get(reindeer_index, time - 1)
    new_distance: int = previous_distance if is_resting else previous_distance + speed

    matrix.set(reindeer_index, time, new_distance)
    if new_distance > furthest_distance:
      furthest_distance = new_distance
      furthest_reindeer = [reindeer_index]
    elif new_distance == furthest_distance:
      furthest_reindeer.append(reindeer_index)
  
  for reindeer in furthest_reindeer:
    current_points: int | None = points.get(reindeer)
    points[reindeer] = current_points + 1 if current_points != None else 1

print(max(points.values()))
