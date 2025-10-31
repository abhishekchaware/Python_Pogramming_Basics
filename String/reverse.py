"""
name =input("Enter the name: ")

for i in range(len(name)-1,-1,-1):
    print(name[i],end=" ")
"""
## Approach 2
'''
num = int(input("enter the number: "))
def num_rev(num):
    rev =0
    tmp = num
    pw=len(str(num))-1
    while (tmp > 0):
        res = tmp % 10
        rev += res *10 **pw
        pw  -=1
        tmp = tmp //10
    return rev
print(num_rev(num=num))
'''
# Optimse approach
num = int(input("enter the number: "))
def rev_num(num):
    rev =0
    tmp = num
    while (tmp != 0):
        rem = tmp %10
        rev = rev *10 + rem
        tmp //=10
    if (-231 <= num and rev <= 231 - 1):
        if num < 1:
            return -rev
        else:
            return rev
    else: 
        return 0
            
print(rev_num(num=num))