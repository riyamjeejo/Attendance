import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Log App")
root.geometry("1000x500")

# Create a label widget
label = tk.Label(root, text="Hello, World!")
label.pack(pady=10)

# Function to run when button is clicked
def on_button_click():
    label.config(text="Button was clicked!")

# Create a button widget
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
   