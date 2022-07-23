nums = [0 for _ in range(10001)]

def make_dr_num(num):
    dr_num = num
    for num_p in str(num):
        dr_num += int(num_p)
    return dr_num


for num in range(1, 10001):
    if nums[num] == 0:
        print(num)
    while num <= 10000:
        if nums[num] == 1:
            break
        else:
            nums[num] = 1
        num = make_dr_num(num)