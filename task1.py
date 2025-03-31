import tkinter as tk

window = tk.Tk()
window.title("tk")
window.geometry("400x35")

entry1 = tk.Entry(window, width = 17)
label1 = tk.Label(window, text="x")
entry2 = tk.Entry(window, width = 17)
button1 = tk.Button(window, text="=")
label2 = tk.Label(window, width = 26, borderwidth=2, relief="groove")

entry1.pack(side="left")
label1.pack(side="left")
entry2.pack(side="left")
button1.pack(side="left")
label2.pack(side="left")


window.mainloop()