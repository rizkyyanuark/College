import tkinter as tk
from tkinter import ttk
import openpyxl
from PIL import ImageTk, Image
import pandas as pd
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
import matplotlib.pyplot as plt

s = pd.read_csv('cancer patient data sets.csv')
s = s.values
x = s[:, 2:25]
y = s[:, 25]
kf = KFold(n_splits=10, random_state=0, shuffle=True)
print(kf)


def load_data(csv='cancer patient data sets.csv'):
    # Read the Excel file and create a DataFrame
    df = pd.read_csv(csv)

    list_values = list(df.values)
    df["Gender"].replace({1: 'male', 2: 'Female'}, inplace=True)
    for row in df.itertuples():
        # Insert the current row into the Treeview widget
        treeview.insert('', tk.END, values=row[2:5])


def insert_row():
    name = name_entry.get()
    age = int(age_spinbox.get())
    subscription_status = status_combobox.get()
    employment_status = "Employed" if a.get() else "Unemployed"

    print(name, age, subscription_status, employment_status)

# Insert row into Excel sheet
    path = "D:\codefirst.io\Tkinter Excel App\people.xlsx"
    workbook = openpyxl.load_workbook(path)
    sheet = workbook.active
    row_values = [name, age, subscription_status, employment_status]
    sheet.append(row_values)
    workbook.save(path)

# Insert row into treeview
    treeview.insert('', tk.END, values=row_values)

# Clear the values
    name_entry.delete(0, "end")
    name_entry.insert(0, "Name")
    age_spinbox.delete(0, "end")
    age_spinbox.insert(0, "Age")
    status_combobox.set(combo_list[0])
    checkbutton.state(["!selected"])


def knn():
    neigh2 = KNeighborsClassifier(n_neighbors=2, metric='euclidean')
    neigh2.fit(x, y)
    l = neigh2.predict(
        [[33, 1, 2, 4, 5, 4, 3, 2, 2, 4, 3, 2, 2, 4, 3, 4, 2, 2, 3, 1, 2, 3, 4]])
    m = neigh2.predict(
        [[17, 1, 3, 1, 5, 3, 4, 2, 2, 2, 2, 4, 2, 3, 1, 3, 7, 8, 6, 2, 1, 7, 2]])
    h = neigh2.predict(
        [[35, 1, 4, 5, 6, 5, 5, 4, 6, 7, 2, 3, 4, 8, 8, 7, 9, 2, 1, 4, 6, 7, 2]])
    train = neigh2.predict(
        [[13, 9, 9, 9, 6, 1, 6, 9, 6, 2, 5, 2, 2, 2, 3, 1, 1, 7, 9, 2, 1, 3, 2]])

    print(train[0])


def toggle_mode():
    if mode_switch.instate(["selected"]):
        style.theme_use("forest-light")
    else:
        style.theme_use("forest-dark")


root = tk.Tk()
root.title("Lung Cancer Diasese")
# root.geometry("950x700")
root.resizable(False, False)


icon = ImageTk.PhotoImage(Image.open("Picture3.png"))
root.iconphoto(False, icon)

root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)

style = ttk.Style(root)
root.tk.call("source", "forest-dark.tcl")
root.tk.call("source", "forest-light.tcl")
style.theme_use("forest-dark")

combo_list = ["Very Low", "low", "Below Average", 'Average',
              'Above Average', 'High', 'Very High', "Maximum", 'Peak']

combo_list8 = ["Very Low", "low", "Below Average", 'Average',
               'Above Average', 'High', 'Very High', "Maximum"]

combo_list7 = ["Very Low", "low", 'Average',
               'Above Average', 'High', 'Very High', "Maximum"]

main_frame = ttk.Frame(root)
main_frame.pack()

notebook = ttk.Notebook(main_frame)
notebook = ttk.Notebook(root)

tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

notebook.add(tab1, text='Tab 1')
notebook.add(tab2, text='Tab 2')

notebook.pack(expand=1, fill='both')

frame = ttk.Frame(tab1)
frame.pack()

biodata_row = ttk.LabelFrame(frame, text="Biodata Row")
biodata_row.grid(row=0, column=0, padx=20, pady=10)

complaint_row = ttk.LabelFrame(frame, text="Medical Complaints Row")
complaint_row.grid(row=1, column=0, padx=20, pady=10)

# hasil_row = ttk.LabelFrame(frame, text='hasil')
# hasil_row.grid(row=1, column=1, padx=20, pady=10)

# hasil_row = ttk.LabelFrame(frame, text="Medical Complaints Row")
# hasil_row.grid(row=1, column=1, padx=20, pady=10)


name_entry = ttk.Entry(biodata_row)
name_entry.insert(0, "Name")
name_entry.bind("<FocusIn>", lambda e: name_entry.delete('0', 'end'))
name_entry.grid(row=0, column=0, padx=10, pady=(20, 20), sticky="ew")

