import sys
sys.path.insert(0, '../..')
from utils.reader import read_lines
from utils.string import parse_ints_from_string

## Name Speed (km/s) Time (s) Rest (s)
reindeers: list[str] = read_lines('./14.txt')
race_time: int = 2503

furthest_distance: int = 0
for reindeer in reindeers:
  speed, max_speed_time, rest_time = parse_ints_from_string(reindeer)
  full_cycle_time: int = max_speed_time + rest_time
  full_cycles: int = race_time // full_cycle_time
  partial_cycle_time: int = race_time % full_cycle_time
  distance: int = full_cycles * speed * max_speed_time
  distance += speed * max_speed_time if partial_cycle_time > max_speed_time else speed * partial_cycle_time
  furthest_distance = max(furthest_distance, distance)
print(furthest_distance)
