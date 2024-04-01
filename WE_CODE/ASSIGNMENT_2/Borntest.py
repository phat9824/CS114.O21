import random
n, m = 3,random.randint(1,10)
k = 1
a = []
for i in range(n):
    temp = []
    for j in range(m):
        temp.append(k)
        k += 1
    a.append(temp)

print(n,end = " ")
print(m)
for x in range(n):
        for y in range(m-1):
            print(a[x][y], end=" ")
        print(a[x][m - 1])