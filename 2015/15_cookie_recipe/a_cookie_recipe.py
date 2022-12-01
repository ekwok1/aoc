import sys
sys.path.insert(0, '../..')
from recipe_utils import get_ingredient_info, RecipeStat
from utils.itertools import combinations_with_replacement, groupby
from utils.reader import read_lines

## Name capacity durability flavor texture calories
ingredients: list[str] = read_lines('./15.txt')
total_ingredients: int = 100

best_score: int = 0
ingredient_info: dict[str, dict[RecipeStat, int]] = get_ingredient_info(ingredients)
for recipe in combinations_with_replacement(ingredient_info.keys(), total_ingredients):
  capacity = durability = flavor = texture = 0
  for key, group in groupby(recipe):
    count: int = len(list(group))
    capacity += count * ingredient_info[key][RecipeStat.CAPACITY]
    durability += count * ingredient_info[key][RecipeStat.DURABILITY]
    flavor += count * ingredient_info[key][RecipeStat.FLAVOR]
    texture += count * ingredient_info[key][RecipeStat.TEXTURE]
  if capacity < 0 or durability < 0 or flavor < 0 or texture < 0:
    continue
  best_score = max(best_score, capacity * durability * flavor * texture)

print(best_score)
