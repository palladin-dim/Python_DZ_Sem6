'''
Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного
максимума)
Ввод: [-5, 9, 0, 3, -1, -2, 1,
4, -2, 10, 2, 0, -9, 8, 10, -9,
0, -5, -5, 7]
Вывод: [1, 9, 13, 14, 19]
'''

mas = list(map(int, input('Введите числа списка через пробел: ').split()))
counter = 0
print(*mas)

maxi=int(input("max = "))

mini=int(input("min = "))

masi=[]

if maxi>=mini:

   for i in range(len(mas)):

      if maxi>=mas[i] and mini<=mas[i]:

          masi.append(i)

   print("Кол-во:",len(masi))

   print("Индексы:",masi)