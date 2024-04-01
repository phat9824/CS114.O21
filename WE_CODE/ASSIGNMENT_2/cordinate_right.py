import sys
#Có tham khảo hàm calcDir có lấy từ stack overflow 'https://stackoverflow.com/questions/27635188/algorithm-to-detect-left-or-right-turn-from-x-y-co-ordinates'
def calcDir(p0, p1, p2):
    v1x = (p1[0]) - (p0[0])
    v1y = (p1[1]) - (p0[1])
    v2x = (p2[0]) - (p1[0])
    v2y = (p2[1]) - (p1[1])
    if v1x * v2y - v1y * v2x > 0.0:
        return 0 #'Left'
    else:
        return 1 #'Right'

n = int(sys.stdin.readline())

point1 = list(map(int, sys.stdin.readline().split()))
point2 = list(map(int, sys.stdin.readline().split()))
count = 0


def vector(p0,p1):
    p = [0]*2
    p[0] = p1[0] - p0[0]
    p[1] = p1[1] - p0[1]
    return p
for i in range(2,n):
    point = []
    point = list(map(int, sys.stdin.readline().strip().split()))
    if calcDir(point1, point2, point) == 1:
        vector_old = vector(point1,point2)
        vector_new = vector(point2,point)
        if vector_new[0] != vector_old[0] and vector_new[1] != vector_old[1]:
            if(vector_new[0]*(-1) != vector_old[0] and  vector_new[1]*(-1)!=vector_old[1]):
                count = count + 1
                #print(point)

    point1 = point2
    point2 = point
    
print(count)
