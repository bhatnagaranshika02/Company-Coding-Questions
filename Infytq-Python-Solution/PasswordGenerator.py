d = input().split(',')
s=[]
for i in d:
    temp = i.split(':')
    name = temp[0]
    numbers = temp[1]
    maxx = 0
    for j in numbers:
        if int(j) <=len(name):
            if int(j) > maxx:
                maxx= int(j)
    if maxx ==0:
        s.append('X')
    else:
        o=name[maxx - 1]
        s.append(o)
print(*s,sep='')
