from tkinter import *
from tkinter import messagebox


root = Tk()
root.title('Login')
root.geometry('924x500+300+200')
root.config(bg='#00ff00')
root.resizable(False, False)

img = PhotoImage(file='Picture3.png')
Label(root, image=img, bg='white').place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg='white')
frame.place(x=480, y=70)

heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white',
                font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

root.mainloop()
