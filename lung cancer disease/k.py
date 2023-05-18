import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

root = tk.Tk()

fig = Figure(figsize=(5, 4), dpi=100)
t = [0, 1, 2, 3, 4]
s = [0, 1, 4, 9, 16]
ax = fig.add_subplot(111)
ax.plot(t, s)

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

tk.mainloop()
