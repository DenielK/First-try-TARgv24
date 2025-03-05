import string #импорт всей библиотеки
vokaali=["a","e","u","o","i","ü","ö","õ","ä"] #vokaali - гласные
konsonanti="qwrtpsdfghlzxcvbnm" #konsonanti - согласные
markid=string.punctuation #пунктуация значков %&'()*+,-./:;<=>?@[\]^_`{|}~
while True:
    v=k=m=t=0
    tekst=input("Sisesta mingi tekst: ").lower()
    if tekst.isdigit():
        break #если введут текст, то закончится сразу
    else:
        tekst_list=list(tekst) #разбивает на элементы
        print(tekst_list)
        for taht in tekst_list: #перебираем каждую букву
            if taht in vokaali:
                v+=1
            elif taht in konsonanti:
                k+=1
            elif taht in markid:
                m+=1
            elif taht ==" ":
                t+=1
    print("Vookali:", v)
    print("Konkonanti:", k)
    print("Markid:", m)
    print("Tühikud:", t)

#2
nimed=[]
for i in range(5):
        nimi=input(f"{i+1}.Nimi: ")
        nimed. append(nimi)
print("Enne sorteerimist:")
print(nimed)

nimed.sort()
print("Sorteeminise pärast:")
print(nimed)
print(f"Viimasena lisatud nimi on: {nimi}")#{nimed[4]}, {nimed[-1]}
v=input("kas muudame nimeid?: ").lower()
if v=="jah":
    v=input("Nime või positsioon: N/P").upper()
    if v=="P":
        print("Sisesta nimi asukoht")
        v=int(input())
        uus_nimi=input("Uus nimi: ")
        nimed[v-1]=uus_nimi
    else:
        print("Sisesta nimi")
        vana_nimi=input("Vana nimi: ")
        v=nimed.index(vana_nimi)
        uus_nimi=input("Uus nimi: ")
        nimed[v]=uus_nimi
    print(nimed)
# dublikatid 1
dublta=list(set(nimed))
print(dublta)
# dublikatid 2
dublta=[]
for nimi in nimed:
    if nimi not in dublta:
            dublta.append(nimi)
print("Mitte korduv loetelu2.variant")
print(dublta)