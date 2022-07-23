import sys

n, x = map(int, sys.stdin.readline().rstrip().split())
num_lst = list(map(int, sys.stdin.readline().rstrip().split()))

for num in num_lst:
    if num < x:
        print(num, end=' ')