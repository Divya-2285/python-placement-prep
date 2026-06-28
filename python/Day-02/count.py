a=int(input('enter a number:'))
count=0
if a == 0:
    print("The number of digits are: 1")
else:
    while a>0:
        count=count+1
        a=a//10
    print('the number of digits are:',count)
