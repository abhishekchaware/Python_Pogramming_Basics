def Fibo(num):
    dp =[-1]*(num+1)
    def hepler(num):
        if (num==1) or (num ==0):
            return num
        if dp[num] !=-1:
            return dp[num]
        dp[num] = hepler(num -1) + hepler(num-2)
        return dp[num]
    return hepler(num)
num =10
print(Fibo(num))
for i in range(num):
    print(Fibo(i),end=" ")
    
print()
num1 = 0
num2 = 1

for i in range(num):
    print(num1,end=" ")
    #num1,num2 = num2,num2+num1
    res = num1
    num1 =num2
    num2 = res+num1
    
