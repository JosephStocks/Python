number = int(input("Number? "))
factors = []
for divisor in range(1, number + 1):
    if number % divisor == 0:
        factors.append(divisor)

print(factors)