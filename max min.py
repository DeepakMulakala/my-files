num=int(input())
min=9
max=0
while num:
    r=num%10
    num=num//10
    if r>max:
        max=r
    elif r<min:
        min=r
print(min,max)



