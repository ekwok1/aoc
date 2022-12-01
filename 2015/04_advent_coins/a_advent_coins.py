import sys
sys.path.insert(0, '../..')
from utils.hash import md5_encode

secretKey: str = 'yzbqklnj'

i: int = 0
while True:
  hash: str = md5_encode(secretKey + str(i))
  if hash.startswith('00000'):
    break
  else:
    i += 1

print(i)
