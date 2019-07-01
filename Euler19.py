def isleap(year):
    if not year%100:
        if not year%400:
            return 29
        return 28
    if not year%4:
        return 29
        
    return 28


ans = 0
days = sum([31,isleap(1900),31,30,31,30,31,31,30,31,30,31])
for y in range(1, 101):
    month = 0
    for m in [0,31,isleap(1900+y),31,30,31,30,31,31,30,31,30]:
        month += m
        if not (days+1+month)%7:
            ans += 1
    days += sum([31,isleap(1900+y),31,30,31,30,31,31,30,31,30,31])

print(ans)  
