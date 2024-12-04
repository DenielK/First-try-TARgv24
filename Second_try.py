from datetime import *
from calendar import *
from math import *
from random import *
from xml.sax import default_parser_list
from re import A

# from socket import RCVALL_SOCKETLEVELONLY 


# #Ülesanne 1
# paevadekogus=(monthrange(2024,11)[1]) #calendar modulist
# print(paevadekogus)

# tana=date.today() #nimetus()-finktsioon
# tanaf=date.today().strftime("%B %d, %Y")

# print(f"Tere! Tana on {tanaf}")
# d=tana.day #nimetus - omadus
# m=tana.month
# y=tana.year
# print(d)
# print(m)
# print(y)

# detsP=monthrange(2024,12)[1] #31

# novP=monthrange(2024,11)[1] #30
# jaak=detsP+novP-d
# jaak2=novP-d
# print(f"Aasta loppuni on {jaak}")
# print(f"Kuu loppuni on {jaak2}")

# #Ülesanne 2
# vastus1=3 + 8 / (4 - 2) * 4
# vastus2=3+8 / 4 - 2 * 4
# vastus3= (3 + 8) / (4 - 2) * 4
# print(vastus1)
# print(vastus2)
# print(vastus3)
# print(vastus1,"\n",vastus2,"\n", vastus3)

# #Ülesanne 3
# try:
#     R=float(input("Sisesta R: ")) #с десятичными 1.01
#     Sk=pi*R**2 #** степень
#     Lk=2*pi*R
#     Skv=(2*R)**2
#     Lkv=2*R*4
#     print(f"Ringi pindala on {Sk}\nRingi umbermoot on {Lk}\nRuudu pindala pn {Skv}\n Ruudu umbermoot on {Lkv}\n") #print(f) alt gr 7 {}
# except:
#     print("On vaja number!")

# #Variant 2

# R=round(random()*100) #0.0...1.0
# print(f"R={R}")
# Sk=pi*R**2 #** степень
# Lk=2*pi*R
# Skv=(2*R)**2
# Lkv=2*R*4
# print(f"Ringi pindala on {Sk}\nRingi umbermoot on {Lk}\nRuudu pindala pn {Skv}\n Ruudu umbermoot on {Lkv}\n")

# #Ülesanne 4
# d=2.575 #mündi d sm
# maa=6378 #maa radius km 
# maa*=100000 #Radius sm + maa=maa*10000 = maa*=10000
# Lmaa=2*pi*maa
# kogus=int(Lmaa/d)
# print(f"On vaja {kogus:,d} mundi.\nMeil on vaja{kogus*2:,d} eur")

#Ülesanne 5
sõna1 = "Kill-koll"

a1 = "kill-koll ".capitalize()

a2 = "killadi-koll ".capitalize()

print(f"{a1}{a1}{a2}{a1}{a1}{a2}{a1}{a1}{a1}{a1}")

#6
y1 = "Rong see sõitis tsuhh tsuhh tsuhh,".upper()
y2 = "piilupart oli rongijuht.".upper()
y3 = "Rattad tegid rat tat taa,".upper()
y4 = "rat tat taa ja tat tat taa.".upper()
y5 = "Aga seal rongi peal,".upper()
y6 = "kas sa tead, kes olid seal?".upper()
y7 = "Rong see sõitis tuut tuut tuut,".upper()
y8 = "piilupart oli rongijuht.".upper()
y9 = "Rattad tegid kill koll koll,".upper()
y10 = "kill koll koll ja kill koll kill.".upper()
y11 = "....Sisend, väljund, tingimus....".upper()
print(f"{y1}\n{y2}\n{y3}\n{y4}\n{y5}\n{y6}\n\n{y7}\n{y8}\n{y9}\n{y10}\n\n\n\n{y11}")

#7
a = float(input("Palun sisestage esimene ristküliku külg: "))
b = float(input("Palun sisestage teine ristküliku külg: "))
Pr = 2 * (a + b)
Sr = a * b
print(f"Ristkuliku umbermoot on {Pr} ja pindala on {Sr}!")

#8
litr = float(input("Palun sisestage tangitud kutuse liitrid: "))
kms = float(input("Palun sisestage labitud kilomeetrid: "))
toplivo = (litr / kms) * 100
print(f"Teie keskmine kütusekulu on {round(toplivo,2)}!")

#9

minutid = float(input("Sisesta aeg minutites: "))
kiiruskmh = 29.9
tunnid = minutid / 60
kaugus = kiiruskmh * tunnid
print(f"Rulluisutaja jõuab {minutid} minutiga {round(kaugus,2)} kaugusele")