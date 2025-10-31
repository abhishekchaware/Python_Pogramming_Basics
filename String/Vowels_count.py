vowels = ['a','e','i','o','u','A','E','I','O','U']
word = input("Enter the word: ")
count=0
for char in word:
    if char in vowels:
        count +=1
print(f"vowels in words are: {count}")