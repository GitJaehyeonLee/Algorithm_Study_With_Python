import math
a, b, v = map(int, input().split())

today = a - b
ans = math.ceil(v / today)

for i in range(a // today + 1, -1, -1):
    if (today * (ans - i) + a) >= v:
        print(ans - i + 1)
        break
else:
    print(ans + 1)