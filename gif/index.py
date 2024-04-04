from tkinter import *
# 2d окно
root = Tk()  # создаем корневой объект - окно
root.title("Error")  # устанавливаем заголовок окна
root.geometry("400x100")  # устанавливаем размеры окна

label = Label(text="Error png, pleas remove", font=('Arial', 25))  # создаем текстовую метку
label.pack()  # размещаем метку в окне

root.mainloop()

