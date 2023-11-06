n=[908,6345,8909,12,567,38]
l=list(map(lambda x:x+x*0.1 if x>1000 else x+x*0.05,n))
print(l)
