num=int(input())
min=9
max=0
minc=0
maxc=0
while num:
    r=num%10
    num=num//10
    if r>max:
        max=r
        maxc=1
    elif max==r:
        maxc+=1
    if r<min:
        min=r
        minc=1
    elif r==min:
        minc+=1
print(min,max,minc,maxc)