# label = ttk.Label(tab1, text='Hasil')
# label.grid(row=0, column=0,)
# tombol = ttk.Button(tab1, text='tekan buat hasil')
# tombol.grid(row=1, column=0)


label = ttk.Label(complaint_row, text='Air Pollution')
label.grid(row=0, column=0,)
label = ttk.Label(complaint_row, text='Alcohol use')
label.grid(row=0, column=1)
label = ttk.Label(complaint_row, text='Dust Allergy')
label.grid(row=0, column=2)
label = ttk.Label(complaint_row, text='OccuPational Hazards')
label.grid(row=0, column=3)

label = ttk.Label(complaint_row, text='Genetic Risk')
label.grid(row=2, column=0)
label = ttk.Label(complaint_row, text='Chronic Lung Disease')
label.grid(row=2, column=1)
label = ttk.Label(complaint_row, text='Balanced Diet')
label.grid(row=2, column=2)
label = ttk.Label(complaint_row, text='Obesity')
label.grid(row=2, column=3)

label = ttk.Label(complaint_row, text='Smoking')
label.grid(row=4, column=0)
label = ttk.Label(complaint_row, text='Passive Smoker')
label.grid(row=4, column=1)
label = ttk.Label(complaint_row, text='Chest Pain')
label.grid(row=4, column=2)
label = ttk.Label(complaint_row, text='Coughing of Blood')
label.grid(row=4, column=3)

label = ttk.Label(complaint_row, text='Fatigue')
label.grid(row=6, column=0)
label = ttk.Label(complaint_row, text='Weight Loss')
label.grid(row=6, column=1)
label = ttk.Label(complaint_row, text='Shortness of Breath')
label.grid(row=6, column=2)
label = ttk.Label(complaint_row, text='Wheezing')
label.grid(row=6, column=3)

label = ttk.Label(complaint_row, text='Swallowing DIfficulty')
label.grid(row=8, column=0)
label = ttk.Label(complaint_row, text='Clubbing of Finger Nails')
label.grid(row=8, column=1)
label = ttk.Label(complaint_row, text='Frequent Cold')
label.grid(row=8, column=2)
label = ttk.Label(complaint_row, text='Dry Cough')
label.grid(row=8, column=3)

label = ttk.Label(complaint_row, text='Snoring')
label.grid(row=10, column=1, columnspan=2)
# label = ttk.Label(complaint_row, text='Genetic Risk')
# label.grid(row=15, column=1)

alamat_entry = ttk.Entry(biodata_row)
alamat_entry.insert(0, "Address")
alamat_entry.bind("<FocusIn>", lambda e: alamat_entry.delete('0', 'end'))
alamat_entry.grid(row=0, column=2, padx=10, pady=(20, 20), sticky="ew")

phone_entry = ttk.Entry(biodata_row)
phone_entry.insert(0, "Phone Number")
phone_entry.bind("<FocusIn>", lambda e: phone_entry.delete('0', 'end'))
phone_entry.grid(row=3, column=0, padx=10, pady=(20, 20), sticky="ew")

age_spinbox = ttk.Spinbox(biodata_row, from_=18, to=100)
age_spinbox.insert(0, "Age")
age_spinbox.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

######### segment combo cox#############
status_combobox = ttk.Combobox(
    complaint_row, state='readonly', values=combo_list, width=10)
status_combobox.current(0)
status_combobox.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

status_combobox = ttk.Combobox(
    complaint_row, state='readonly', values=combo_list, width=10)
status_combobox.current(0)
status_combobox.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

status_combobox = ttk.Combobox(
    complaint_row, state='readonly', values=combo_list, width=10)
status_combobox.current(0)
status_combobox.grid(row=1, column=2, padx=10, pady=5, sticky="ew")

status_combobox = ttk.Combobox(
    complaint_row, state='readonly', values=combo_list, width=10)
status_combobox.current(0)
status_combobox.grid(row=1, column=3, padx=10, pady=5, sticky="ew")

status_combobox = ttk.Combobox(
    complaint_row, state='readonly', values=combo_list, width=10)
status_combobox.current(0)
status_combobox.grid(row=3, column=0, padx=10, pady=5, sticky="ew")

status_combobox = ttk.Combobox(
    complaint_row, state='readonly', values=combo_list, width=10)
status_combobox.current(0)
status_combobox.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

status_combobox = ttk.Combobox(
    complaint_row, state='readonly', values=combo_list, width=10)
status_combobox.current(0)
status_combobox.grid(row=3, column=2, padx=10, pady=5, sticky="ew")

status_combobox = ttk.Combobox(
    complaint_row, state='readonly', values=combo_list, width=10)
status_combobox.current(0)
status_combobox.grid(row=3, column=3, padx=10, pady=5, sticky="ew")

