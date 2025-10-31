'''
AP to print numbers between 1 to 100 which are divisible by 3, 5 and by both
( total 3 list of numbers to be printed)
'''

def divisble():
    three =[]
    five =[]
    tf =[]
    for num in range(1,101):
        if (num % 3==0):
            three.append(num)
        if (num % 5==0):
            five.append(num)
        if (num %3==0)  and(num % 5==0):
            tf.append(num)
    return three,five,tf

print(divisble())