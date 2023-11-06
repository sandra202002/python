n=int(input("enter the year:"))
result=[i for i in range(2023,n) if(i%400==0 or(i%100!=0 and i%4==0))]
print("leap year:",result)


