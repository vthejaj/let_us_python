# store functions in a list and call them in loop

def fun():
    print('In fun')

def disp():
    print('In disp')

def msg():
    print('In msg')

lst = [fun,disp,msg]

for f in lst:
    f()
