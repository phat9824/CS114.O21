import sys

a, b = list(map(int, sys.stdin.readline().strip().split()))

matrix = []

for i in range(a):
    row = list(map(int, sys.stdin.readline().strip().split()))
    matrix.append(row)

count = 0
for i in range(a):
    for j in range(b):
        if matrix[i][j] == 1:
            #TH 1
            if j - 1 >= 0:
                if matrix[i][j-1] == 0:
                    count = count + 1
            else:
                count = count + 1

            #TH 2
            if i - 1 >= 0:
                if matrix[i-1][j] == 0:
                    count = count + 1
            else:
                count = count + 1
            
            #TH 3
            if i + 1 < a:
                if matrix[i+1][j] == 0:
                    count = count + 1
            else:
                count = count + 1

            #TH 4
            if j + 1 < b:
                if matrix[i][j+1] == 0:
                    count = count + 1
            else:
                count = count + 1

            print(i,j,count)
        
print(count)