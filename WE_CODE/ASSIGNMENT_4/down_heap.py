import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
nums = []
for i in range(n):
    tmp = int(sys.stdin.readline())
    nums.append(-tmp)


# Convert the elements to negative before heapifying
heapq.heapify(nums)

for i in range(m):
    tmp = sys.stdin.readline().strip()
    #case :-1
    if tmp == "-1":
        heapq.heappop(nums)

    #case :-2
    elif tmp == "-2":
        max_num = heapq.heappop(nums)
        if nums:
            while nums[0] == max_num:
                heapq.heappop(nums)
                if not nums:
                    break
        else:
            break
    
    else:
        tmp1, tmp2 = map(int, tmp.split())
        max_num = nums[0]
        #case :-3
        if tmp1 == -3:
            heapq.heappop(nums)
            heapq.heappush(nums, max_num + tmp2)
        #case :-4
        else:
            while nums[0] == max_num:
                heapq.heappop(nums)
                heapq.heappush(nums, max_num + tmp2)
                if not nums:
                    break
    if not nums:
                break

# Pop and print elements in the original order
while nums:
    print(-heapq.heappop(nums))