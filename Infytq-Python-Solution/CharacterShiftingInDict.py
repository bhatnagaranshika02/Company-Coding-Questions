dic = dict(input().split(','))
for i in dic:
    s= i.split(':')
    string = s[0]
    number = s[1]
    summ=0
    for j in number:
        summ+=(int(digit)**2)
    if (summ%2==0):
        s = string[len(string) : len(string)]
        print(s+string[0:len(string)-2],end=' ')
    else:
        s=string[0]
        print(string[1:len(string)]+s,end=' ')
