import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()
count = 0
for i in range(1,n):
    if arr[i-1] < arr[i]:
        count += arr[i] - arr[i-1] -1

print(count)
