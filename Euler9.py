def tri(num):
    for m in range(num):
        for n in range(1,m):
            a = m**2-n**2
            b = 2*m*n
            c = m**2+n**2
            tot = a + b + c
            if not num%tot:
                return (num // tot)**3 * (a * b * c)

print(tri(1000))
