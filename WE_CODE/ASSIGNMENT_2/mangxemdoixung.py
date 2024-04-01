import sys

n = int(sys.stdin.readline())
a = [sys.stdin.readline().strip() for _ in range(n)]

dem = 0
for i in range(int((n+1)/2)):
    if a[i] != a[n-i-1]:
        dem+=1
    
    if dem > 1:
        break
if(dem <= 1):
    print("TRUE")
else:
    print("FALSE")