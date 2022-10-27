from tkinter import *
import sqlite3
from tkinter import messagebox

class Login():
    np = "hhhhh"
    page="Login"
    def __init__(self, window):
        self.window = window
        window.config(background='white')
        self.frame00 = Frame(window, bg='white')
        self.logo1 = PhotoImage(file="login.png")
        self.im = Label(self.frame00, image=self.logo1, width=128, height=128,bg='white').pack( pady=15, expand=YES)
        self.frame00.pack(pady=15)
        self.frame0 = Frame(window, bg='white')
        title = Label(self.frame0, text="Saisir votre Login:", font=("Courrier", 13), bg='white').grid(row=1, column=1,                                                                                               pady=8)
        self.login = StringVar()
        textbox = Entry(self.frame0, textvariable=self.login, font=("Helvetica", 13), border=1, bg='white', fg='black',
                        width=18).grid(row=1, column=2, pady=8)

        title = Label(self.frame0, text="Saisir votre mot de passe:", font=("Courrier", 13), bg='white').grid(row=2,
                                                                                                              column=1,
                                                                                                              pady=8)
        self.password = StringVar()
        textbox = Entry(self.frame0, textvariable=self.password, show="*", font=("Helvetica", 13), border=1, bg='white',
                        fg='black',
                        width=18).grid(row=2, column=2, pady=8)
        frame3 = Frame(window, bg='white')
        self.button = Button(frame3, text="Valider 'Ajout'", command=self.connectAjout, border=0, font=("Courrier", 13),
                             bg='#FF0000',
                             fg='white', width=25)
        self.button.pack(pady=2)
        self.button = Button(frame3, text="Valider 'Analyse'", command=self.connectAnalyse, border=0, font=("Courrier", 13),
                             bg='#FF0000',
                             fg='white', width=25)
        self.button.pack()
        self.frame0.pack(pady=10)

        lbl = Label(frame3, text=r"Je suis pas un Admin ??", fg="blue", bg='white', cursor="hand2")
        lbl.configure(font="Verdana 10 underline")
        lbl.pack()
        frame3.pack(pady=15)
        lbl.bind("<Button-1>", self.command)


    