a=list(input("Введите слово: "))
print(a)
k=0
for i in a:
    if (i == "a") or (i == "e") or (i == "i") or (i == "o") or (i == "u"):
        k=k+1
print("Гласных букв =", k) 
print("Согласных букв =", len(a)-k) 

h=0
s=0
d=0
f=0
g=0
for i in a:
    if (i == "a"):
        h=h+1
    elif (i == "e"):
        s=s+1
    elif (i == "i"):
        d=d+1
    elif (i == "o"):
        f=f+1
    elif (i == "u"):
        g=g+1
    else: continue

print ("a =", h if h>0 else "False", ", e =", s if s>0 else "False", ", i =", d if d>0 else "False", ", o =", f if f>0 else "False", ", u =", g if g>0 else "False")
