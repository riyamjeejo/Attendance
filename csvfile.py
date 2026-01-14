import csv
with open('books.csv', mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    print(type(reader))
    for row in reader:
        print(row['ID'], row['NAME']) 
