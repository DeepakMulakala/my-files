num=int(input())
rev=0
while num:
    r=num%10
    num=num//10
    rev=rev*10+r
x=rev
c=0
n1=0
n2=0
n3=0
ld=rev%10
while rev!=0:
    fd=rev%10
    rev=rev//10
    c+=1
temp=fd
fd=ld
ld=temp
n1=fd*(10**(c-1))+ld
n2=x-fd-(ld*(10**(c-1)))
n3=n2+n1
print(n3)

