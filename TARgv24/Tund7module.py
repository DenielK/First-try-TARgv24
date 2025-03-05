from random import randint
from telnetlib import theNULL


def summa3(arv1:int,arv2:int,arv3:int)->int:
    """Tagastab kolme täisarvu summa

    :param int arv1: Esimene number
    :param int arv2: Teine number
    :param int arv3: Kolmas number
    :rtype: int


    """
    summa=arv1+arv2+arv3
    return summa

#1
def arithmetic(a:float,b:float,t:str)->any:
    """Lihtne kalkulaator.
    + - liitmine
    - - lahutamine
    * - korrutamine
    / - jagamine
    :param float a: arv1
    :param float b: arv2
    :param srt t: atitmeetiline tehing
    :rtype var Määramata tüüp(float or str)
    """
    if t in ["+","-","*","/"]:
        if b==0 and t=="/":
            vastus="DIV/0"
        else:
            vastus=eval(str(a)+t+str(b))
    else:
        vastus="Tundmatu tehe"
    
    return vastus

#2
def is_year_leap(aasta:int)->bool:
    """Liigasta leidmine
    Tagastab True, kui liigaasta ja False kui on tavaline aasta.
    :param int aasta: aasta number
    :rtype: bool tagastab loogilises foormaadis tulemus
    """

    if aasta%4==0:
        v=True
    else:
        v=False
    return v

#3
def square_text(a:float)->str:
    """
    """
    S=a**2
    P=4*a
    d=(2)**(1/2)*a

    return "Pindala "+str(S)+"\nÜmbermõõt "+str(P)+"\nLäbimõõt "+str(d)

#4
def season(month:int)->str:
    """
    """
    if month >= 3 and month < 6:
        month="kevad"
    elif month >= 6 and month < 9:
        month="summer"
    elif month >= 9 and month < 12:
        month="autumn"
    elif month == 12 or month < 3:
        month="winter"
    else:
        month="We have only 12 months"
    return month

#5
def bank(a:float,years:int)->float:
    """
    """
    for i in range(years):
        a*=1.1
    return round(a, 3)

#6
def is_prime(a=randint(0,1000))->bool:
    """
    """
    print(a)
    v=False
    for i in range(2,a):
        if a%i==0:
            v=True

    return v
