input: int = 34000000
upper_bound: int = 1000000

houses: list[int] = [0]*upper_bound
for i in range(1, upper_bound):
  for j in range(i, upper_bound, i):
    houses[j] += i * 10
  if houses[i] > input:
    print(i)
    break
