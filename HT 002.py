N = int(input("Введите целое число: "))

for i in range (1, N+1):
    result = 1
    for j in range (1, i+1):
        result *= j
    print(f"{result}", end = ' ')
