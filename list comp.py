"""r=[]
x = int(input())
y = int(input())
z = int(input())
n = int(input())
for i in range(0,x):
    for j in range(0,y):
        for k in range(0,z):
            r.append([i,j,k])
print(r)"""


if __name__ == '__main__':
    r=[]
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    result = [[i, j, k]
    for i in range(x+1)
    for j in range(y+1)
    for k in range(z+1)
    if (i + j + k) != n
    ]
    print(result)