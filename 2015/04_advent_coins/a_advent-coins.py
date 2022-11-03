import hashlib
import sys
sys.path.insert(0, '../..')
from utils.reader import read_line

secretKey: str = read_line('./04.txt')

i: int = 0
while True:
  hash: str = hashlib.md5((secretKey + str(i)).encode()).hexdigest()
  if hash.startswith('00000'):
    break
  else:
    i += 1

print(i)
