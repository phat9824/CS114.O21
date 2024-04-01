import sys

n = int(sys.stdin.readline())
ln = dict()
s = ""
c = 0
while True:
    inp = sys.stdin.read(44444)
    if inp == "":
        break
    s = s + inp
    t = s.split()
    for x in t[:-1]:
        if c < n:
            ln[x] = c
            c += 1
        elif c > n:
            print(ln.get(x, -1))
        else:
            c += 1
    s = "" + t[-1]
    if inp[-1] == " ":
        s = s + " "
print(ln.get(str(int(s)), -1))