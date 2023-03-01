from tkinter import *


# создаем кнопку которая будет прибавлять введенное число
def add_on():
    # переменная num принимает введенное число
    num = enter_txt.get()
    # переменная становится числом
    num = int(num)
    # переменная answer принимает текст для вывода
    answer = output_txt["text"]
    # переменная становится числом
    answer = int(answer)
    # делаем счетчик сложения 0 + введенное число
    total = answer + num
    # текст отображаемый на выводе становится переменной суммы
    output_txt["text"] = total


def reset():
    # делаем нулевой счетчик
    total = 0
    # число на выводе принимает нулевое значение
    output_txt["text"] = 0
    # удаляем содержимое отображаемого числа
    enter_txt.delete(0, END)
    enter_txt.focus()


total = 0
num = 0

window = Tk()
window.title("Складывание чисел")
window.geometry("500x200")
# window.resizable(width=False, height=False)

# добавляем текстовый элемент
enter_lbl = Label(text="Введите число: ")
enter_lbl.place(x=50, y=20, width=100, height=25)

# делаем область ввода текста
enter_txt = Entry()
enter_txt.place(x=150, y=20, width=100, height=25)
enter_txt.focus()

# делаем кнопку и подключаем ее
add_btn = Button(text="Добавить", command=add_on)
add_btn.place(x=300, y=20, width=100, height=30)

# добавляем текстовый элемент
output_lbl = Label(text="Ответ = ")
output_lbl.place(x=50, y=50, width=100, height=25)

# делаем область вывода с пустым значением, чтобы потом присвоить нулевую переменную
output_txt = Message(text="")
output_txt.place(x=150, y=50, width=100, height=25)

# делаем кнопку и подключаем ее
clear_btn = Button(text="Очистить", command=reset)
clear_btn.place(x=300, y=50, width=100, height=30)

window.mainloop()