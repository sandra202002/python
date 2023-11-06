word=input("enter a word:")
l=list(word)
result=[i for i in l if i.lower()=='a' or i.lower()=='e' or i.lower()=='i' or i.lower()=='o' or i.lower()=='u']
print("given word is:",l)
print("list of vowels are:",result)
