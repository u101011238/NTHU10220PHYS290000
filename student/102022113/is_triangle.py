x=float(raw_input('The length of the first sticks is '))
y=float(raw_input('The length of the second sticks is '))
z=float(raw_input('The length of the third sticks is '))

if x<=0 or y<=0 or z<=0:
    print 'All the lengths have to be positive.'
else:
    def is_triangle(x,y,z):
        if x+y>z and y+z>x and z+x>y:
            print 'Yes'
        else:
            print 'No'
    is_triangle(int(x),int(y),int(z))
