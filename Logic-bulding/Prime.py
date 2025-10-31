def isprime(n):
    if n==2:
        return True
    elif n%2==0:
        return False
        
    else:
        for num in range(2,(n+1)//2):
            if n % num ==0:
                return False
        return True
n = 11
print(isprime(n))