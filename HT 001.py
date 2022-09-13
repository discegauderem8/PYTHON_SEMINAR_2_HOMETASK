from decimal import Decimal

a = Decimal(input("Введите вещественное число: "))

while (a % 1 != 0):
    a *= 10

result = 0

while (a//10 > 0):
    result += a % 10
    a //= 10
else:
    result += a

print(f"Сумма всех цифр введенного числа равна: {round(result)}")


# # АЛЬТЕРНАТИВНАЯ ВЕРСИЯ ПРОГРАММЫ (через строки):

# initial_number = input("Введите вещественное число: ")
# left = initial_number.split('.')[0]
# right = initial_number.split('.')[1]

# sum = int(left) + int(right)

# result = 0

# while (sum//10 > 0):
#     result += sum % 10
#     sum //= 10
# else:
#     result += sum

# print(f"Сумма цифр введенного числа равна: {result}")