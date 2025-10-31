strs= ["flower","flow","flight"]
def lst_com_prefix(strs):
    if not  strs:
        return ""
    l = len(strs[0])
    for i in range(l):
        char = strs[0][i]
        for word in strs:
            if i==len(word) or word[i] != char:
                return strs[0][:i]
    return strs[0]
    
print(lst_com_prefix(strs))

s1 =["abhi","abh","ab","abhishek"]
# vertical scanning in for loop
def longestcommonsuffix(s):
    curr = s[0]
    l = len(curr)
    rem = s[1:]
    for i in range(l):
        char = curr[i]
        for word in rem:
            if i==len(word) or char !=word[i]:
                return curr[:i]
    return curr
    
print(longestcommonsuffix(s1))