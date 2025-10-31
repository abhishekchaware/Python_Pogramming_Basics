'''
12. You are given a string S and width w.
Your task is to wrap the string into a paragraph of width w
Example .
String : “ABCDEFGHIJKLIMNOQRSTUVWXYZ”
Width: 4
Output:
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
'''
str1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
w = int(input("enter width: "))
l = len(str1)
for i in range(0,l,w):
    print(str1[i:i+w])