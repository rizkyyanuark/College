import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from tkinter import *

# Create the window
window = Tk()

# Create the label
label = Label(window, text="KNN Classification")
label.pack()

# Create the entry box for the number of neighbors
entry_box = Entry(window)
entry_box.pack()

# Create the button to classify the data
button = Button(window, text="Classify", command=classify)
button.pack()

# Create the canvas to display the data
canvas = Canvas(window, width=600, height=400)
canvas.pack()

# Load the training data
X_train = np.loadtxt("train.csv", delimiter=",")
y_train = np.loadtxt("train_labels.csv", delimiter=",")

# Create the KNN classifier
clf = KNeighborsClassifier(n_neighbors=int(entry_box.get()))

# Fit the classifier to the training data
clf.fit(X_train, y_train)

# Create a function to classify the data


def classify():
    # Get the data from the entry box
    data = np.array([float(x) for x in entry_box.get().split(",")])

    # Predict the label for the data
    label = clf.predict([data])

    # Draw the data on the canvas
    canvas.create_oval(data[0] - 10, data[1] - 10,
                       data[0] + 10, data[1] + 10, fill="red")
    canvas.create_text(data[0], data[1], text=label)


# Start the event loop
window.mainloop()
