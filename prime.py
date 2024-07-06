num=int(input("Enter number"))
if(num==1):
    print("Not prime")
if(num==2):
    print("Prime")
for i in range (2 ,num):
    if (num%i==0):
        print("Not Prime")
        break
    else:
        print("Prime")