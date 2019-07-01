total = 0
f = 1
even_f = 2
while even_f < 4000001:
    total += even_f
    next_f = f + even_f
    f = next_f + even_f
    even_f = next_f + f

print(total)
