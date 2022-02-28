print('Задача 10. Максимальное число (по желанию)')

# Пользователь вводит три числа.
# Напишите программу,
# которая выводит на экран максимальное из этих трёх чисел (все числа разные).
# Можно использовать дополнительные переменные, если нужно 
print('Вариант 0 - в рамках темы')
numbers1 = int(input('Введите первое число: '))
numbers2 = int(input('Введите второе число: '))
numbers3 = int(input('Введите третье число: '))
if numbers1 > numbers2:
    max_numbers = numbers1
else:
    max_numbers = numbersbers2
if max_numbers < numbersbers3:
    max_numbers = numbersbers3
print('Максимальное число:', max_numbersb)

print('Вариант 1 - за рамками темы')
numbers1 = int(input('Введите первое число: '))
numbers2 = int(input('Введите второе число: '))
numbers3 = int(input('Введите третье число: '))
if numbers1 > numbers2:
    if numbers1 > numbers3:
        print('Максимальное число:', numbers1)
    else:
        print('Максимальное число:', numbers3)
else:
    if numbers2 > numbers3:
        print('Максимальное число:', numbers2)
    else:
        print('Максимальное число:', numbers3)


print('Вариант 2 - за рамками темы')
numbers1 = int(input('Введите первое число: '))
numbers2 = int(input('Введите второе число: '))
numbers3 = int(input('Введите третье число: '))
if numbers1 > numbers2 and numbers1 > numbers3:
    print('Максимальное число:', numbers1)
elif numbers2 > numbers1 and numbers2 > numbers3:
    print('Максимальное число:', numbers2)
else:
    print('Максимальное число:', numbers3)


print('Вариант 3 - за рамками темы')
numbers1 = int(input('Введите первое число: '))
numbers2 = int(input('Введите второе число: '))
numbers3 = int(input('Введите третье число: '))
if numbers1 < numbers2 > numbers3:
    print ('Максимальное число:', numbers2)
elif numbers2 < numbers3 > numbers1:
    print('Максимальное число:', numbers3)
else:
    print('Максимальное число:', numbers1)