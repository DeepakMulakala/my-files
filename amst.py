n=int(input("enter the number "))
temp=n
i=0
while n!=0:
    r=n%10
    n=n//10
    i=i+pow(r,3)
if temp==i:
        print("armstrong number")
else:
        print("not a armstrong number")
