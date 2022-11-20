import sys
sys.path.insert(0, '../..')
from utils.reader import read_lines
from utils.string import parse_ints_from_string

## Name Speed (km/s) Time (s) Rest (s)
reindeer_stats: list[str] = read_lines('./14.txt')

time_limit: int = 2503
max_distance: int = 0
for reindeer_stat in reindeer_stats:
  speed, max_speed_time, rest_time = parse_ints_from_string(reindeer_stat)
  full_cycle_time: int = max_speed_time + rest_time
  full_cycles: int = time_limit // full_cycle_time
  partial_cycle_seconds: int = time_limit - full_cycles * full_cycle_time

  distance: int = full_cycles * speed * max_speed_time
  distance += speed * max_speed_time if partial_cycle_seconds > max_speed_time else partial_cycle_seconds * speed
  if distance > max_distance:
    max_distance = distance

print(max_distance)
