import sys
import bisect

my_list = []

def BinarySearch(a, x):
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i + 1
    else:
        return 0

while True:
    line = sys.stdin.readline().strip()
    if line == "0":
        break
    values = line.split()
    a, b = map(int, values)
    if a == 1:
        if BinarySearch(my_list, b) == 0:
            bisect.insort(my_list, b)
    else:
        index = BinarySearch(my_list, b) 
        print(index)
