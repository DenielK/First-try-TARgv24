﻿import numpy as np #надо скачать отдельно через подарок
import matplotlib.pyplot as plt #надо скачать отдельно через подарок 

def Vaal(color:str):
    x1=np.arange(0,10,1) #0,1,2,3,4,5,6,7
    y1=(2/27)*x1**2-3
    x2=np.arange(-10,1,1)
    y2=0.04*x2**2-3
    x3=np.arange(-9,-2.5,0.5)
    y3=(2/9)*(x3+6)**2+1
    x4=np.arange(-3,8.5,0.5)
    y4=(-1/12)*(x4-3)**2+6
    x5=np.arange(5,8,0.5)
    y5=(1/9)*(x5-5)**2+1.5
    x6=np.arange(5,8.5,0.5)
    y6=(1/8)*(x6-7)**2+1.5
    x7=np.arange(-13,-8.5,0.5)
    y7=(-0.75)*(x7+11)**2+6
    x8=np.arange(-15,-12.5,0.5)
    y8=(-0.5)*(x8+13)**2+3
    x9=np.arange(-15,-10,0.5)
    y9=[1]*len(x9)
    x10=np.arange(3,4,0.5)
    y10=[3]*len(x10)
    plt.figure(facecolor=color)
    plt.title("Vaal")
    plt.ylabel=("Y")
    plt.xlable=("X")
    plt.grid(True)
    ax=plt.axes()
    ax.set_facecolor("lightblue")
    #plt.plot(x1,y1,"r:o") - если каждую строку отдельно делать
    colors=("c","m","y","r","g","b","w","k","b","b") 
    for i in range(1,11): #делать через цикл
        plt.plot(eval(f"x{i}"),eval(f"y{i}"),color[0]+"-*")#colors[i-1]+"-*")#colors[i-1]+"-*") #b-* цвет,стиль линии и маркер
    plt.show()

def Zontik(color:str):
    x1=np.arange(-12,11.5,0.5)
    y1=(-1/18)*x1**2+12
    x2=np.arange(-4,4.5,0.5)
    y2=(-1/8)*x2**2+6
    x3=np.arange(-12,-4,0.5)
    y3=(-1/8)*(x3+8)**2+6
    x4=np.arange(4,11.5,0.5)
    y4=(-1/8)*(x4-8)**2+6
    x5=np.arange(-4,-0.2,0.1)
    y5=2*(x5+3)**2-9
    x6=np.arange(-4,0.3,0.1)
    y6=1.5*(x6+3)**2-10
    plt.figure(facecolor=color)
    plt.title("Zontik")
    plt.ylabel=("Y")
    plt.xlable=("X")
    plt.grid(True)
    ax=plt.axes()
    ax.set_facecolor("lightblue")
    colors=("c","m","y","r","g","k") 
    for i in range(1,7): #делать через цикл
        plt.plot(eval(f"x{i}"),eval(f"y{i}"),color[0]+"-*")#colors[i-1]+"-*") #b-* цвет,стиль линии и маркер
    plt.show()

