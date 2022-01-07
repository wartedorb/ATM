import tkinter as tk
import time


class Atm:
    """

    """
    password_symbols = []
    money_symbols = []
    possibility = False
    money = 322.00

    def __init__(self):
        self.win = tk.Tk()
        self.win.geometry('1600x900+0+0')
        self.page_load = tk.PhotoImage(file='Start_Page.png')
        self.choice_page_load = tk.PhotoImage(file='Choice_Page.png')
        self.page_fail_load = tk.PhotoImage(file='Wrong_Password_Page.png')
        self.screen_btn1 = tk.PhotoImage(file='Balance_Screen.png')
        self.balance_loader = tk.PhotoImage(file='Wallet_Page.png')
        self.back_screen_load = tk.PhotoImage(file='Back_Screen_Button.png')
        self.wallet_screen = tk.PhotoImage(file='money_screen.png')
        self.bgl = tk.PhotoImage(file='bg.png')

        self.balance_sheet_load = tk.PhotoImage(file='Balance_place.png')

        self.screen_btn2 = tk.PhotoImage(file='Exit_Screen_Button.png')
        self.screen_btn3 = tk.PhotoImage(file='Outmoney.png')
        self.screen_btn4 = tk.PhotoImage(file='inp_scrn.png')
        self.screen_btn_next = tk.PhotoImage(file='Next_Screen.png')

        self.crd_l = tk.PhotoImage(file='card.png')
        self.bge_l = tk.PhotoImage(file='bgofa.png')
        # self.card_p = tk.Canvas(self.win, width=100, height=200, bg='red')

        self.insert_l = tk.PhotoImage(file='insert_card.png')

        self.bg = tk.Label(image=self.bgl)
        self.money_out = tk.Label(image=self.wallet_screen,
                                  bg='black')
        self.page_fail = tk.Label(image=self.page_fail_load,
                                  bg='black')
        self.page = tk.Label(image=self.page_load,

                             bg='black')
        self.page_choice = tk.Label(image=self.choice_page_load,

                                    bg='black'
                                    )
        self.page_balance = tk.Label(image=self.balance_loader)

        self.warning_lbl = tk.Label(font='Calibri 20',
                                    bd=0,
                                    bg='#7a85f6',
                                    text='Сумма не должна быть больше 30000.00₽',
                                    fg='black')

        self.balance_sheet = tk.Label(font='Calibri 48',
                                      bd=0,
                                      bg='#7a85f6',
                                      text=str(Atm.money) + '₽',
                                      fg='black')

        self.s_btn1 = tk.Button(self.win,
                                bd=0,
                                bg='#13b7e1',
                                activebackground='#13b7e1',
                                relief='flat',
                                cursor='cross',
                                image=self.screen_btn1,
                                command=lambda: self.balance_page())

        self.s_btn2 = tk.Button(self.win,
                                bd=0,
                                bg='#13b7e1',
                                activebackground='#13b7e1',
                                relief='flat',
                                cursor='cross',
                                image=self.screen_btn2,
                                command=lambda: self.exit())

        self.s_btn3 = tk.Button(self.win,
                                bd=0,
                                bg='#13b7e1',
                                activebackground='#13b7e1',
                                relief='flat',
                                cursor='cross',
                                image=self.screen_btn3,
                                command=lambda: self.money_page()
                                )

        self.s_btn4 = tk.Button(self.win,
                                image=self.screen_btn4,
                                bd=0,
                                bg='#13b7e1',
                                activebackground='#13b7e1',
                                relief='flat',
                                cursor='cross',
                                command=lambda: self.money_page_2())

        self.enter_money_out = tk.Entry(self.win,
                                        bd=0,
                                        bg='#13b7e1',
                                        font='Calibri 48',
                                        width=7,
                                        )

        self.enter_money_in = tk.Entry(self.win,
                                       bd=0,
                                       bg='#13b7e1',
                                       font='Calibri 48',
                                       width=7,
                                       )
        self.insert_button = tk.Button(self.win,
                                       image=self.insert_l,
                                       bd=0,
                                       highlightthickness=0,
                                       relief='flat',
                                       cursor='cross',
                                       command=lambda: self.card_animation('in'))

        self.s_next = tk.Button(self.win,
                                image=self.screen_btn_next,
                                bd=0,
                                bg='#7a85f6',
                                activebackground='#7a85f6',
                                relief='flat',
                                cursor='cross',
                                command=lambda: self.check_money())

        self.s_next_2 = tk.Button(self.win,
                                  image=self.screen_btn_next,
                                  bd=0,
                                  bg='#7a85f6',
                                  activebackground='#7a85f6',
                                  relief='flat',
                                  cursor='cross',
                                  command=lambda: self.check_money_2())

        self.s_back = tk.Button(self.win,
                                image=self.back_screen_load,
                                bd=0,
                                bg='#13b7e1',
                                activebackground='#13b7e1',
                                relief='flat',
                                cursor='cross',
                                command=lambda: self.choice_page())

        self.btn1 = tk.Button(self.win,
                              text='1',
                              width=2,
                              command=lambda: self.button_input(1, 'pwd'))

        self.btn2 = tk.Button(self.win,
                              text='2',
                              width=2,
                              command=lambda: self.button_input(2, 'pwd'))

        self.btn3 = tk.Button(self.win,
                              text='3',
                              width=2,
                              command=lambda: self.button_input(3, 'pwd'))

        self.btn4 = tk.Button(self.win,
                              text='4',
                              width=2,
                              command=lambda: self.button_input(4, 'pwd'))

        self.btn5 = tk.Button(self.win,
                              text='5',
                              width=2,
                              command=lambda: self.button_input(5, 'pwd'))

        self.btn6 = tk.Button(self.win,
                              text='6',
                              width=2,
                              command=lambda: self.button_input(6, 'pwd'))

        self.btn7 = tk.Button(self.win,
                              text='7',
                              width=2,
                              command=lambda: self.button_input(7, 'pwd'))

        self.btn8 = tk.Button(self.win,
                              text='8',
                              width=2,
                              command=lambda: self.button_input(8, 'pwd'))

        self.btn9 = tk.Button(self.win,
                              text='9',
                              width=2,
                              command=lambda: self.button_input(9, 'pwd'))

        self.enter = tk.Entry(self.win,
                              width=13)

        self.__state_of_window = True

        self.balance_objects = [self.s_back, self.page_balance, self.balance_sheet]

        self.money_out_objects = [self.s_next, self.money_out, self.enter_money_out, self.warning_lbl]

        self.money_in_objects = [self.money_out, self.s_next_2, self.enter_money_in]

        self.buttons = [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6, self.btn7,
                        self.btn8, self.btn9]

    def balance_page(self):
        self.s_btn1.place_forget()
        self.s_btn2.place_forget()
        self.s_btn3.place_forget()
        self.s_btn4.place_forget()
        self.s_back.place(x=253, y=103)
        self.balance_sheet['text'] = str(Atm.money) + ' ₽'
        self.balance_sheet.place(x=490, y=400)
        self.page_balance.place(x=250, y=100)

    def button_refactor(self, where):
        if where == 'first':
            self.btn1['command'] = lambda: self.button_input(1, 'pwd')
            self.btn2['command'] = lambda: self.button_input(2, 'pwd')
            self.btn3['command'] = lambda: self.button_input(3, 'pwd')
            self.btn4['command'] = lambda: self.button_input(4, 'pwd')
            self.btn5['command'] = lambda: self.button_input(5, 'pwd')
            self.btn6['command'] = lambda: self.button_input(6, 'pwd')
            self.btn7['command'] = lambda: self.button_input(7, 'pwd')
            self.btn8['command'] = lambda: self.button_input(8, 'pwd')
            self.btn9['command'] = lambda: self.button_input(9, 'pwd')
        elif where == 'in':
            self.btn1['command'] = lambda: self.button_input(1, 'in')
            self.btn2['command'] = lambda: self.button_input(2, 'in')
            self.btn3['command'] = lambda: self.button_input(3, 'in')
            self.btn4['command'] = lambda: self.button_input(4, 'in')
            self.btn5['command'] = lambda: self.button_input(5, 'in')
            self.btn6['command'] = lambda: self.button_input(6, 'in')
            self.btn7['command'] = lambda: self.button_input(7, 'in')
            self.btn8['command'] = lambda: self.button_input(8, 'in')
            self.btn9['command'] = lambda: self.button_input(9, 'in')
        else:
            self.btn1['command'] = lambda: self.button_input(1, 'out')
            self.btn2['command'] = lambda: self.button_input(2, 'out')
            self.btn3['command'] = lambda: self.button_input(3, 'out')
            self.btn4['command'] = lambda: self.button_input(4, 'out')
            self.btn5['command'] = lambda: self.button_input(5, 'out')
            self.btn6['command'] = lambda: self.button_input(6, 'out')
            self.btn7['command'] = lambda: self.button_input(7, 'out')
            self.btn8['command'] = lambda: self.button_input(8, 'out')
            self.btn9['command'] = lambda: self.button_input(9, 'out')

    def exit(self):
        self.button_refactor('first')
        self.s_btn1.place_forget()
        self.s_btn2.place_forget()
        self.s_btn3.place_forget()
        self.s_btn4.place_forget()
        self.page_choice.place_forget()
        self.page.place(x=250, y=100)
        self.card_animation('out')

    def choice_page(self):
        for el in self.balance_objects:
            el.place_forget()
        for el in self.money_out_objects:
            el.place_forget()
        for el in self.money_in_objects:
            el.place_forget()
        self.page_choice.place(x=250, y=100)
        self.s_btn1.place(x=750, y=201)
        self.s_btn2.place(x=750, y=435)
        self.s_btn3.place(x=300, y=201)
        self.s_btn4.place(x=300, y=435)

    def money_page(self):
        self.button_refactor('out')
        self.page_choice.place_forget()
        self.s_btn1.place_forget()
        self.s_btn2.place_forget()
        self.s_btn3.place_forget()
        self.s_btn4.place_forget()
        self.money_out.place(x=250, y=100)
        self.s_back.place(x=253, y=103)
        self.enter_money_out.place(x=470, y=370)
        self.warning_lbl.place(x=360, y=455)
        self.s_next.place(x=670, y=360)

    def money_page_2(self):
        self.button_refactor('in')
        self.page_choice.place_forget()
        self.s_btn1.place_forget()
        self.s_btn2.place_forget()
        self.s_btn3.place_forget()
        self.s_btn4.place_forget()
        self.enter_money_in.place(x=470, y=370)
        self.money_out.place(x=250, y=100)
        self.s_back.place(x=253, y=103)
        self.s_next_2.place(x=670, y=360)

    def check_password(self):
        if Atm.password_symbols == [4, 2, 5, 9]:
            self.page_fail.place_forget()
            self.page.place_forget()
            self.choice_page()
            Atm.password_symbols.clear()
            self.enter.delete(0, 'end')
            print('ВЕРНО')
            Atm.possibility = False
        else:
            self.page.place_forget()
            self.page_fail.place(x=250, y=100)
            print('НЕВЕРНО')
            Atm.password_symbols.clear()
            self.enter.delete(0, 'end')

    def check_money(self):
        try:
            s = float(self.enter_money_out.get())
            if 0 < s <= 30000.00:
                if s <= Atm.money:
                    Atm.money -= s
                    self.enter_money_out.delete(0, 'end')
                    self.choice_page()
                    self.button_refactor('first')
                else:
                    self.enter_money_out.delete(0, 'end')
            else:
                self.enter_money_out.delete(0, 'end')
        except ValueError:
            self.enter_money_out.delete(0, 'end')

    def check_money_2(self):
        try:
            s = float(self.enter_money_in.get())
            if 0 < s:
                Atm.money += s
                self.enter_money_in.delete(0, 'end')
                self.choice_page()
                self.button_refactor('first')
            else:
                self.enter_money_in.delete(0, 'end')
        except ValueError:
            self.enter_money_in.delete(0, 'end')

    def place(self):
        self.bg.place(x=0, y=0)
        self.btn1.place(x=80, y=400)
        self.btn2.place(x=108, y=400)
        self.btn3.place(x=136, y=400)
        self.btn4.place(x=80, y=430)
        self.btn5.place(x=108, y=430)
        self.btn6.place(x=136, y=430)
        self.btn7.place(x=80, y=460)
        self.btn8.place(x=108, y=460)
        self.btn9.place(x=136, y=460)
        self.page.place(x=250, y=100)
        self.enter.place(x=79, y=379)
        self.insert_button.place(x=50, y=712)

    def card_animation(self, where):
        if where == 'in':
            self.insert_button.place_forget()
            self.card_p = tk.Canvas(self.win, width=100, height=200, bd=0, highlightthickness=0)
            self.card_p.place(x=65, y=505)
            back = self.card_p.create_image(50, 112, image=self.bge_l)
            card = self.card_p.create_image(52, 102, image=self.crd_l)
            for i in range(100):
                self.card_p.move(card, 0, -1)
                self.win.update()
                time.sleep(0.005)
            Atm.possibility = True

        elif where == 'out':
            self.insert_button.place(x=50, y=712)
            self.card_p = tk.Canvas(self.win, width=100, height=200, bd=0, highlightthickness=0)
            self.card_p.place(x=65, y=505)
            back = self.card_p.create_image(50, 112, image=self.bge_l)
            card = self.card_p.create_image(52, 2, image=self.crd_l)
            for i in range(100):
                self.card_p.move(card, 0, 1)
                self.win.update()
                time.sleep(0.005)
            Atm.possibility = False

    def add_money(self, digit, page):
        if page == 1:
            self.enter_money_out.insert(len(self.enter_money_out.get()), digit)
        elif page == 2:
            self.enter_money_in.insert(len(self.enter_money_in.get()), digit)

    def button_input(self, digit, none):
        if Atm.possibility and none == 'pwd':
            self.page.place(x=250, y=100)
            Atm.password_symbols.append(digit)
            self.page_fail.place_forget()
            if len(Atm.password_symbols) == 4 and Atm.possibility:
                self.enter.insert(len(self.enter.get()), '*')
                self.check_password()
            else:
                self.enter.insert(len(self.enter.get()), '*')
        elif none == 'in':
            self.add_money(digit, 2)
        elif none == 'out':
            self.add_money(digit, 1)


if __name__ == '__main__':
    win = Atm()
    win.place()
    win.win.mainloop()
