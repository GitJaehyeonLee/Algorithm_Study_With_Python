A, B, C = sorted(map(int, input().split()))

if A == C:
    print(10000 + A * 1000)
elif A == B or B == C:
    print(1000 + B * 100)
else:
    print(C * 100)