'''
7. Find all overlapping occurrences of given substring in given string
Ex.
String = 0111
Substring = 11
Expected answer : 2
String : ANANAAAANNN
Substring: ANA
Expected answer : 2
String : ANANAAAANNN
Substring: AA
Expected answer : 3
'''
s = "ANANAAAANNN"
sb = "ANA"
def overlap_count_occ(s,sb):
    l = len(sb)
    c = 0
    i =0
    while i<len(s):
        if s[i:i+l] ==sb:
            c +=1
        i +=1
    return c 

print(overlap_count_occ(s,sb))
