import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("Example")
window.geometry("257x141")

dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto)
label1.grid(row=0, column=10)
label2 = tk.Label(window, text="Pochacco!")
label3 = tk.Label(window, text="A cuddly little puppy! This is from the same\ncreators who brought you Keropi and Kero Kero", background="#aaffff")

window.mainloop()