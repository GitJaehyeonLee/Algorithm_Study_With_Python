h, m = map(int, input().split())

m = m - 45
if m < 0:
    m = m + 60
    h = 23 if h == 0 else h - 1

print(h, m)