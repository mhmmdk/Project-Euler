n = 20
found = 0
while not found:
    for i in (16,9,5,7,11,13,17,19):
        if n%i:
            break
        found = i//20
    n += 1

print(n-1)
