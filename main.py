import csv

name = input("Name: ")
age = input("Age: ")
favorite_color = input("Favourite color: ")
location = input("Located (city/village): ")

with open("people_data.csv", mode="a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    if file.tell() == 0:
        writer.writerow(["Name", "Age", "Favourite Color", "Location"])

    writer.writerow([name, age, favorite_color, location])

print("Data saved to people_data.csv")
