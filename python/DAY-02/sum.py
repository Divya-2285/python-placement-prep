temp=int(input('enter a number:'))
sum=0
while temp>0:
    b=temp%10
    sum=sum+b
    temp=temp//10
print(sum)
