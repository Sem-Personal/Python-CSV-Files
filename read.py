import csv

print("Search by:")
print("1. Age")
print("2. Name")
print("3. Favourite color")
print("4. Location")
choice = input("Choose option: ")

search_value = input("Enter search value: ")

with open("people_data.csv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if (
            (choice == "1" and row["Age"] == search_value) or
            (choice == "2" and row["Name"].lower() == search_value.lower()) or
            (choice == "3" and row["Favourite Color"].lower() == search_value.lower()) or
            (choice == "4" and row["Location"].lower() == search_value.lower())
        ):
            print(row)
