def even_num(numbers):
    for item in numbers:
        if(item==237):break
        elif not item%2:print(item)
n=input("enter a list of numbers:")
n=list(map(int,n.split()))
even_num(n)
