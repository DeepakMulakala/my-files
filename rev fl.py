num=int(input())
x=num
c=0
n1=0
n2=0
n3=0
ld=num%10
while num!=0:
    fd=num%10
    num=num//10
    c+=1
temp=fd
fd=ld
ld=temp
n1=fd*(10**(c-1))+ld
n2=x-fd-(ld*(10**(c-1)))
n3=n2+n1
print(n3)


