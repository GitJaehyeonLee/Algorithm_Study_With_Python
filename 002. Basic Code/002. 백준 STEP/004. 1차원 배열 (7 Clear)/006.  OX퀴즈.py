r_num = int(input())

for _ in range(r_num):
    input_oxs = input()
    score = 0
    pre = 0
    for ox in input_oxs:
        if ox == "O":
            pre = pre + 1
            score = score + pre
        else:
            pre = 0
    print(score)
