import csv

def checkavalibility():
    with open('books.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        book_name = input("Enter Bookname : ")
        count = 0

        for i in reader :
            if book_name.capitalize() == i["NAME"].capitalize():
                book_name = i["NAME"]
                if i["Availability"] == ("Yes"):
                    count = 1
                else:
                    count = 2
                break

        if count == 0:
            print("book not in library")
            return ""
        elif count == 1:
            print("yes book is available")        
            return book_name
        elif count == 2:
            print("book is not available")
            return book_name
        



def add_new_book():
    filename = 'books.csv'
    fieldnames = ["ID","NAME", "Availability"]
    
    name = input("Enter new Book Name: ").strip().capitalize()
    availability = input("Is it available? (Yes/No): ").strip().capitalize()

    id = 0
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = list(reader)
        id = len(data)

    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({"ID": id ,"NAME": name, "Availability": availability})
        print(f"Book '{name}' added successfully.")

def print_all_book():
    filename = 'books.csv'
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        print("ID","Name","Availability")
        for i in reader:
            print(i["ID"],i["NAME"],i["Availability"])

def update_book_availability():
    filename = "books.csv"
    fieldnames = ["ID", "NAME", "Availability"]
    print("search book you want to update : ")
    book = checkavalibility()
    if book == "":
            print("Update canceled.")
            return

    new_status = input("Enter new availability (Yes/No): ").strip().capitalize()
    found = False

    updated_rows = []
    found = False
    
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["NAME"] == book:
                        row["Availability"] = new_status
                        found = True
                        updated_rows.append(row)
    if found:
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(updated_rows)
            print(f"Book ID {book} updated successfully.")
    else:
            print(f"Book ID {book} not found.")
            
def menu():
    while True:
        print("\n LIBRARY MENU")
        print("1. Check Book Availability")
        print("2. Add New Book")
        print("3. Update Book Availability")
        print("4. Print All Books")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            checkavalibility()
        elif choice == "2":
            add_new_book()
        elif choice == "3":
            update_book_availability()
        elif choice == "4":
            print_all_book()
        elif choice == "5":
            print("Thanks for using the library system")
            break
        else:
            print(" Invalid choice, try again")

"""
       
while True :
    checkavalibility()

    choice=input("Do you want to check another book ? Y/N :")
    
    if choice in ("Y","y"):
        continue
    elif choice in ("N","n"):
        print("Thanks")
        break
    else:
        print("Enter a valid choice")
        exit()


"""
menu()
