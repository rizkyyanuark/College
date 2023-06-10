from openpyxl import Workbook
from openpyxl.drawing.image import Image
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Gambar di GUI")

wb = Workbook()
ws = wb.active

img = Image('Picture2.png')
ws.add_image(img, 'A1')

wb.save('example.xlsx')

img = Image.open('Picture2.png')
img = img.resize((250, 250), Image.ANTIALIAS)

img = ImageTk.PhotoImage(img)
panel = Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")

root.mainloop()
