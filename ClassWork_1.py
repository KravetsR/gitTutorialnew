# 1. Написати скрипт, який з двох введених чисел визначить, яке з них більше, а яке менше.
number1=input("enter number1=")
number2=input("enter number2=")
if(number1>=number2):
    print("max",number1, "min",number2)
else:
    print("max",number2 , "min", number1)


# 2. Написати скрипт, який перевірить чи введене число парне чи непарне і вивести відповідне повідомлення.

number1=input("enter number1=")
number1=int(number1)
if(number1 % 2):
    print("odd number")
else:
    print('even number') 

# 3. Написати скрипт, який обчислить факторіал введеного числа.

number1=input("enter number1=")
number1=int(number1)
i=1
b=1
while number1 > i:
    i=i+1
    b=b*i
    
print(b)