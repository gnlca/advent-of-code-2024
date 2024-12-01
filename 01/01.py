from typing import Dict


with open("./input.txt", "r") as f:
    lines = f.readlines()

lines = [line.strip("\n") for line in lines]
# PART 1
v1, v2 = map(sorted, zip(*map(lambda line: map(int, line.split()), lines)))
res = sum(abs(int(x) - int(y)) for x, y in zip(v1, v2))
res
# PART 2
m2: Dict[int, int] = {}
for el in v2:
    m2[el] = m2.get(el, 0) + 1

res2 = sum(m2.get(el, 0) * el for el in v1)
print(res2)
