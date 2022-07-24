word = input()

alpha_lst = [0 for _ in range(26)]
ord_A = ord('A')
for c in word:
    alpha_seq = ord(c.upper()) - ord_A
    alpha_lst[alpha_seq] += 1

is_duplicate = False
max_alphabet = ''
max_cnt = 0

for i, alpha_cnt in enumerate(alpha_lst):
    if max_cnt > alpha_cnt:
        continue
    if max_cnt == alpha_cnt:
        is_duplicate = True
    else:
        is_duplicate = False
        max_alphabet = i
        max_cnt = alpha_cnt

if is_duplicate:
    print("?")
else:
    print(chr(ord_A + max_alphabet))








