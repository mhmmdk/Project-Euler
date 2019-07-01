def isPalindrome(n):
    return n == int(str(n)[::-1])

ans = 0
low = 99
for a in range(999, 99, -1):
    for b in range(a, low, -1):
        if  isPalindrome(a*b):
            if ans < a*b:
                ans = a*b
            low = b      # Min a and max b may exceed
            break        # max a and min b. 

print(ans)
