'''

Write a  program that takes three numbers as input then print 
maximum and minimum number of the three
'''
def max_3n(n1,n2,n3):
    if n1>n2>n3:
        return n1
    elif n2>n3>n1:
        return n2
    else:
        return n3
    
def min_3n(n1,n2,n3):
    if n1<n2<n3:
        return n1
    elif n2<n3<n1:
        return n2
    else:
        return n3
    
n1 = int(input('enter the number1: '))
n2 = int(input("enter number2: "))
n3 = int(input("enter the number 3 : "))
print("minimum : ",min_3n(n1,n2,n3))
print("maximum : ",max_3n(n1,n2,n3))