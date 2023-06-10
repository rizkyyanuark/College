import tkinter as tk
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(text):
    # Create a PDF document
    doc = SimpleDocTemplate("output.pdf", pagesize=letter)

    # Set the style for the text
    styles = getSampleStyleSheet()
    style = styles["Normal"]

    # Add the text to the PDF document
    story = [Paragraph(text, style)]
    doc.build(story)


def on_button_click():
    # Get the text from the text widget
    text = text_widget.get("1.0", tk.END)

    # Create a PDF file from the text
    create_pdf(text)


# Create the main window
root = tk.Tk()

# Create a text widget
text_widget = tk.Text(root)
text_widget.pack()

# Create a button widget
button = tk.Button(root, text="Create PDF", command=on_button_click)
button.pack()

# Run the main loop
root.mainloop()
