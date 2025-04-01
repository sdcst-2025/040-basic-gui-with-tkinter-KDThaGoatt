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
entry2 = tk.Entry(window, width=17)
button2 = tk.Button(window,text="< Previous")
button3 = tk.Button(window, text="Save Entry", width=14, height=2)
button4 = tk.Button(window, text="Next >")
label4 = tk.Label(window, text="Type")
entry3 = tk.Entry(window, width=17)
label5 = tk.Label(window, text="Breed")
entry4 = tk.Entry(window, width=17)

label1.place(x=10, y=0)
entry1.place(x=500, y=0)
button1.place(x=400, y=0)
label2.place(x=250, y=50)
label3.place(x=35, y=105)
entry2.place(x=2, y=125)
button2.place(x=2, y=150)
button3.place(x=240, y=150)
button4.place(x=550, y=150)
label4.place(x=155, y=105)
entry3.place(x=120, y=125)
label5.place(x=275, y=105)
entry4.place(x=240, y=125)

window.mainloop()