longest = 0
answer = 0
l = 0
for n in range(1000000):
    if l > longest:
        longest = l
        answer = n-1 
    l = 0
    while n > 1:
        if n%2:
            n = 3*n+1
        else:
            n = n//2
        l += 1
        
print(answer)   
