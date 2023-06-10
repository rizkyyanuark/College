import tkinter as tk
from tkinter import ttk

root = tk.Tk()
tree = ttk.Treeview(root)
tree["columns"] = ("one", "two")
tree.heading("one", text="Column A")
tree.heading("two", text="Column B")

# insert data
tree.insert("", "end", text="Row 1", values=("1A", "1B"))
tree.insert("", "end", text="Row 2", values=("2A", "2B"))
tree.insert("", "end", text="Row 3", values=("3A", "3B"))

# sort data
data = []
for child in tree.get_children():
    data.append((child, tree.item(child)["values"]))
data.sort(key=lambda x: x[1])
for i, item in enumerate(data):
    tree.move(item[0], "", i)

root.mainloop()
