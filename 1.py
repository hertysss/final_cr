import sys

#QWERTY
#HHJGSRFESTFLJMJBLJ
#GCTREQWRFXGJVHMNLKNLKHJH
#VHMGFTRDRESESWAW

data = [i for i in sys.stdin.read().split()]

uns = data.pop(0)

for i in data:
    d = []
    s = ""
    for j in i:
         if j not in uns:
             s += j
         else:
             d.append(s)
             s = ""
    d.append(s)
    print(max(d, key=lambda x: len(x)))