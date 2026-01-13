import csv

def letters_only(text):
    return all(char.isalpha() or char.isspace() for char in text)

# Name ---
while True:
    name = input("Name: ")
    if letters_only(name) and name.strip():
        break
    else:
        print("Name may only contain letters.")

# Age ---
while True:
    age = input("Age: ")
    if age.isdigit():
        break
    else:
        print("Age must be a number.")

# Favourite color ---
while True:
    favorite_color = input("Favourite color: ")
    if letters_only(favorite_color) and favorite_color.strip():
        break
    else:
        print("Colour may only contain letters.")

# Location ---
while True:
    location = input("Located (city/village): ")
    if letters_only(location) and location.strip():
        break
    else:
        print("Location may only contain letters.")

# Save to CSV ---
with open("people_data.csv", mode="a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    if file.tell() == 0:
        writer.writerow(["Name", "Age", "Favourite Color", "Location"])

    writer.writerow([name, age, favorite_color, location])

print("✅ Data saved to people_data.csv")
