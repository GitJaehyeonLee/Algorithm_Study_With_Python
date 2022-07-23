import sys

num = int(sys.stdin.readline())
org_num = num
i = 0

while True:
    i = i + 1
    n = num // 10
    m = num % 10
    num = m * 10 + ((n + m) % 10)
    if org_num == num:
        break

print(i)