
password = input('Введите пароль: ')

try:
    result = 1/len(password)
    try:
        result = int(password)
        print('Ваш пароль состоит только из цифр')
    except ValueError:
        print('Требования к паролю соблюдены')
except ZeroDivisionError:
    print('Вы ввели пустой пароль')