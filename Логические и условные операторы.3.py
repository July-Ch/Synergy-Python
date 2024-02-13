a=int(input("Сумма Майкла: "))
b=int(input("Сумма Ивана: "))
x=int(input("Минимальная сумма: "))
y=a+b
if (a>=x) and (b<x):
    print ("Mike")
elif (b>=x) and (a<x):
    print ("Ivan")
elif (a>=x) and (b>=x):
    print (2)
elif (y>=x):
    print (1)
else: print (0)
