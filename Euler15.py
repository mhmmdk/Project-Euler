n = 20
li = []
temp = []
for i in range(n):
    temp += [1]
    
li += [temp]
for j in range(n-1):
    temp = []
    for i in range(n, 0, -1):
        temp += [sum(li[j][:i])]
    temp.reverse()
    li += [temp]

tot = 0
for i in range(n):
    tot += sum(li[i])
    
print(tot + 1)
