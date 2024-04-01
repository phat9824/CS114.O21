import sys

n = int(sys.stdin.readline().strip())
ln = list(map(int, sys.stdin.readline().strip().split()))
lk = []
lx = []
while True:
    inp = sys.stdin.readline().strip()
    if inp == "":
        break
    k, x = list(map(int, inp.split()))
    lk.append(k)
    lx.append(x)

for k, x in zip(lk, lx):
    if 2*k < len(ln):
        if x > ln[len(ln) - k]:
            left = len(ln) - 2*k
            right = len(ln) - k
            while left < right:
                mid = (left + right) // 2
                if x - ln[mid] <= ln[mid + k] - x:
                    right = mid
                else:
                    left = mid + 1
            print(ln[left], end=" ")
            print(ln[left + k - 1])
        elif x < ln[2*k]:
            left = 0
            right = 2*k
            while left < right:
                mid = (left + right) // 2
                if x - ln[mid] <= ln[mid + k] - x:
                    right = mid
                else:
                    left = mid + 1
            print(ln[left], end=" ")
            print(ln[left + k - 1])
        else:
            left = 0
            right = len(ln) - k
            while left < right:
                mid = (left + right) // 2
                if x - ln[mid] <= ln[mid + k] - x:
                    right = mid
                else:
                    left = mid + 1
            print(ln[left], end=" ")
            print(ln[left + k - 1])
    else:
        left = 0
        right = len(ln) - k
        while left < right:
            mid = (left + right) // 2
            if x - ln[mid] <= ln[mid + k] - x:
                right = mid
            else:
                left = mid + 1
        print(ln[left], end=" ")
        print(ln[left + k - 1])