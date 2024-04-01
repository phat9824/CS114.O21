import sys

n = int(sys.stdin.readline())
time_get_dam = list(map(float, sys.stdin.readline().strip().split()))

x = float(sys.stdin.readline())
y = float(sys.stdin.readline())
z = float(sys.stdin.readline())

total_damage = 0
time_out = []
count_quill = 0


for cur in time_get_dam:
    total_damage += x
    time_out.append(float(cur + z))
    
    # remove that quills run out of time
    if count_quill > 0:
        while count_quill > 0 and time_out[0] < cur:
            time_out.pop(0)
            count_quill -= 1

    total_damage += y * count_quill
    count_quill += 1
    #print(total_damage,count_quill)


print(int(total_damage))
