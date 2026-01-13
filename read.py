import csv

with open("people_data.csv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(
            f"Name: {row['Name']}, "
            f"Age: {row['Age']}, "
            f"Favourite Color: {row['Favourite Color']}, "
            f"Location: {row['Location']}"
        )
