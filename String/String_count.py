'''
11. Given a paragraph count number of words, sentences. Every sentence ends with either . or ? or !
Print Count of how many normal sentences ending with . , how many interrogative sentences ( ending
with ?) and how many exclamatory sentences ( ending with !).
Ex.
Input : “I am at CDAC. What about you? I am surprised by current weather!”
Normal sentence : 1
Interrogative: 1
Exclamatory : 1

'''
inp = "I am at CDAC. What about you? I am surprised by current weather!"
n = inp.count(".")
i = inp.count("?")
e = inp.count("!")
print("Normal sentence : ",n )
print("Interrogative: ",i)
print("Exclamatory : ",e)