def solution(x, y):
    a=set(x)
    b=set(y)
    g=list(a.symmetric_difference(b))
    return g[0]
g= [13, 5,  7, 2, 5]
m = [5, 2, 5, 13]
k=solution(g,m)
print(k)


