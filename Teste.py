print('vini-san world')
x=1
while x <= 50:
    print("*" * x)
    x+=1
while x >= 0:
    print("*" * x)
    x-=1
y = 50
while x <= 50:
    print(" " * y +"*" * x + " " * y)
    x+=1
    y-=1
#xeredelda
x=1
y=50
while x <= 50:
    yy = int(y/2)
    print("-" * yy + "*" * x + "-" * yy)
    x+=2
    y-=2
    