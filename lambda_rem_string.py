a=input("enter a list of strings:")
l=list(filter(lambda x:len(x)>5,a.split()))
print(l)
