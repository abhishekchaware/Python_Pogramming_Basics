'''
WAP that accepts three integers from the user and return true if two or more of them have 
the same rightmost digit. The integers are non-negative
'''
num1 = input('enter the number1: ')
num2 = input('enter the number2: ')
num3 = input('enter the number3: ')
def is_ldgt_same(num1,num2,num3):
    l1=num1[-1]
    l2 =num2[-1]
    l3 = num3[-1]
    if (l1 ==l2) or (l2==l3)or (l1 == l3):
        return True
    return False
    
print(is_ldgt_same(num1,num2,num3))