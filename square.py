num=input("enter the numbers")
list_num=num.split(',')
print("the list off numbers:",list_num)
result=[int(num)*int(num) for num in list_num]
print("the square of numbers:",result)
