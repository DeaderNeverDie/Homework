numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
lenght = len(numbers)
for i in range(2, lenght + 1):
    for x in range(2, i):
        if i % x == 0:
            primes.append(i)
            break
    else:
        not_primes.append(i)
print(primes)
print(not_primes)