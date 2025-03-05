from ast import Lambda
from tkinter import*
from Tund10Matplotlib import*
global värv


def värvi_valik():
    värv="white"
    if tekst.get()!="":
        tekst.configure(bg="yellow")
        värv=tekst.get()
    else:
        tekst.configure(bg="red")
    return värv

def figuur(värv:str):
    valik=var.get()
    värv=värvi_valik()
    if valik==1:
        Vaal(värv)
    elif valik==2:
        Zontik(värv)



aken=Tk() # Tk класс окна
aken.geometry("400x800")
aken.title("Graafikud")
pealkiri=Label(aken,text="Erinevad piltid Matplotlib abil",font="Calibri 24",fg="black",bg="lightgreen",padx=20,pady=20,width=100) #padx=20 - отступ на 20

var=IntVar()
r1=Radiobutton(aken,text="Vaal",font="Calibri 18",variable=var,value=1,command=lambda:figuur(värv=värvi_valik))
r2=Radiobutton(aken,text="Zontik",font="Calibri 18",variable=var,value=2,command=lambda:figuur(värv=värvi_valik))
tekst=Entry(aken,font="Calibri 24",fg="black",bg="lightgreen",width=50)
nupp=Button(aken, text="Värvi valik",font="Calibri 24", command=värvi_valik())


pealkiri.pack() #place(x=....,y=....),grid(column=....,row=....) если ставить на определенную точку
tekst.pack()
nupp.pack()
r1.pack()
r2.pack()
aken.mainloop()