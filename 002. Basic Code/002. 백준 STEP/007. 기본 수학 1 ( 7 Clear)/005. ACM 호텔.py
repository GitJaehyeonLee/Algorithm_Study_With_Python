rec_cnt = int(input())

for _ in range(rec_cnt):
    h, w, n = map(int, input().split())
    if n % h == 0:
        floor = h
        room_no = n // h
    else:
        floor = n % h
        room_no = n // h + 1

    print(floor * 100 + room_no)