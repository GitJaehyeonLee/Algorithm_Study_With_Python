alpha_loc = [-1 for _ in range(26)]

a = ord('a')
for i, c in enumerate(input()):
    ord_c = ord(c) - a
    if alpha_loc[ord_c] == -1:
        alpha_loc[ord_c] = i

print(' '.join(str(loc) for loc in alpha_loc))