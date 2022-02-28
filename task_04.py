print('Задача 4. Калькулятор скидки')

# Андрей переехал на новую квартиру, и ему нужно купить три стула в разные комнаты.
# Естественно, цена на стулья в разных магазинах различается,
# а где-то ещё и скидка есть. 
# Вот для одного из таких магазинов он и написал калькулятор скидки, 
# чтобы проще ориентироваться в ценах.
 
# Напишите программу,
# которая запрашивает три стоимости товара и вычисляет сумму чека. 
# Если сумма чека превышает 10 000 рублей,
# то нужно вычесть из этой суммы скидку 10% (умножить на 10, разделить на 100). 
# В конце вывести итоговую сумму на экран.

stool = int(input('Введите стоимость первого стула: '))
chair = int(input('Введите стоимость второго стула: '))
throne = int(input('Введите стоимость третьего стула: '))
furniture = stool + chair + throne
if furniture <= 10000:
    print('Стоимость трёх стульев', furniture, ' рублей, скидка не применяется.')
else:
    furniture = furniture - (furniture * 10 / 100)
    print('Стоимость трёх стульев', furniture, ' рублей с 10% скидкой.')