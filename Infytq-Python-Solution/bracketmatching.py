def bracket(s):
    stack=[]
    count=0
    for i in s:
        if i=='[' or i=='{' or i=='(':
            stack.append(i)
            count+=1
            continue
        if len(stack) == 0:
            return count+1
        x=stack.pop()
        if i==']' and x=='[':
            count+=1
        elif i=='}' and x=='{':
            count+=1
        elif i==')' and x=='(':
            count+=1
            
if __name__ == "__main__":
    for _ in range(int(input())):
        a=input()
        print(bracket(a))
