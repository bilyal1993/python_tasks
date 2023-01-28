import math
print('Введите коэффициент а:')
a=int(input())
print('Введите коэффициент b:')
b=int(input())
print('Введите коэффициент c:')
c=int(input())
print('Решаем уравнение^ ', a,'x^2+',b,'x+',c,'=0')
D=b*b-4*a*c
if D<0: print('Корней нет')
if D==0: print('Один корень')
if D>0: print('Два корня')

if D>0: 
    x1= ((-b)+ math.sqrt(D))/(2*a)
    x2= ((-b)- math.sqrt(D))/(2*a)
    print('x1=',x1,' x2=',x2)
elif D==0:
    x=(-b)/(2*a)
    print('x=',x)
