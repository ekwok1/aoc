from enum import Enum
from utils.string import parse_ints_from_string

class RecipeStat(Enum):
  CAPACITY = 'capacity'
  DURABILITY = 'durability'
  FLAVOR = 'flavor'
  TEXTURE = 'texture'
  CALORIES = 'calories'

def get_ingredient_info(ingredients: list[str]) -> dict[str, dict[RecipeStat, int]]:
  ingredient_info: dict[str, dict[RecipeStat, int]] = dict()
  for ingredient in ingredients:
    name: str = ingredient.split(' ')[0]
    capacity, durability, flavor, texture, calories = parse_ints_from_string(ingredient)
    ingredient_info[name] = dict()
    ingredient_info[name][RecipeStat.CAPACITY] = capacity
    ingredient_info[name][RecipeStat.DURABILITY] = durability
    ingredient_info[name][RecipeStat.FLAVOR] = flavor
    ingredient_info[name][RecipeStat.TEXTURE] = texture
    ingredient_info[name][RecipeStat.CALORIES] = calories
  return ingredient_info