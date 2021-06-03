n=int(input())
temp=0
i=0
k=n
while n:
    r=n%10
    n=n//10
    i=i+pow(r,2)
    if n==0 and i>=10:
       n=i
       print(n)
       i=0
if i<10:
    print (i)
    if i==1:
        print(k,"is a happy number")
    else:
        print(k,"is not a happy number")
