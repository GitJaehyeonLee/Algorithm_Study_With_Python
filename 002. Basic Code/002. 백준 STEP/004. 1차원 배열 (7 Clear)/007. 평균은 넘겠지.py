r_num = int(input())

for _ in range(r_num):
    score_lst = list(map(int, input().split()))
    avg_score = sum(score_lst[1:]) / score_lst[0]
    avg_score_up_cnt = 0
    for score in score_lst[1:]:
        if score > avg_score:
            avg_score_up_cnt += 1
    # print("%.3f%%" % ((round(avg_score_up_cnt / score_lst[0] * 100, 3))))
    print(f"{(round(avg_score_up_cnt / score_lst[0] * 100, 3)): .3f}%")