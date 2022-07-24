rotation_cnt = int(input())

for _ in range(rotation_cnt):
    r, input_text = input().split()
    r = int(r)
    for char in input_text:
        print(char * r, end='')
    print()

