number = 2345
x = 1
for i in str(number):
    x *= int(i)
print(x)    
print(str(number) [::-1])
print("".join(sorted(str(number))))