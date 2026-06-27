a=int(input('enter a number: '))
if a<2:
     print('not prime')
else:
     
    for i in range(2,a):
        if a%i == 0:
            print('not prime')
            break
    else:
        print('prime')
