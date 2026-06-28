a=int(input('enter a number:'))
temp=a
arm=0
while a>0:
    b=a%10
    arm=arm+(b**3)
    a=a//10
print(arm)
if temp==arm:
    print('armstrong')
else:
    print('not armstrong')
