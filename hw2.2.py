number = int(input("Enter your number: "))
print(number)

n1 = number // 10000
n2 = number // 1000 % 10
n3 = number // 100 % 10
n4 = number % 100 // 10
n5 = number % 10

12
result = n5 * 10000 + n4 * 1000 + n3 * 100 + n2 * 10 + n1
print(result)