a=input()

l=[]
for i in range(1,len(a),2):
    o=int(a[i])**2
    l.append(o)
print(*l[:3],sep='')
    
