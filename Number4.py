2
while True:
    try:
        A=int(input("Sisesta A:"))
        break
    except:
        print("on vaja naturaalne arv")
summa=0
if A>0:
    for i in range(1,A+1,1):
        summa+=i                         #summa=summa+1
        print(f"{i}. samm summa={summa}")
print(f"Vastus {summa}")

#3
p=1
for j in range(8):
    while True:
        try:
            arv=float(input(f"Sisesta {j+1} arv:"))
            break
        except:
            print("on vaja arv")
    if arv>0: 
        p*=arv
    else:
        print("Korrutame arvud rohkem kui 0")
    print(f"{j+1}. samm korrutis= {p}")
print(f"Lõpputulemus on {p}")

#4
for i in range(10,20,1):
    print(i**2, end=";")

print()

#16
for j in range(1,10):
    for i in range(1,10):
        if i==j:
            print(j,end=" ")
        else:
            print("0", end=" ")
    print()

print()

#15
for read in range(10):
    for rida in range(10):
        print(rida, end=" ")
    print()
print()

#1
for i in range (10):
