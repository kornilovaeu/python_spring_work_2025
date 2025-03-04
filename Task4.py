x=10
y=15
z=2
a=[x, y, z]
max=a [0]
for i in a:
    if i > max:
        max=i
print ('Наибольшее число', max)

x=77
y=9
z=130
a=[x, y, z]
largest_number=a[0]
for i in range (1,len(a)):
    if a[i] > largest_number:
        largest_number=a[i]
print ('Наибольшее число', largest_number)
