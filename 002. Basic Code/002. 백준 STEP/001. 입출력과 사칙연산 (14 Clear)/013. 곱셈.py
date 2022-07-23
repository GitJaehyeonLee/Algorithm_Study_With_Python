num1 = int(input())
str_num2 = input()

for i in range(2, -1, -1):
    print(num1 * int(str_num2[i]))
print(num1 * int(str_num2))