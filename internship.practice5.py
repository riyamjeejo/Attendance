import tkinter as tk
from tkinter import messagebox
import csv
from datetime import datetime

filename = "check_out.csv"

def validate_login():
    user = username_entry.get()
    pwd  = password_entry.get()

    if user == "admin" and pwd == "password":
        messagebox.showinfo("Login Status", "Login Successful!")
    else:
        messagebox.showerror("Login Status", "Invalid username or password")

def check_in():
    name = name_entry.get().strip()
    if not name:
        messagebox.showwarning("Input Error", "Enter a name to check in")
        return
    
    check_in_time = datetime.now()
    with open(filename, mode="a",newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, check_in_time ,""])
        print(f" {name} checked in at {check_in_time},")

def check_out():
    name = input("Enter your name: ")
    check_out_time = datetime.now()  
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
        print(f"{name} checked out at {check_out_time}")
    else:
        print("No active check_in found")


def print_all_login():
    filename = "check_out.csv"
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        print("NAME","CHECK-IN","CHECK-OUT")
        for i in reader:
            print(i[0],i[1],i[2])

def menu():
    while True:
        print("\n CHECKING MENU")
        print("1. Check_In_Time")
        print("2. Check_Out_Time")
        print("3. Login")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            check_in()
        elif choice == "2":
            check_out()
        elif choice == "3":
            print_all_login()
        elif choice == "4":
            print("Thanks for using the library system")
            break
        else:
            print(" Invalid choice, try again")
            
