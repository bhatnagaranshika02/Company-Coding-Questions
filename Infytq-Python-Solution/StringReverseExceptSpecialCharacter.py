import re
a=input()
b=re.findall("[a-zA-Z]",a)
b.reverse()
for i in range(len(a)):
    if a[i]=='#' or a[i] == '@':
        b.insert(i,a[i])
print(''.join(b))
