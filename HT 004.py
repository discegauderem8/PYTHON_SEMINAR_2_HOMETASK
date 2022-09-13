from random import randint

N = int(input("Введите число N: "))

my_list = []

for i in range(0, N):
    my_list.append(randint(-N, N))

print(f"Получившийся массив: {my_list}")

input_index = input("Введите через пробел индексы нужных элементов")

left = input_index.split(' ')[0]
right = input_index.split(' ')[1]

print(f"Их произведение равно: {int(left)*int(right)}")