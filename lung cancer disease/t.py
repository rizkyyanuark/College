import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

notebook.add(frame1, text="Frame 1")
notebook.add(frame2, text="Frame 2")

button1 = tk.Button(frame1, text="Button 1")
button2 = tk.Button(frame1, text="Button 2")

button1.grid(row=0, column=0)
button2.grid(row=0, column=1)

root.mainloop()
