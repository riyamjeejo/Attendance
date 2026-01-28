import tkinter as tk
from tkinter import messagebox

# Create Login Funtion
def validate_login():
    user = username_entry.get()
    pwd  = password_entry.get()

    if user == "admin" and pwd == "password":
        messagebox.showinfo("Login Status", "Login Successful!")
    else:
        messagebox.showerror("Login Status", "Invalid username or password")

# Create the main window
root = tk.Tk()
root.title("Simple Log App")
root.geometry("1000x500")

# Create label for entry and username
tk.Label(root, text="Username:").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack()

#Create laber for entry and password
tk.Label(root, text="Password:").pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Create Login Button
tk.Button(root, text="Login", command=validate_login).pack(pady=10)

# To Run
root.mainloop()
