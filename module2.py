import tkinter as tk
import ssl
import imghdr
from email.message import EmailMessage
from tkinter import W, E, N, S
from tkinter import Entry, Text, Button, Label, filedialog, messagebox

page = tk.Tk()
page.geometry('800x800')
#page.resizable(False,False)
page.title('E-mail Sender')

def vali_pilt():
    file = filedialog.askopenfilename()
    label_lisa2.delete(0, tk.END)  # Очистить поле ввода
    label_lisa2.insert(0, file)  # Вставить путь к файлу

def saada_kiri():
    kellele = label_email.get()
    teema = teema.get()
    kiri = entry_kiri.get("1.0", tk.END).strip()
    failitee = label_lisa2.get()

    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "your-email@gmail.com"  # Укажите свой email
    password = "your-app-password"  # Используйте пароль приложения Google

    if not kellele or not kiri:
        messagebox.showerror("Viga", "Palun sisestage e-posti aadress ja kiri!")
        return

    msg = EmailMessage()
    msg.set_content(kiri)
    msg['Subject'] = teema
    msg['From'] = sender_email
    msg['To'] = kellele

    if failitee:
        try:
            with open(failitee, 'rb') as fpilt:
                pilt = fpilt.read()
            msg.add_attachment(pilt, maintype='image', subtype=imghdr.what(None, pilt))
        except Exception as e:
            messagebox.showerror("Viga", f"Faili lisamine ebaõnnestus: {e}")
            return

    try:
        context = ssl.create_default_context()
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)
        server.login(sender_email, password)
        server.send_message(msg)
        server.quit()
        messagebox.showinfo("Informatsioon", "Kiri saadetud edukalt!")
    except Exception as e:
        messagebox.showerror("Tekkis viga!", f"Viga: {e}")


#настройки полей
label_email=tk.Label(page, text='EMAIL',font=('Calibri',26,'bold'),bg='green',width=10)
label_teema=tk.Label(page, text='TEEMA',font=('Calibri',26,'bold'),bg='green',width=10)
label_lisa=tk.Label(page, text='LISA',font=('Calibri',26,'bold'),bg='green',width=10)
label_kiri=tk.Label(page, text='KIRI',font=('Calibri',26,'bold'),bg='green',width=10)
label_lisa2=tk.Label(page, text='...',font=('Calibri',26,'bold'),bg='lightgreen',fg='white',width=25)
entry_email=tk.Entry(page,font=('Calibri',26,'bold'),bg='lightgreen',width=25)
entry_teema=tk.Entry(page,font=('Calibri',26,'bold'),bg='lightgreen',width=25)
entry_kiri=tk.Text(page,font=('Calibri',26,'bold'),bg='lightgreen',width=25)
button_pilt=tk.Button(page,text='LISA PILT',font=('Calibri',26,'bold'),bg='green')
button_saada=tk.Button(page,text='SAADA',font=('Calibri',26,'bold'),bg='green')
label_email.grid(row=0,column=0,sticky=W+E+N+S)
label_teema.grid(row=1,column=0,sticky=W+E+N+S)
label_lisa.grid(row=2,column=0,sticky=W+E+N+S)
label_kiri.grid(row=3,column=0,sticky=W+E+N+S)
label_lisa2.grid(row=2,column=1,sticky=W+E+N+S)
entry_email.grid(row=0,column=1)
entry_teema.grid(row=1,column=1)
entry_kiri.grid(row=3,column=1)
button_pilt.grid(row=4,column=0,padx=5, pady=5,sticky=W+E+N+S)
button_saada.grid(row=4,column=1,padx=5, pady=5,sticky=W+E+N+S)






page.mainloop()
