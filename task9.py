#todo Решить линейное уравнение A·x + B = 0, заданное своими коэффициентами A и B (коэффициент A не равен 0).
# Примечание: коэффициенты получаем через функцию input().

print ('Для решения линейного уравнения A·x + B = 0, введите, пожалуйста, значение коэффициентов А и В:')
A, B = map (float, input ().split())
x = -B / A

print (x)