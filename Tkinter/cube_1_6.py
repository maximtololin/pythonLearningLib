from tkinter import *
import random


def click():
    num = random.randint(1, 6)
    answer["text"] = num


window = Tk()
# заголовок окна программы
window.title("Cube")
# размер окна программы
window.geometry("500x410")

# создаем кнопку с текстом и нажатием
button1 = Button(text="Press me", command=click)
# устанавливаем расположение кнопки
button1.place(x=140, y=50, width=220, height=100)

# создаем область для вывода данных
answer = Message(text="")
answer.place(x=40, y=70, width=30, height=25)

window.mainloop()