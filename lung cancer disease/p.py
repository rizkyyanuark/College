import tkinter as tk
from tkinter import ttk

import tkinter.messagebox as messagebox


import tkinter as tk
import pandas as pd
from tkinter import ttk


def on_click(event):
    item = tree.item(tree.focus())
    popup = tk.Toplevel(root)
    popup.geometry("200x200")
    label = tk.Label(popup, text=item["text"])
    label.pack()
    for key in item:
        if key != "text":
            sub_label = tk.Label(popup, text=f"{key}: {item[key]}")
            sub_label.pack()


root = tk.Tk()

tree = ttk.Treeview(root)
tree.pack()

tree["columns"] = ("one", "two")
tree.column("#0", width=100)
tree.column("one", width=100)
tree.column("two", width=100)

tree.heading("#0", text="Nama")
tree.heading("one", text="Alamat")
tree.heading("two", text="Telepon")

df = pd.read_excel("data.xlsx")
for index, row in df.iterrows():
    tree.insert("", "end", text=row["Nama"],
                values=(row["Alamat"], row["Telepon"]))

tree.bind("<Double-1>", on_click)

root.mainloop()
