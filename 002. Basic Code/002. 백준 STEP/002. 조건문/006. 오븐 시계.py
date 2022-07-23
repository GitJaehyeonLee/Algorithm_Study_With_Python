h, m = map(int, input().split())
cooking_time = int(input())

m = m + cooking_time
if m >= 60:
    plus_hour = m // 60
    m = m - plus_hour * 60
    h = (h + plus_hour) % 24

print(h, m)
