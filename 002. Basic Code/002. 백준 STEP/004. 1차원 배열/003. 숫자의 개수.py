import sys

num_cnts = [0 for _ in range(10)]

n1 = int(sys.stdin.readline().rstrip())
n2 = int(sys.stdin.readline().rstrip())
n3 = int(sys.stdin.readline().rstrip())

gop = str(n1 * n2 * n3)

for c in gop:
    num_cnts[int(c)] += 1

for num_cnt in num_cnts:
    print(num_cnt)


