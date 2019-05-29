"""
1. Роздрукувати всі парні числа менші 100 (написати два варіанти коду: один використовуючи цикл while, а інший з використанням циклу for).
"""
for i in range(0,100,2):
  print(i,end=" ")

i=0
while i<100:
  print(i,end=" ")
  i+=2
  
"""
2. Роздрукувати всі непарні числа менші 100. (написати два варіанти коду: один використовуючи оператор continue, а інший без цього оператора).
"""
for i in range(100):
  if i%2==0:
    continue
  print(i,end=" ")

for i in range(100):
  if i%2!=0:
    print(i,end=" ")
"""	
3. Перевірити чи список містить непарні числа.
(Підказка: використати оператор break)
"""
list_example=[15,16,1,4,7,8,9,6,3,2,5,4,4,1,4,5,2,1,4,5,2,356,54,12]
for i in list_example:
  if i%2==1:
    print("There are odd values in the list")
    break
else:
  print("There are no odd values in the list")

"""
4. Створити список, який містить елементи цілочисельного типу, потім за допомогою циклу перебору змінити тип даних елементів на числа з плаваючою крапкою.
(Підказка: використати вбудовану функцію float ()).
"""
list_example=list(range(15))
for i in range(len(list_example)):
  list_example[i]=float(list_example[i])
print(list_example)

"""
5. Вивести числа Фібоначі включно до введеного числа n, використовуючи цикли. (Послідовність чисел Фібоначі 0, 1, 1, 2, 3, 5, 8, 13 і т.д.)
"""
fibo=[0,1,1]
user_input=int(input("Please enter the max value of the Fibonachi row: \n"))
while user_input>=fibo[len(fibo)-1]:
  fibo.append(fibo[len(fibo)-1]+fibo[len(fibo)-2])
print(fibo[0:len(fibo)-1])

"""
6. Створити список, що складається з чотирьох елементів типу string. Потім, за допомогою циклу for, вивести елементи по черзі на екран.
"""
list_example=["a","b","c","d"]
for i in list_example:
  print(i,end=", ")

"""
7. Змінити попередню програму так, щоб в кінці кожної букви елементів при виводі додавався певний символ, наприклад “#”.
(Підказка: цикл for може бути вкладений в інший цикл, а також треба використати функцію print(“ ”, end=”%”)).
"""
list_example=["a","b","c","d"]
for i in list_example:
  print(i,end="#, ")