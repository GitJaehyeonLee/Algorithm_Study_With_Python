target = int(input())

pre = 1
ans = 1
while pre < target:
    pre += 6 * ans
    ans = ans + 1

print(ans)
