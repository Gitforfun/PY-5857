a = '10'

try:
    name = input("name >>>")
    print(a + 1)
except TypeError:
    print('Это не строка!')
except:
    print('Неизвестная ошибка! ...')
finally:
    print('Сейчас программа закроется')
