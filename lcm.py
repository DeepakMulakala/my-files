a,b=map(int,input().split())
c=2
d=1
while c<=a and c<=b:
      if a%c==0 and b%c==0:
          a=a//c
          b=b//c
          d=d*c
      else:
          c+=1
d=d*a*b
print(d)
