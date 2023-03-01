from tkinter import *


# кнопка, после нажатия на которую меняется цвет текстбокса2
def click():
    name = textbox1.get()
    message = str("Hello " + name)
    textbox2["bg"] = "yellow"
    textbox2["fg"] = "black"
    textbox2["text"] = message
    textbox2["justify"] = "center"
    textbox2.focus()


window = Tk()
# заголовок окна программы
window.title("First Program")
# размер окна программы
window.geometry("500x410")

# добавляем на экран текст, содержаний сообщение о вводе имени
label1 = Label(text="Enter your name: ")
# задаем позицию текста на экране
label1.place(x=30, y=20)

# создаем пустое текстовое поле для ввода
textbox1 = Entry()
# задаем положение текстового поля
textbox1.place(x=150, y=20, width=200, height=25)
# задаем выравнивание текстового поля
textbox1["justify"] = "center"
textbox1.focus()

# создаем кнопку с текстом и нажатием
button1 = Button(text="Press me", command=click)
# устанавливаем расположение кнопки
button1.place(x=30, y=50, width=120, height=25)

# создаем поле для вывода данных
textbox2 = Message(text="", bg="white", fg="black")
# задаем параметры текстовому полю
textbox2.place(x=150, y=50, width=200, height=25)

window.mainloop()
