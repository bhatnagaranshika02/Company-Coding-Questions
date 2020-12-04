a=input()
for i in range(len(a)//2 , 0 ,-1):
    p = a[0:i]
    s = a[len(a) -i : len(a)]
    if p == s:
        print(len(p))
        break
