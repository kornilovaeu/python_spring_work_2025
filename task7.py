#todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().


print ('Введите три точки на числовой оси:')
A, B, C = map (float, input ().split())

AC = abs (C-A)
BC = abs (C-B)
summa = AC + BC

print ('Длина отрезка AC=', AC, 'Длина отрезка BC=', BC, '.', 'Cумма указанных отрезков =', summa)