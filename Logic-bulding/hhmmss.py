'''
WAP to convert input number of seconds to HH:MM:SS.
'''
def sec_to_hms(n):
    hours = n //3600
    rem = n % 3600
    minutes= rem //60
    rem = rem % 60
    seconds= rem
    return [hours ," hh ", minutes, " mm ", seconds ," ss"] 

n = int(input("enter the number: "))
print(sec_to_hms(n))    