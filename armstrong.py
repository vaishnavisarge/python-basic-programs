num=int(input("Enter num"))
temp=num
sum=0
while temp !=0:
    digit=temp%10
    sum=digit**3+sum
    temp=temp//10
if sum==num:
    print("Armstrong number")
else:
    print("Not Armstrong")