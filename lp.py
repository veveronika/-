m=float(input('Введите массу тела: '))
h=float(input('Введите рост: '))
i=0
i= m/(h*h)
if i>= 18.5 and i<=25:
    print('Индекс массы тела в норме: ', i)
else:
    print('Индекс массы тела не в норме: ', i)