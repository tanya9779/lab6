'''
Задача A
++++++++

В массиве ровно два элемента равны. Найдите эти элементы.

Программа получает на вход число N, в следующей строке заданы N элементов списка через пробел.

Выведите значение совпадающих элементов.

+-------------+-------+
| Ввод        | Вывод |
+=============+=======+
| 6           | 5     |
+-------------+-------+
| 8 3 5 4 5 1 |       |
+-------------+-------+
'''


in_f=open('input.txt')
out_f=open('output.txt','w')
s=in_f.readline().rstrip()
N=int(s)
s=in_f.readline().rstrip()
A = list(map(int, s.split()))
A.sort() # отсортируем список и
         # поищем два подрядыдущих
for i in range(N):
    tmp=A[i]
    if tmp==A[i+1]:
        break
print(str(tmp),file=out_f)
in_f.close()
out_f.close()