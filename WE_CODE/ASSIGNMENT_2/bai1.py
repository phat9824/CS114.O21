import math
import sys
import copy
r, c = list(map(int,sys.stdin.readline().strip().split()))
arr = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(r)]

i = 0
n = min(r,c)
while True:
    vong = []
    if (c - i - 1 == i):
        for j in range(i,r-i):
            vong.append(arr[j][i])
    elif (i == r - i - 1):
        for j in range(i,c-i):
            vong.append(arr[i][j])
    else:
        for j in range(i,c - i):
            vong.append(arr[i][j])
        for j in range(i + 1, r - i - 1):
            vong.append(arr[j][c-i-1])
        for j in range(c - i - 1, i, -1):
            vong.append(arr[r - i - 1][j])
        for j in range(r - i - 1, i, -1):
            vong.append(arr[j][i])

    if i % 2 == 0:
        vong.insert(0, vong.pop())
    else:
        vong.append(vong.pop(0))

    if (c - i - 1 == i):
        for j in range(r-i-1,i-1,-1):
            arr[j][i] = vong.pop()
    elif (i == r - i - 1):
        for j in range(c-i-1,i-1,-1):
            arr[i][j] = vong.pop()
    else:
        for j in range(i + 1 , r - i - 1):
            arr[j][i] = vong.pop()

        for j in range(i, c - i):
            arr[r - i - 1][j] = vong.pop()

        for j in range(r - i - 2, i, -1):
            arr[j][c - i - 1] = vong.pop()

        for j in range(c - i - 1, i - 1 ,-1):
            arr[i][j] = vong.pop()


    i = i + 1
    if (i >= n/2):
        break

for x in range(r):
    for y in range(c-1):
        print(arr[x][y],end=" ")
    print(arr[x][c-1])