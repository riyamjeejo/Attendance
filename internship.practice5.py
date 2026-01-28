import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime

filename = "check_out.csv"

with open(filename, "a", newline="") as f:
    pass

# --LOGIN LOGIC --

def validate_login():
    user = username_entry.get()
    pwd  = password_entry.get()

    if user == "admin" and pwd == "password":
        messagebox.showinfo("Login Status", "Login Successful!")
        # hide login, show main
        login_frame.pack_forget()
        main_frame.pack(fill="both", expand=True)
    else:
        messagebox.showerror("Login Status", "Invalid username or password")

# --CHECK-IN/OUT LOGIC--

def check_in():
    name = name_entry.get().strip()
    if not name:
        messagebox.showwarning("Input Error", "Enter a name to check in")
        return
    
    check_in_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, check_in_time, ""])
    messagebox.showinfo("Checked In", f"{name} checked in at {check_in_time}")
    name_entry.delete(0, tk.END)

def check_out():
    name = name_entry.get().strip()
    if not name:
        messagebox.showwarning("Input Error", "Enter a name to check out")
        return
    
    check_out_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    rows = []
    found = False

    with open(filename, mode="r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == name and row[2] == "":
                row[2] = check_out_time
                found = True
            rows.append(row)

    if found:
        with open(filename, mode="w", newline="") as file: 
            writer = csv.writer(file)
            writer.writerows(rows)
        messagebox.showinfo("Checked Out", f"{name} checked out at {check_out_time}")
    else:
        messagebox.showwarning("No Check-In", "No active check-in found!")
    name_entry.delete(0, tk.END)


def show_all():
    output_text.delete("1.0", tk.END)
    with open(filename, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        output_text.insert(tk.END, "NAME\tCHECK-IN\tCHECK-OUT\n")
        for row in reader:
            output_text.insert(
                tk.END,
                f"{row[0]}\t{row[1]}\t{row[2]}\n"
            )

def logout():
    main_frame.pack_forget()
    login_frame.pack()

# --UI SETUP--

root = tk.Tk()
root.title("Login then Check-In/Check-Out App")
root.geometry("700x500")

# --Login Screen--

login_frame = tk.Frame(root)
login_frame.pack(fill="both", expand=True)

tk.Label(login_frame, text="Username:").pack(pady=5)
username_entry = tk.Entry(login_frame)
username_entry.pack()

tk.Label(login_frame, text="Password:").pack(pady=5)
password_entry = tk.Entry(login_frame, show="*")
password_entry.pack()

tk.Button(login_frame, text="Login", command=validate_login).pack(pady=10)

# --Main Check-In Screen--

main_frame = tk.Frame(root)

tk.Label(main_frame, text="Enter Name:").pack(pady=5)
name_entry = tk.Entry(main_frame, width=40)
name_entry.pack(pady=5)

tk.Button(main_frame, text="Check In", command=check_in, width=15).pack(pady=5)
tk.Button(main_frame, text="Check Out", command=check_out, width=15).pack(pady=5)
tk.Button(main_frame, text="Show All Logins", command=show_all, width=15).pack(pady=5)
tk.Button(main_frame, text="Logout", command=logout, width=10).pack(pady=10)

output_text = tk.Text(main_frame, height=12, width=80)
output_text.pack(pady=10)

root.mainloop()
