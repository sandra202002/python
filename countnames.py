names=input('ENTER THE NAMES SEPERATED WITH COMMA:')
n=names.split(",")
c=0
for names in n:
    if(names[0]=='A'):
        c=c+1
print(c)

