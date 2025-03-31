import tkinter as tk
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")
window.geometry("600x200")

dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(window, image=dogphoto)
entry1 = tk.Entry(window, width=15)
button1 = tk.Button(window, text="Search by Name", width=12)
label2 = tk.Label(window, text="Client Database")
label3 = tk.Label(window, text="Name")
entry2 = tk.Entry(window, width=14)
button2 = tk.Button(window,text="< Previous")

label1.place(x=10, y=0)
entry1.place(x=500, y=0)
button1.place(x=400, y=0)
label2.place(x=250, y=50)
label3.place(x=25, y=105)
entry2.place(x=2, y=125)
button2.place(x=2, y=150)

window.mainloop()