numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
i = 0
for i in range(len(numbers)):
    is_prime = True
    n = numbers[i]
    if n < 2:
        continue
    else:
        l = n ** (1 / 2)
    for j in range(2, int( l + 1)):
            if n % j == 0:
                is_prime = False
                break
    if not (is_prime):
          not_primes.append(n)
    else:
          primes.append(n)
is_prime = True
print(primes)
print(not_primes)








