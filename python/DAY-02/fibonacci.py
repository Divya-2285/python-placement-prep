a=int(input('enter a length:'))
first=0
second=1
while a>0:
    next=first+second
    print(first)
    first=second
    second=next
    a=a-1
