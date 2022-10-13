import random
pile = 2
count = random.randint(4,30)
print('Количество камней',count)
while count >= 0:
    if count == 0:
        break
    else:
        if (count!= 0):
            digit = random.randint(1, 3)
            if pile == 2:
                count_pile = count
                count -= digit
            if count <= 0:
                print('Компьютер забрал', count, 'камней. Осталось',
                      '0')
                print('Компьютер победил!')
                break
            else:
                print('Компьютер забрал', digit, 'камней. ',
                      'Осталось', count)
                takes = int(input('Выберите кол-во камней: '))
                your_pile = 1
                if your_pile == 1:
                    count -= takes
                    print('Вы забрали', takes, 'камней ',
                          'Осталось', count, )
                if count <= 0 :
                    print('Вы забрали', takes, 'камней. Осталось',
                          '0', '0')
                    print('Вы победили!')
                    break