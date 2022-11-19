import sys
sys.path.insert(0, '../..')
from utils.json import parse_json, sum_ints_in_json
from utils.reader import read_line

document: str = read_line('./12.txt')
  
print(sum_ints_in_json(parse_json(document), 'red'))
