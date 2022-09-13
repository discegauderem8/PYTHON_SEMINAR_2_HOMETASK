N = int(input("Введите число N: "))

result = 0

for i in range(1, N+1):
    result += result + (1 + 1/N)**N

print(f"{result}")


