import time
import main, sys, function
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Notebook, Frame, Combobox, Radiobutton
from threading import Thread

type_of_account = ''
login_of_account = ''
password_of_account = ''
condition_of_bot = ''

class Main_menu():
    def __init__(self):

        # Основные переменные


        self.window = Tk()
        # window.update()
        # window.attributes("-topmost", True)
        self.window.attributes('-topmost', False)
        self.window.title("Castle Quiz Bot")
        self.window.geometry("600x400")

        # Главное окно
        self.tab_control = Notebook(self.window)
        self.tab1 = Frame(self.tab_control)
        self.tab_control.add(self.tab1, text="Главное")

        # Дополнительное окно
        self.tab2 = Frame(self.tab_control)
        self.tab_control.add(self.tab2, text="Статистика")
        self.tab_control.pack(expand=True, fill=BOTH)

        # В этой части добавляются элементы главного меню

        self.login_text = Label(self.tab1, text="Введите логин:",
                          # bg="White",
                          fg="Black",
                          font=("Times new Roman", 10, "bold"),
                          bd=10,
                          justify=CENTER,
                          heigh=2,
                          width=15)

        self.login_text.place(relheight=0.08, relwidth=0.20, relx=0.01, rely=0.05)

        self.login_input = Entry(self.tab1, width=40)
        self.login_input.place(relheight=0.08, relwidth=0.25, relx=0.22, rely=0.05)

        self.password_text = Label(self.tab1, text="Введите пароль:",
                             # bg="White",
                             fg="Black",
                             font=("Times new Roman", 10, "bold"),
                             bd=10,
                             justify=CENTER,
                             heigh=2,
                             width=15)

        self.password_text.place(relheight=0.08, relwidth=0.20, relx=0.01, rely=0.2)
        bullet = "\u2022"
        self.password_input = Entry(self.tab1, width=40, show=bullet)
        self.password_input.place(relheight=0.08, relwidth=0.25, relx=0.22, rely=0.2)

        self.r_var = IntVar()
        self.r_var.set(0)

        self.r1 = Radiobutton(self.tab1, text='Vk', variable=self.r_var, value=0)
        self.r1.place(relheight=0.05, relwidth=0.2, relx=0.6, rely=0.1)
        self.r1.bind('<Button-1>')
        self.r2 = Radiobutton(self.tab1, text='Facebook', variable=self.r_var, value=1)
        self.r2.place(relheight=0.05, relwidth=0.2, relx=0.6, rely=0.15)
        self.r2.bind('<Button-2>')
        self.r3 = Radiobutton(self.tab1, text='Without registering', variable=self.r_var, value=2)
        self.r3.place(relheight=0.05, relwidth=0.3, relx=0.6, rely=0.2)
        self.r3.bind('<Button-3>')

        self.text_ = ('Состояние - выключен')
        self.condition_of_bot = Label(self.tab1, text=self.text_,
                                # bg="Light gray",
                                fg="Black",
                                font=("Times new Roman", 12, "bold"),
                                bd=10,
                                justify=CENTER,
                                heigh=2,
                                width=15)
        self.condition_of_bot.place(relheight=0.2, relwidth=0.4, relx=0.3, rely=0.55)

        self.start_btn = Button(self.tab1, text="Запустить",
                          bg="Light gray",
                          fg="Black",
                          # font = ("Times New Roman"),
                          bd=2,
                          justify=CENTER,
                          heigh=2,
                          width=15,
                          command=self.antifreeze
                          )
        self.start_btn.place(relheight=0.1, relwidth=0.2, relx=0.2, rely=0.8)

        self.exit_btn = Button(self.tab1, text="Выйти",
                         bg="Light gray",
                         fg="Black",
                         # font = ("Times New Roman"),
                         bd=2,
                         justify=CENTER,
                         heigh=2,
                         width=15,
                         command=exit
                         )
        self.exit_btn.place(relheight=0.1, relwidth=0.2, relx=0.6, rely=0.8)

        # В этой части добавляются элементы дополнительного меню
        self.score_ = Label(self.tab2, text='Заработано очков: 0',
                      # bg="Light gray",
                      fg="Black",
                      font=("Times new Roman", 15, "bold"),
                      bd=15,
                      justify=CENTER,
                      heigh=2,
                      width=15)
        self.score_.place(relheight=0.2, relwidth=0.4, relx=0.02, rely=0.05)

        self.count_of_game = Label(self.tab2, text='Игр сыграно: 0',
                             # bg="Light gray",
                             fg="Black",
                             font=("Times new Roman", 15, "bold"),
                             bd=15,
                             justify=CENTER,
                             heigh=2,
                             width=15)
        self.count_of_game.place(relheight=0.2, relwidth=0.4, relx=0.5, rely=0.05)

        self.reset_btn = Button(self.tab2, text="Сбросить статистику",
                          bg="Light gray",
                          fg="Black",
                          # font = ("Times New Roman"),
                          bd=2,
                          justify=CENTER,
                          heigh=2,
                          width=15,
                          command=self.reset
                          )
        self.reset_btn.place(relheight=0.1, relwidth=0.3, relx=0.35, rely=0.8)

        self.window.mainloop()

    def warning_log(self):
        self.status('Состояние - выключен')
        messagebox.showerror('Ошибка', 'Неверный логин или пароль!')

    def stat(self):
        self.score_.configure(text='Заработано очков: ' + str(function.total_score__))
        self.count_of_game.configure(text='Игр сыграно: ' + str(function.game_count__))

    def status(self, text):
        self.condition_of_bot.configure(text=text)

    def exit(self):
        try:
            main.driver.quit()
        except:
            pass
        self.window.destroy()

    def antifreeze(self):
        if (self.login_input.get() != '' and self.password_input.get() != '' and self.text_ == 'Состояние - выключен' and self.r_var.get() != 2) \
                or (self.login_input.get() != '' and self.text_ == 'Состояние - выключен' and self.r_var.get() == 2 and len(self.login_input.get()) >=3
        and len(self.login_input.get()) <= 12):
            proc = Thread(target=self.start_)
            proc.start()
        else:
            if self.login_input.get() == '':
                messagebox.showwarning('Ошибка', 'Введите логин!')
            elif self.password_input.get() == '' and self.r_var.get() != 2:
                messagebox.showwarning('Ошибка', 'Введите пароль!')
            elif self.r_var.get() == 2 and (len(self.login_input.get()) <3 or len(self.login_input.get()) > 12):
                messagebox.showwarning('Ошибка', 'Логин должен быть от 3х до 12 символов')
            else:
                messagebox.showwarning('Ошибка', 'Бот уже запущен!')

    def start_(self):
        global type_of_account, login_of_account, password_of_account
        type_of_account = self.r_var.get()
        login_of_account = self.login_input.get()
        password_of_account = self.password_input.get()
        self.status('Состояние - запущен')
        main.main()

    def reset(self):
        function.total_score__ = 0
        function.game_count__ = 0
        self.stat()


def gui():
    app = Main_menu()