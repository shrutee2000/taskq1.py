n1=int(input("enter start no"))
n2=int(input("enter stop no"))
n3=int(input("enter random no"))
c1=0
c=0
i=1
j=1
while n1<=n2:
    while i<=n1:
        if(n1%i==0):
            c=c+1
            i=i+1
    if(c==2):
        print(n1)
     n1=n1+1
while j<=n3:
    if(n3%j==0):
        c1=c1+1
        j=j+1
if(c1==2):
    print(f"prime no{n3}")
else:
    print(f"composite no{n3}")
