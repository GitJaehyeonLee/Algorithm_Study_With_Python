rec_cnt = int(input())

group_word_cnt = 0
ord_a = ord('a')

for _ in range(rec_cnt):
    is_group_alpha = True
    alphabet_table = [-1 for _ in range(26)]
    word = input()
    for i, c in enumerate(word):
        c_alpha_seq = ord(c) - ord_a
        if alphabet_table[c_alpha_seq] != -1 and alphabet_table[c_alpha_seq] != i - 1:
            is_group_alpha = False
            break
        alphabet_table[c_alpha_seq] = i

    if is_group_alpha:
        group_word_cnt += 1

print(group_word_cnt)