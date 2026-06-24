num=int(input('enter the number:'))
temp=num
pal=0
while temp>0:
    a=temp%10
    pal=pal*10+a
    temp=temp//10

if num==pal:
    print('palindrome')
else:
    print('not palindrome')