status_combobox = ttk.Combobox(
    complaint_row, state='readonly', values=combo_list, width=10)
status_combobox.current(0)
status_combobox.grid(row=5, column=0, padx=10, pady=5, sticky="ew")

status_combobox = ttk.Combobox(
    complaint_row, state='readonly', values=combo_list, width=10)
status_combobox.current(0)
status_combobox.grid(row=5, column=1, padx=10, pady=5, sticky="ew")

status_combobox = ttk.Combobox(
    complaint_row, state='readonly', values=combo_list, width=10)
status_combobox.current(0)
status_combobox.grid(row=5, column=2, padx=10, pady=5, sticky="ew")

status_combobox = ttk.Combobox(
    complaint_row, state='readonly', values=combo_list, width=10)
status_combobox.current(0)
status_combobox.grid(row=5, column=3, padx=10, pady=5, sticky="ew")

status_combobox = ttk.Combobox(
    complaint_row, state='readonly', values=combo_list, width=10)
status_combobox.current(0)
status_combobox.grid(row=7, column=0, padx=10, pady=5, sticky="ew")

status_combobox = ttk.Combobox(
    complaint_row, state='readonly', values=combo_list, width=10)
status_combobox.current(0)
status_combobox.grid(row=7, column=1, padx=10, pady=5, sticky="ew")

status_combobox = ttk.Combobox(
    complaint_row, state='readonly', values=combo_list, width=10)
status_combobox.current(0)
status_combobox.grid(row=7, column=2, padx=10, pady=5, sticky="ew")

status_combobox = ttk.Combobox(
    complaint_row, state='readonly', values=combo_list, width=10)
status_combobox.current(0)
status_combobox.grid(row=7, column=3, padx=10, pady=5, sticky="ew")

status_combobox = ttk.Combobox(
    complaint_row, state='readonly', values=combo_list, width=10)
status_combobox.current(0)
status_combobox.grid(row=9, column=0, padx=10, pady=5, sticky="ew")

status_combobox = ttk.Combobox(
    complaint_row, state='readonly', values=combo_list, width=10)
status_combobox.current(0)
status_combobox.grid(row=9, column=1, padx=10, pady=5, sticky="ew")

status_combobox = ttk.Combobox(
    complaint_row, state='readonly', values=combo_list, width=10)
status_combobox.current(0)
status_combobox.grid(row=9, column=2, padx=10, pady=5, sticky="ew")

status_combobox = ttk.Combobox(
    complaint_row, state='readonly', values=combo_list, width=10)
status_combobox.current(0)
status_combobox.grid(row=9, column=3, padx=10, pady=5, sticky="ew")

status_combobox = ttk.Combobox(
    complaint_row, state='readonly', values=combo_list, width=10)
status_combobox.current(0)
status_combobox.grid(row=11, column=1, columnspan=2,
                     padx=10, pady=5, sticky="ew")


a = tk.BooleanVar()
checkbutton = ttk.Checkbutton(
    biodata_row, text="Terms&Conditions", variable=a)
checkbutton.grid(row=6, column=0, padx=5, pady=5, sticky="nsew")

# checkbutton = ttk.Checkbutton(biodata_row, text="Employed", variable=a)
# checkbutton.grid(row=7, column=2, padx=10, pady=10, sticky="nsew")

button = ttk.Button(biodata_row, text="Insert", command=insert_row)
button.grid(row=8, column=0, padx=5, pady=5, sticky="nsew")

separator = ttk.Separator(biodata_row)
separator.grid(row=9, column=0, padx=(20, 10), pady=10, sticky="ew")

mode_switch = ttk.Checkbutton(
    biodata_row, text="Mode", style="Switch", command=toggle_mode)
mode_switch.grid(row=10, column=0, padx=5, pady=10, sticky="nsew")

treeFrame = ttk.Frame(frame)
treeFrame.grid(row=0, column=1, pady=10)

treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side="right", fill="y")

cols = ("Patient Id", "Age", "Gender", "Level")
treeview = ttk.Treeview(treeFrame, show="headings",
                        yscrollcommand=treeScroll.set, columns=cols, height=13)
treeview.heading('#1', text='Patient Id')
treeview.heading('#2', text='Age')
treeview.heading('#3', text='Gender')
treeview.heading('#4', text='Level')
treeview.column('Patient Id', width=50)
treeview.column('Age', width=50)
treeview.column('Gender', width=50)
treeview.column('Level', width=50)

treeview.pack()
treeScroll.config(command=treeview.yview)
load_data()

root.update()
root.minsize(root.winfo_width(), root.winfo_height())
x_cordinate = int((root.winfo_screenwidth()/2) - (root.winfo_width()/2))
y_cordinate = int((root.winfo_screenheight()/2) - (root.winfo_height()/2))
root.geometry("+{}+{}".format(x_cordinate, y_cordinate))

root.mainloop()
