serch_seq = int(input())
total = 0
i = 0
while total < serch_seq:
    i += 1
    total += i

bunmo = i - (total - serch_seq)
bunza = i - bunmo + 1
if i % 2 == 1:
    bunmo, bunza = bunza, bunmo
print(f"{bunmo}/{bunza}")