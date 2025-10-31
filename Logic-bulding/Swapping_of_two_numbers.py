'''
Write a  program to swap two variables
a. by using a temporary variable
b. using arithmatic operation and not using a variable
c. without using variable ( using python unpacking syntax)
'''
def swap1(a,b):
    c = a
    a = b
    b = c
    return a, b
a = 10
b = 20
print(swap1(a,b))

def swap2(a,b):
    a = a^b
    b = a^b
    a = a^b
    return a,b
print(swap2(a,b))

def swap3(a,b):
    a = a +b 
    b = a -b
    a = a -b
    return a ,b
print(swap3(a,b))

def swap4(a,b):
    a ,b = b,a
    return a ,b
print(swap4(a,b))