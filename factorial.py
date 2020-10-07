def fact(num):
    result=1
    for i in range(1,num):
        result=result*num  
        num=num-1
    print(result)
b=int(input("enter"))
fact(b)




def c(n):
    if n==1:
        return 1
    else: 
        return n * c(n-1)
print(c(5))