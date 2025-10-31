'''
Armstrong Number.
    It is a number with 'n' digits. Here (sum of every digit ^ n) equal to ( number itself)

    1) 1^3+5^3+3^3=153 ( here number of digits(n) is 3)
    2) 1^1 = 1 ( here number of digits is 1)
    3) 1634 = 1^4 + 6^4 + 3^4 + 4^4 ( here number of digits is 4)
'''
def Armstrong(n):
    l =len(str(n))
    og =n
    summ = 0
    for _ in range(l):
        rem = n%10
        n //=10
        summ +=rem**l
    if summ==og:
        return "it is ArmStrong number" 
    return "Not an Armstrong number"

n =153
print(Armstrong(n))
n1=153
if n==n1:
    print("same")
