import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("Example")
window.geometry("257x141")

dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto)
label2 = tk.Label(window, text="Pochacco!")
label3 = tk.Label(window, text="A cuddly little puppy! This is from the same\ncreators who brought you Keropi and Kero Kero", background="#aaffff")

label1.place(x=75, y=5)
label2.place(x=145, y=40)
label3.place(x=0, y=105)

window.mainloop()