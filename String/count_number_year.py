'''
109. Write a Python program that counts the number of leap years within the range of years. Ranges of years should be accepted as strings.
Sample Data:
("1981-1991") -> 2
("2000-2020") -> 6

'''
#s = "1981-1991"
s ="2000-2020"
def find_leap(s):
    start = int(s[:4])
    end = int(s[-4:])+1
    c =0
    for i in range(start,end):
        if (i%4==0):
            c +=1
    return c
        
print(find_leap(s))