import sys
sys.path.insert(0, '../..')
from typing import List
from utils import readlines

instructions: List[str] = readlines('./02.txt')

print(instructions)
