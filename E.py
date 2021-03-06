'''
Задача E
++++++++

В одном карточном клубе состоит N джентльменов. Иногда азарт некоторых из них берет верх над благоразумием, и кто-то
проигрывает больше денег, чем у него есть с собой. В этом случае проигравший обычно берет в долг у кого-то из
посетителей клуба, чтобы расплатиться с партнерами по игре. Чтобы начать новый год “с чистого листа”, джентльмены решили
собраться в клубе и оплатить все долговые расписки, которые накопились у них друг к другу. Однако выяснилось, что иногда
одни и те же джентльмены в разные дни выступали как в роли должников, так и в роли кредиторов. Поскольку истинные
джентльмены считают мелочный подсчет денег ниже своего достоинства, то расчетами придется заняться вам.

Напишите программу, которая по заданным распискам вычислит, сколько всего должен каждый джентльмен выплатить другим (или
получить с других).

Первая строка входных данных содержит сначала число N — количество джентльменов (натуральное, не превышает 100, не менее
2), и число K — количество долговых расписок (натуральное, не превышает 10000), после этого следует K троек чисел: номер
джентльмена взявшего в долг, номер джентльмена давшего деньги и сумма. Номера джентльменов в расписках — натуральные
числа, не превышающие N. Сумма — натуральное число, не превышает 100. Гарантируется, что ни один джентльмен не брал в
долг сам у себя.

Выведите N чисел — суммы, которые должны получить соответствующие джентльмены. Выведите положительное число, если этот
джентльмен должен получить деньги от других, отрицательное — если он должен отдать деньги другим.

+---------+------------+
| Ввод    | Вывод      |
+=========+============+
| 2 3     | -50 50     |
+---------+------------+
| 1 2 10  |            |
+---------+------------+
| 1 2 20  |            |
+---------+------------+
| 1 2 20  |            |
+---------+------------+
+---------+------------+
| 3 1     | 100 0 -100 |
+---------+------------+
| 3 1 100 |            |
+---------+------------+
'''

#creditor - тот кто дал в долг
#debtor - тот кто взял

in_f=open('input.txt')
out_f=open('output.txt','w')
s=in_f.readline().rstrip()
N,K=list(map(int,s.split()))
gentleman=[]
for j in range(N+1): # отчет с 1 - в списке будут суммы
    gentleman.append(0)

for i in range(K): # обработаем все расписки
    s=in_f.readline().rstrip()
    debtor,creditor,summa = list(map(int, s.split()))
    gentleman[debtor]-=summa
    gentleman[creditor]+=summa

print(' '.join(map(str,gentleman[1: ])),file=out_f) # отчет от 1
in_f.close()
out_f.close()