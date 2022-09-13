import random
from random import randint

my_list = []

for i in range(0, 7):
    my_list.append(randint(-10, 10))

print(my_list)

random.shuffle(my_list)

print(my_list)



# АЛЬТЕРНАТИВНАЯ ВЕРСИЯ КОДА (иногда меняет местами только два элемента, но не менее двух будет поменяно местами, так как нечетное число шагов):

# from random import randint

# my_list = []

# for i in range(0, 7):
#     my_list.append(randint(-10, 10))

# print(my_list)

# for i in range (0, randint(29, 90)):
#     randomizer = randint(0,2)
#     left = my_list[randomizer]
#     right = my_list[randomizer+3]

#     save = left
#     my_list[randomizer] = right
#     my_list[randomizer+3] = save

# print(my_list)

