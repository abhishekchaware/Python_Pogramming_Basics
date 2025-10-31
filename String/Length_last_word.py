# s = "   fly me   to   the moon  "
# l3 = s.strip()
# l = list(l3.split(" "))
# l2 = len(l[-1])
# print(l2)

l =[4,3,2,9]
# n = l[-1]+1
# l[-1] = n
# if l[-1] != 9:
#     l[-1]+1
# else:
#     l2 =l[:-1]
#     l2.append()
s1 = ["a","c","d"]
s = "".join(s1)
print("s :", s)

n= int("".join(map(str,l)))+1
# l2 = list(map(int,str(n)))
# print(l2)

d =[]
while n>0:
    d.append(n %10)
    n //=10
d.reverse()
print(d)

n1 = 10
rem = 0
while n1 >7:
    rem += n1%7
    n1= n1//7
    q =n1
print(rem)
print(q)

    
    