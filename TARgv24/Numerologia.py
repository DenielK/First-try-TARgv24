import tkinter as tk
from tkinter import messagebox

# Функция для создания таблицы чисел для русского алфавита
def loo_vene_tabel():
    vene_tabel = {
        'А': 1, 'Б': 2, 'В': 3, 'Г': 4, 'Д': 5, 'Е': 6, 'Ё': 7, 'Ж': 8, 'З': 9,
        'И': 1, 'Й': 2, 'К': 3, 'Л': 4, 'М': 5, 'Н': 6, 'О': 7, 'П': 8, 'Р': 9,
        'С': 1, 'Т': 2, 'У': 3, 'Ф': 4, 'Х': 5, 'Ц': 6, 'Ч': 7, 'Ш': 8, 'Щ': 9,
        'Ы': 1, 'Э': 2, 'Ю': 3, 'Я': 4
    }
    return vene_tabel

# Функция для создания таблицы чисел для латинского алфавита
def loo_ladina_tabel():
    ladina_tabel = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
        'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 6, 'P': 7, 'Q': 8, 'R': 9,
        'S': 1, 'T': 2, 'U': 3, 'V': 4, 'W': 5, 'X': 6, 'Y': 7, 'Z': 8
    }
    return ladina_tabel

# Функция для определения алфавита
def tuvasta_tähestik(nimi):
    if all(c in 'АБВГДЕЁЖЗИКЛМНОПРСТУФХЦЧШЩЫЭЮЯ' for c in nimi.upper()):
        return 'vene'
    elif all(c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' for c in nimi.upper()):
        return 'ladina'
    else:
        raise ValueError("Невозможно определить алфавит. В имени смешаны буквы разных алфавитов.")

# Функция для вычисления номера имени
def arvuta_nime_number(nimi, tabel):
    summa = sum(tabel.get(c.upper(), 0) for c in nimi)
    return reduktsioon(summa)

# Функция для редукции числа до однозначного
def reduktsioon(summa):
    while summa >= 10:
        summa = sum(int(digit) for digit in str(summa))
    return summa

# Функция для сохранения результатов в файл
def salvesta_tulemus(nimi, number):
    with open("nimetulemused.txt", "a") as f:
        f.write(f"{nimi}: {number}\n")

# Функция для вычисления и отображения результата
def arvuta_ja_kuvasta():
    nimi = nimi_entry.get()
    try:
        # Определяем, какой алфавит используется
        if tuvasta_tähestik(nimi) == 'vene':
            tabel = loo_vene_tabel()  # Для русского алфавита
        else:
            tabel = loo_ladina_tabel()  # Для латинского алфавита

        # Вычисляем номер имени
        number = arvuta_nime_number(nimi, tabel)

        # Отображаем результат на экране
        tulemus_label.config(text=f"Результат: {number}")

        # Запрашиваем, сохранить ли результат
        if messagebox.askyesno("Сохранить результат", "Хотите сохранить результат?"):
            salvesta_tulemus(nimi, number)
    except ValueError as ve:
        messagebox.showerror("Ошибка", str(ve))

# Создаем окно Tkinter
root = tk.Tk()
root.title("Вычисление номера имени")

# Метка и поле ввода для имени
nimi_label = tk.Label(root, text="Введите имя:")
nimi_label.pack()

nimi_entry = tk.Entry(root)
nimi_entry.pack()

# Кнопка для вычисления результата
arvuta_button = tk.Button(root, text="Вычислить номер", command=arvuta_ja_kuvasta)
arvuta_button.pack()

# Метка для отображения результата
tulemus_label = tk.Label(root, text="Результат:")
tulemus_label.pack()

# Запуск основного цикла Tkinter
root.mainloop()
