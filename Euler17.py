tens = [6,6,5,5,5,7,6,6]                 
AND = 3
ten = 3
hundred = 7
thousand = 8


_1_9 = [3,3,5,4,4,3,5,5,4]            
_11_19 = [6,6,8,8,7,7,9,8,8]                    
_20_99 = []
_100_999 = []

#21_99
for i in tens:
    _20_99 += [i]
    for j in _1_9:
        _20_99 += [i+j]
        
#100_999
for i in _1_9:
    _100_999 += [i+hundred]
    for j in _1_9:
        _100_999 += [i+hundred+AND+j]
    _100_999 += [i+hundred+AND+ten]
    for j in _11_19:
        _100_999 += [i+hundred+AND+j]
    for j in _20_99:
        _100_999 += [i+hundred+AND+j]

answer = 0
for i in _1_9:
    answer += i
answer += ten
for i in _11_19:
    answer += i
for i in _20_99:
    answer += i
for i in _100_999:
    answer += i

print(answer + 3 + thousand)  
