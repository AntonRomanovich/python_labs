import csv

name_1 = "Анна"
name_2 = "Victor"

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow([name_1, name_2])