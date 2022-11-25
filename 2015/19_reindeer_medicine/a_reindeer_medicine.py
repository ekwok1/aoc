import sys
sys.path.insert(0, '../..')
from utils.reader import read_line, read_lines

initial_molecule: str = read_line('./19.txt')
replacements: list[str] = read_lines('./19_replacements.txt')

replacement_dict: dict[str, list[str]] = dict()
max_from_length: int = 0
for replacement in replacements:
  f, t = replacement.split(' => ')
  max_from_length = max(max_from_length, len(f))
  if replacement_dict.get(f) is None:
    replacement_dict.setdefault(f, [t])
  else:
    replacement_dict[f].append(t)

replaced_set: set[str] = set()
for i, _ in enumerate(initial_molecule):
  for j in range(1, max_from_length+1):
    replacement_list: list[str] | None = replacement_dict.get(initial_molecule[i:i+j])
    if replacement_list is not None:
      for replacement in replacement_list:
        molecule_with_replacement: str = initial_molecule[:i] + replacement + initial_molecule[i+j:]
        replaced_set.add(molecule_with_replacement)

print(len(replaced_set))
