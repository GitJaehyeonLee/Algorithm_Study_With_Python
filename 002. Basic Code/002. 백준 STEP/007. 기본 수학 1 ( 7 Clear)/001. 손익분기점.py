import math
a, b, c = map(int, input().split())

if c - b > 0:
    print(math.ceil((a + 1) / (c - b)))
else:
    print(-1)