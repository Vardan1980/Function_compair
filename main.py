def my_function(x,y,number):
    x.extend(y)
    c=[]
    for i in x:
        if i>number:
           c.append(i)
    print(c)
my_function([-4,-8,-3,6],[2,0,-4,8],0)