a=input()
start=0
l=[]
l2=[]
for i in range(start-1,len(a)):
    if a[i] not in l:
        l.append(a[i])
        
    else:
        l2.append(l)
        l=[]
        start = i
maxx = 0
for j in range(len(l2)):
    if maxx<len(l2[j]):
        maxx = len(l2[j])
print(*l2[j],sep='')    
