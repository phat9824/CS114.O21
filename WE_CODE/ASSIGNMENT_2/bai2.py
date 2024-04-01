import sys

a, b = list(map(int, sys.stdin.readline().strip().split()))

matrix = []

for i in range(a):
    row = list(map(int, sys.stdin.readline().strip().split()))
    matrix.append(row)



for i in range(int((a+1)/2)):
    for j in range(b):
        matrix[i][j], matrix[a-i-1][j] = matrix[a-i-1][j], matrix[i][j]

for row in matrix:
    print(" ".join(map(str, row)))