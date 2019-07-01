n = 600851475143
num = n
i = 2
while not num%i:
    num //= i

i = 3             
while i <= num**0.5:
    while not num%i:
        num //= i
    i += 2

if num ==  n:
  print("No Factor!")
else:
  print(num)  
