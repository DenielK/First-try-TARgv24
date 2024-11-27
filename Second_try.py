from datetime import *
from calendar import *
from math import *
from random import *
from xml.sax import default_parser_list

# from socket import RCVALL_SOCKETLEVELONLY 


#Ülesanne 1
paevadekogus=(monthrange(2024,11)[1]) #calendar modulist
print(paevadekogus)

tana=date.today() #nimetus()-finktsioon
tanaf=date.today().strftime("%B %d, %Y")

print(f"Tere! Tana on {tanaf}")
d=tana.day #nimetus - omadus
m=tana.month
y=tana.year
print(d)
print(m)
print(y)

detsP=monthrange(2024,12)[1] #31

novP=monthrange(2024,11)[1] #30
jaak=detsP+novP-d
jaak2=novP-d
print(f"Aasta loppuni on {jaak}")
print(f"Kuu loppuni on {jaak2}")

#Ülesanne 2
vastus1=3 + 8 / (4 - 2) * 4
vastus2=3+8 / 4 - 2 * 4
vastus3= (3 + 8) / (4 - 2) * 4
print(vastus1)
print(vastus2)
print(vastus3)
print(vastus1,"\n",vastus2,"\n", vastus3)

#Ülesanne 3
try:
    R=float(input("Sisesta R: ")) #с десятичными 1.01
    Sk=pi*R**2 #** степень
    Lk=2*pi*R
    Skv=(2*R)**2
    Lkv=2*R*4
    print(f"Ringi pindala on {Sk}\nRingi umbermoot on {Lk}\nRuudu pindala pn {Skv}\n Ruudu umbermoot on {Lkv}\n") #print(f) alt gr 7 {}
except:
    print("On vaja number!")

#Variant 2

R=round(random()*100) #0.0...1.0
print(f"R={R}")
Sk=pi*R**2 #** степень
Lk=2*pi*R
Skv=(2*R)**2
Lkv=2*R*4
print(f"Ringi pindala on {Sk}\nRingi umbermoot on {Lk}\nRuudu pindala pn {Skv}\n Ruudu umbermoot on {Lkv}\n")

#Ülesanne 4
d=2.575 #mündi d sm
maa=6378 #maa radius km 
maa*=100000 #Radius sm + maa=maa*10000 = maa*=10000
Lmaa=2*pi*maa
kogus=int(Lmaa/d)
print(f"On vaja {kogus:,d} mundi.\nMeil on vaja{kogus*2:,d} eur")