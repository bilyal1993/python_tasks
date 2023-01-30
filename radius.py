import math
print('Введите радиус круга:')
r=int(input())
if r<=0:
    print('error')
elif r>0:    
    S=math.pi*r*r
    print('Площадь круга равна ',"%4.2f"%S)
    l=math.pi*2*r
    print('Длина окружности ',"%4.2f"%l)