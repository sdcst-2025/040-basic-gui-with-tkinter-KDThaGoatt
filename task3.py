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

label1.grid(row=0, column=0, padx=0, pady=0, sticky=tk.E)
label2.grid(row=0, column=1, padx=0, pady=0,sticky=tk.W)
label3.grid(row=2, column=0, columnspan=2, padx=0, pady=5)

window.mainloop()