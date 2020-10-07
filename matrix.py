list=[]
a=int(input("enter row "))
b=int(input("enter coloum"))
for i in range (a):
    row=[]
    for j in range(b):
        elem=int(input("value"))
        row.append(elem)
    list.append(row)
print("2d array")
for i in range(a):
    for j in range(b):  
        print(list[i][j],end="  ")
    print("\n")     
print("leading")
for i in range(a):
    for j in range(b):
        if i>j:
            print(list[i][j],end=" ")






