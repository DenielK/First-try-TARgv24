# from random import * #*-kõik funktsioonid, randint as rd funktsioonide ümbernimetus
from math import * #pi kasutamiseks
from fractions import Fraction

#Ülesanne 1

# Мы используем: print(), input(), float(), int(), Upper(), Lower(), Capitalize(), математические функции
# type()
# , функции случайных модулей: pi, round(), randint().

# 1 .
# Напишите свою первую программу, которая выводит в командную строку текст: «Привет, мир!». 
# Запросите имя пользователя и измените текст так: «Привет, мир! Привет, Мати», если имя пользователя — Мати.

# Попросите пользователя ввести информацию о его возрасте и выведите его на экран:

# "Привет, мир! Привет Мати! Тебе N лет».

# 2

# К какому типу относятся следующие переменные:

# а) возраст = 18
# б) имя = «Яак»
# в) длина = 16,5
# г) if_goes_to_school = True
# Каким еще способом, кроме True, можно было бы получить значение последней переменной? Как можно было проверить значения этих переменных в коде?
# Напишите код для проверки типов.



# 3

# В коде игры запишите количество конфет на столе в переменную. Затем выведите на экран количество конфет в переменной с помощью команды print().
# Попросите пользователя указать, сколько конфет он хочет убрать со стола. Удалите нужное количество конфет из количества конфет на столе и отобразите на экране, сколько конфет сейчас находится на столе.
# 4

# Вычисление диаметра дерева
# Напишите программу, которая запрашивает у пользователя длину окружности дерева, а затем сообщает диаметр дерева.

# 5.
# Рассчитайте длину диагонали прямоугольного участка земли размерами Нм х мм в командной строке Python. N и M спрашивают пользователя.

# 6
# Найдите семантическую ошибку в следующем примере программы:
# time = float(input("Сколько часов вам потребовалось, чтобы ехать?")) 
# distance = float(input("Сколько километров вы проехали?")) 
# скорость = время / расстояние 

# print("Ваша скорость была " + str (скорость) + «км/ч»)
# 7.
# Напишите программу, которая вычисляет среднее арифметическое любых пяти целых чисел.

# 8.
# Нарисуйте такую ​​же лягушку
#    @..@
#    (----)
#   ( \__/ )
# ^^ "" ^^  
# 9.
# Давайте посчитаем периметр треугольника. Создайте три целочисленные переменные a, b, c. Создайте формулу, вычисляющую периметр треугольника (P=a+b+c).

# 10.
# Пицца

#     Вы взяли с другом большую пиццу P за 12,90 евро.
#     Вы оставляете официанту чаевые в размере 10 %.
#     Создайте программу, которая определяет, сколько каждый должен заплатить.

# print ("Hello World")
# nimi=input("Mis on sinu nimi? ").capitalize() #lower()все маленькие ааа,upper()все большие ААА ,capitalize - с большой буквы Ааа
# print ("Tere tulemast! Tervitan sind ", nimi)
# print ("Tere tulemast! Tervitan sind "+ nimi)
# vanus=int(input("Kui vana sa oled? "))
# print ("Tere tulemast! Tervitan sind "+nimi+" Sa oled ",vanus,"aastat vana" )
# print (f"\tTere tulemast! \nTervitan sind {nimi} Sa oled {vanus} aastat vana" )

#Ülesanne 2

# vanus = 18
# eesnimi = "Jaak"
# pikkus = 16.5
# kas_käib_koolis = True
# print(type(vanus))

#Ülesanne 3
# kokku=randint(1,1000)
# print (f"Kokku on {kokku} kommi")
# kommi=int(input("Mitu kommi sa tahad? "))
# kokku-kommi
# print(f"Jääk on {kokku} kommi")

#Ülesanne 4
# print("Läbimõõdu leidmine ")
# #l-ümbermõõt
# l=float(input("Ümbermõõt: "))
# d=l/pi
# print(f"Läbimõõdu suurus on {round(d,2)}")













# #10
# from fractions import Fraction

# BigPizza = 12.9
# DefaultTips = 0.1
# Tips = DefaultTips * BigPizza
# print(f"Your tips is {Tips}")