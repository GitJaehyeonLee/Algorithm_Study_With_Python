max_num = 0
max_seq = 0

for i in range(1, 10):
    num = int(input())
    if max_num < num:
        max_num = num
        max_seq = i

print(max_num)
print(max_seq)