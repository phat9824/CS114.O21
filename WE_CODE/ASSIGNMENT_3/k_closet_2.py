import sys
import math


def find_closest_numbers(arr, n, k, x):
    l, r = 0, n - k

    while l < r:
        m = (l + r) // 2
        if x - arr[m] > arr[m + k] - x:
            l = m + 1
        else:
            r = m

    sys.stdout.write("{} {}\n".format(arr[l], arr[r + k - 1]))


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

while True:
    input_str = sys.stdin.readline().strip()
    if not input_str:
        break

    k, x = map(int, input_str.split())

    find_closest_numbers(arr, n, k, x)
