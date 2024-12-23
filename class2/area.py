import math
try:
    radius = int(input('Write the radius of circle'))
    area =math.pi*(radius**2)
    print(f'The area is {area}')
except:
    print('only interger pls')