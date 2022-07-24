rec_cnt = int(input())
for _ in range(rec_cnt):
    lst = [i + 1 for i in range(16)]
    k = int(input())
    n = int(input())
    for _ in range(k):
        for j in range(1, n + 1):
            lst[j] = lst[j] + lst[j - 1]
    print(lst[n - 1])

# i_lst = [1, 2, 3]
#
# print(sum(i_lst[:2]))