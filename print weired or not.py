n=int(input("no"))
x=n%2
if x==0:
    if n>2 and n<5.5:
        print("Not Weird")
    elif n>5.5 and n<20.5:
        print("Weird")
    elif n>20.5:
        print("Not Weird")
else:
    print("Weird")
