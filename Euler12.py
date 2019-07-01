
def num_factors(n):
    num = n
    answer = 2
    i = 2
    temp = 0
    while not num%i:
        num //= i
        temp += 1
        
    answer *= temp+1
    i = 3             
    while i < num**0.5:
        temp = 0
        while not num%i:
            num //= i
            temp += 1
        answer *= temp+1
        i += 2
        
    if not num**0.5%1:
        answer /= 2
        answer *= 3

    return answer

i = 1
answer = 0
while True:
    n = (i**2 + i)//2           
    num = num_factors(n)
    if num > 500:
        answer = n
        break
    i += 1
    
print(answer)

