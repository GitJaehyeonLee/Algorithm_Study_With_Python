t_cnt = int(input())
answers = []
for _ in range(t_cnt):
    A, B = map(int, input().split())
    answers.append(A + B)

for answer in answers:
    print(answer)