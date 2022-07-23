namuge_num = [0 for _ in range(42)]

for _ in range(10):
    namuge = int(input()) % 42
    if namuge_num[namuge] != 1:
        namuge_num[namuge] += 1

print(sum(namuge_num))
