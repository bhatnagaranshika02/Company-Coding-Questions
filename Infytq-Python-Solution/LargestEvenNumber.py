import re
a=input()
d= list(set(re.findall('\d',a)))
d.sort()
d.reverse()
num = int(''.join(d))
if num%2==0:
    print(num)
else:
    for i in range(len(a)-1 , 0, -1):
        if int(d[i])%2==0:
            d1 = d[i]
            d.remove(d1)
            d.insert(len(a)-1 , d1)
            even = int(''.join(d))
            print(even)
            break
    else:
        print('-1')
