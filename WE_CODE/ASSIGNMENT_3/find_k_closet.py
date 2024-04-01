import sys

def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return left

def find_closest_numbers(arr, k, x):
    n = len(arr)

    index = binary_search(arr, x)

    left, right = index - 1, index
    while k > 0 and left >= 0 and right < n:
        if abs(arr[left] - x) <= abs(arr[right] - x):
            left -= 1
        else:
            right += 1
        k -= 1

    while k > 0 and left >= 0:
        left -= 1
        k -= 1

    while k > 0 and right < n:
        right += 1
        k -= 1

    sys.stdout.write(' '.join(map(str, arr[left + 1:right])))

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
k, x = map(int, sys.stdin.readline().split())

find_closest_numbers(arr, k, x)
