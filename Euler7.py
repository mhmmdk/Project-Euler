n = 29
counter = 0
primes = [7,11,13,17,19,23,29]
while counter < 9998:
    for i in [2,6,4,2,4,2,4,6]:
        n += i
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
            counter += 1


print(primes[9997])
