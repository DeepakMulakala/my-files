num=int(input())
while num:
    r=num%10
    num=num//10
    if r==1:
        print(0)
    if r==0:
        print(1)
