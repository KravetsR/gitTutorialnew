# 1.  Створити список цілих чисел, які вводяться з терміналу та визначити серед них максимальне та мінімальне число.

rices = [int(i) for i in input('Введите значения цен через пробел ').split()]
print(" Max number is:", max(rices))
print(" Min number is:", min(rices))
# 2.  В інтервалі від 1 до 10 визначити числа 
#  парні, які діляться на 2,
#  непарні, які діляться на 3, 
#  числа, які не діляться на 2 та 3.

for i in range(1, 11):
    if i % 2 == 0:
        print("parni = ", i)
    elif i % 3 == 0:
        print("neparni = ", i)
    else:
        print("ne dilatsa na 2,3 =", i)
# 3.  Написати програму, яка обчислює факторіал числа, яке користувач вводить.(не використовувати рекурсивного виклику функції) 
a = int(input())
b = 1
if a < 0:
    print("sorry, factorial doesnt exist negativ numbers")
else:
    for i in range(1, a+1):
        b *= i
    print("factorial number {0} sum {1}".format(a, b))
# 4.  Напишіть скрипт, який перевіряє логін, який вводить користувач. 
#Якщо логін вірний (First), то привітайте користувача. 
#Якщо ні, то виведіть повідомлення про помилку. 
#(використайте цикл while)

user_name = input("username ")
while user_name == "first":
    print('Hello')
    break
else:
    print('eror, try again')

''' 5.  Перший випадок. 
#Написати програму, яка буде зчитувати числа поки не зустріне від’ємне число. 
# При появі від’ємного числа програма зупиняється (якщо зустрічається 0 програма теж зупиняється).'''
a = 1
while a != 0:
    if a > 0:
        a = int(input())
        print('You number = ', a)
    else:
        break

'''# 6.  Другий випадок. 
# На початку на вхід подається кількість елементів послідовності, а потім самі елементи. 
# При появі від’ємного числа програма зупиняється (якщо зустрічається 0 програма теж зупиняється).'''

sum_pos = input()
sum_pos = int(sum_pos)
for i in range(sum_pos):
    chusla = int(input())
    if chusla < 0 or chusla == 0:
        break

# 7.  Знайти прості числа від 10 до 30, а всі решта чисел представити у вигляді добутку чисел 
#(наприклад 10 equals 2 * 5
#                    11 is a prime number
#                    12 equals 2 * 6
#                    13 is a prime number
#                    14 equals 2 * 7
#                     ………………….)

for i in range(10, 30):
    if i % 2 == 0:
        print(i, 'equals 2 *', i / 2)
    elif i % 3 == 0:
        print(i, 'equals 3 *', i / 3)
    else:
        print(i, 'is a prime number')
# 8.  Відсортувати слова в реченні в порядку їх довжини (використати List Comprehensions)
def sorting(lst):
    lst.sort(key=len)
    return lst
lst = ["rohan", "amy", "sapna", "muhammad",
       "aakash", "raunak", "chinmoy"]
print(sorting(lst))
"""