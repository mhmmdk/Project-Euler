n = 3
primes = []
total = 2
while n < 2000000:
    isPrime = True
    sqrt_n = n**0.5
    for p in primes:
        if p > sqrt_n:
            break
        if not n%p:
            isPrime = False
            break

    if isPrime:
        primes += [n]
        total += n
    n += 2

print(total)
