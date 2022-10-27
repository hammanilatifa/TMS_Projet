from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
from PIL import  ImageTk, Image
import time

class UploadCSV():
    def __init__(self, window):
        self.window = window
        self.window.config(background='white')
        self.window.title("Transport Management System")
        self.window.geometry("720x480")
        self.window.minsize(480, 360)
        self.label = Label(window, text="Vous devez choisir un fichier CSV", font=("Courrier", 12))
        self.label.pack(pady=20)
        #image
        """self.frame0 = Frame(window)
        self.logo1 = PhotoImage(file="CSVfile.png")
        self.w1 = Label(self.frame0, image=self.logo1, width=290, height=290).pack(side="left", padx=15, expand=YES)
        self.frame0.pack(pady=10)"""

        frame = Frame(window, width=600, height=400)
        frame.pack()
        frame.place(anchor='center', relx=0.5, rely=0.5)
        # Create an object of tkinter ImageTk
        img = ImageTk.PhotoImage(Image.open("Logo.png"))

        # Create a Label Widget to display the text or Image
        label = Label(frame, image = img)
        label.pack()

        #llllllllllllllll
        
        self.greet_button = Button(window, text="Choisir le fichier", command=self.open_file)
        self.greet_button.pack()

        self.label1 = Label(window, text="", font=("Courrier", 17))
        self.label1.pack(pady=20)
        
        self.frame = Frame(window)
        self.frame.pack(pady=40)


    def open_file(self):
        file_path = askopenfile(mode='r', filetypes=[('CSV Files', '*.csv')])
        if file_path is not None:
            titlee = Label(self.frame, text='Fichier téléchargé avec succès !', foreground='green',font=("Courrier", 13))
            titlee.pack()
            print(file_path)


 


