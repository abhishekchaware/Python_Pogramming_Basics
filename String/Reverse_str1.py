s = int(input("Enter the word to do reverse: "))
print(s)
def rev_str(n:int)-> bool:
    rev = int(str(n)[::-1])
    print(n)
    if n == rev:
        return True
    return False
print(rev_str(s))