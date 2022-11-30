input: int = 34000000
upper_bound: int = 1000000

houses: list[int] = [0]*upper_bound
for i in range(1, upper_bound):
  counter: int = 0
  for j in range(i, upper_bound, i):
    if counter > 50:
      break
    houses[j] += i * 11
    counter += 1
  if houses[i] > input:
    print(i)
    break
