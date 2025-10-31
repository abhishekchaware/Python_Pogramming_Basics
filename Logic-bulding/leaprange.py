'''
WAP to print all leap years between 2000 to 2100. 
Apply all conditions of checking leap year 
( (divisible by 4 and not divisible by 100) OR (divisible by 400))

'''
for year in range(2000,2011):
    if (year % 4 ==0) and(year % 100 !=0) or (year % 400 ==0):
        print(year)
    