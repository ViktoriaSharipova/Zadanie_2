number = int(input("Введите целое число: "))

n1 = number % 10
number = number // 10
n2 =  number % 10
number = number // 10
n3 =  number % 10
number = number // 10
n4 =  number % 10
number = number // 10
res = n1 * 1000 + n2* 100 + n3 * 10 + n4
print(res)