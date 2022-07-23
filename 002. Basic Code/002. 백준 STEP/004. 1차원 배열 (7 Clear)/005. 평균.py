_ = input()
num_lsts = list(map(int, input().split()))

print(( sum(num_lsts) / max(num_lsts)) * 100 / len(num_lsts))
