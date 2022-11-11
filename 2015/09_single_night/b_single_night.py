import sys
sys.path.insert(0, '../..')
from itertools import permutations
from utils.math import max_int
from utils.reader import read_lines

edges: list[str] = read_lines('./09.txt')

locations: set[str] = set()
distances: dict[str, dict[str, int]] = dict()

for edge in edges:
  location1, location2, distance = edge.split(' ')
  locations.add(location1)
  locations.add(location2)
  distances.setdefault(location1, dict())[location2] = int(distance)
  distances.setdefault(location2, dict())[location1] = int(distance)

longest_distance: int = 0
for index, permutation in enumerate(permutations(locations)):
  total_distance: int = sum(map(lambda x, y: distances[x][y], permutation[:-1], permutation[1:]))
  if total_distance > longest_distance:
    longest_distance = total_distance

print(longest_distance)
