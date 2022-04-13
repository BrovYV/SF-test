per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input('Введите сумму вклада:' ))
for k, v in per_cent.items():
    per_cent[k] = round(v * money/100, 2)
income = list(per_cent.values())
print('Доход составит:', income)
print('Максимальный доход:', max(income))