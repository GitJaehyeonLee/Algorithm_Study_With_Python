croatia_alphabet_back = ['-', '=', 'j']
croatia_alphabet = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
text = input()
ans = 0
keep = 0
i = len(text) - 1
while i > -1:
    if text[i] in croatia_alphabet_back:
        if i > 1 and text[i - 2:i + 1] == 'dz=':
            i = i - 2
        elif i > 0 and text[i - 1:i + 1] in croatia_alphabet:
            i = i - 1
    ans += 1
    i = i - 1

print(ans)