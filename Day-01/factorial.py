num=int(input('enter the number:'))
n=num
fact=1
while num>0:
    fact=fact*num
    num=num-1

print('factorial of ',n,'is',fact)
