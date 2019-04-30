num_1 = int(input("Enter first num: "))
res = input("+ or -: ")
num_2 = int(input("Enter second num: "))

if res == "-":
    res = num_1 - num_2     
elif res == "+": 
    res = num_1 + num_2   
else:
    ("Enter please + or -" )
print("Resule is", res)