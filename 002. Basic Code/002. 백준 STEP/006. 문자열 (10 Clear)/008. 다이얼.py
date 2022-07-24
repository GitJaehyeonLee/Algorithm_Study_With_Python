ALPHABET_DIAL_CONVERTER = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9]
in_text = input()

ord_A = ord('A')
ans = 0
for text in in_text:
    ans += ALPHABET_DIAL_CONVERTER[ord(text) - ord_A] + 1

print(ans)
