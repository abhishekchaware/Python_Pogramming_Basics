# def hepler(num,dp):
#     if (num==1) or (num==0):
#         return 1
#     if dp[num] != -1:
#         return dp[num]
#     dp[num] = num * hepler(num-1,dp)
#     return dp[num]
# def Factorial1(num):
#     dp = [-1]*(num+1)
#     return hepler(num,dp)

# def Factorial1(num):
#     dp = [-1]*(num+1)
#     def helper(num):
#         if (num==1) or (num==0):
#             return 1
#         if dp[num] != -1:
#             return dp[num]
#         dp[num] = num * helper(num-1)
#         return dp[num]
#     return helper(num=n)

'''
Factorial of a number using loop
    n! = n * (n-1) * (n-2) * ... *2*1
'''    
def Factorial1(n):
    fact = 1
    for i in range(n,0,-1):
        fact *= i
    return fact

n=int(input("enter the number here: "))
print(Factorial1(n))