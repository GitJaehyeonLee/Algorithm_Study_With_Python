lst = [0]
lst.extend([1 for _ in range(99)])
lst.extend([0 for _ in range(950)])

input_num = int(input())

for i in range(100, input_num + 1):
    num = list(str(i))
    if int(num[0]) - int(num[1]) == int(num[1]) - int(num[2]):
        lst[i] = 1

print(sum(lst[:input_num + 1]))