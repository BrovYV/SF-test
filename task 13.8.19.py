quant = int(input('Введите количество билетов: '))
age = [int(input('Введите возраст посетителя: ')) for i in range(quant)]
price = 0
for i in age:
    if 18 <= i < 25:
        price += 990
    elif i >= 25:
        price += 1390
    else:
        price += 0
if quant > 3:
    price -= price * 10 / 100
    print(price)
else:
    print(price)

