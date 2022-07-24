num1, num2 = input().split()

num1 = int(num1[2]) * 100 + int(num1[1]) * 10 + int(num1[0])
num2 = int(num2[2]) * 100 + int(num2[1]) * 10 + int(num2[0])

print(max(num1, num2))
