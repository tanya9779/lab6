'''
Задача B
++++++++

Одна фирма обслуживает автоматы по продаже чая и кофе.

Стоимость стакана чая и кофе в автомате равна пяти рублям. Автомат принимает монеты по 5 и 10 рублей, а также купюры в
10, 50 и 100 рублей. Когда покупателю надо выдавать сдачу (т.е. когда пассажир бросил в автомат десятирублёвую монету
или 10-, 50- или 100-рублёвую купюру), автомат выдаёт сдачу пятирублёвыми монетами; если же покупатель бросил в автомат
пятирублёвую монету, то автомат её сохраняет и может использовать для сдачи следующим покупателям.

Ясно, что, чтобы обеспечить возможность выдачи сдачи всем покупателям, может потребоваться изначально загрузить в
автомат некоторое количество пятирублёвых монет. Сейчас автоматы проходят испытания с целью определить минимальное
количество монет, которые надо загрузить в автомат перед началом дня. Вам дан протокол одного из таких испытаний:
известен порядок, в котором покупатели оплачивали свои покупки различными монетами и купюрами. Определите, какое
минимальное количество пятирублёвых монет должно было изначально находиться в автомате, чтобы всем покупателям хватило
сдачи.

В первой строке входных данных находится одно натуральное число N — количество покупок в автомате, которые были
совершены в ходе испытания (1≤N≤50000). Во второй строке находятся N натуральных чисел, каждое из которых равно номиналу
монеты или купюры, которую использовал очередной покупатель для оплаты; каждый номинал может принимать одно из четырёх
значений: 5, 10, 50 или 100.

Выведите одно число — минимальное количество пятирублёвых монет, которые надо было загрузить в автомат изначально, чтобы
всем покупателям хватило сдачи.

+----------+-------+
| Ввод     | Вывод |
+==========+=======+
| 3        | 19    |
+----------+-------+
| 10 5 100 |       |
+----------+-------+
+----------+-------+
| 3        | 0     |
+----------+-------+
| 5 5 10   |       |
+----------+-------+
+----------+-------+
| 4        | 9     |
+----------+-------+
| 50 5 5 5 |       |
+----------+-------+
'''

in_f=open('input.txt')
out_f=open('output.txt','w')
s=in_f.readline().rstrip()
N=int(s)
s=in_f.readline().rstrip()
A = list(map(int, s.split()))

S=0 # считаем, сколько накопилось на сдачу
B=[] # список, сколько монет  не хватило на сдачу (каждый раз когда не хватило)
max_n=0
for i in range(N):
    if A[i]==5: # еще одна монета на сдачу
        S+=1
    else:
        if S<(A[i]//5)-1: # того что есть, на сдачу не хватает
            B.append((A[i]//5)-1-S) # запомним, сколько не хватило
            S=0
        else: # сможем сдать своими
            S-=(A[i]//5)-1
if len(B)>0:
    max_n=sum(B) # сложим все что не хватило
print(max_n,file=out_f)
in_f.close()
out_f.close()

