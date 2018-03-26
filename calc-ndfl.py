# MSSERG | 26.03.2018
# Calculator for NDFL
print('Калькулятор для расчета налога на доходы физических лиц.')
result = 0; stavka = 0
a = int(input('Введите сумму: '))
b = int(input('1 - Обычные доходы 13%.\n3 - Дивиденды 9%.\n3 - Иностранцы 30%.\n4 - Другая ставка (ввести вручную %).\nВведите номер требуемого вычисления: '))
# NDFL 1 | 2 | 3 | 4
if b == 1:
	ndfl = a/100*13
	stavka = 13
elif b == 2:
	ndfl = a/100*9
	stavka = 9
elif b == 3:
	ndfl = a/100*30
	stavka = 30
elif b == 4:
	stavka = int(input('Введите ваше значение %: '))
	ndfl = a/100*stavka
result = a - ndfl
print('Итого ', a, ' | Без НДФЛ ', result, ' | НДФЛ ', ndfl, ' | Ставка ', stavka, ' %', sep='')
# System Pause
input()