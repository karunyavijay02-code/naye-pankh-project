import csv
import os

# Create data folder if not exists
os.makedirs("data", exist_ok=True)

# Add volunteer
def add_volunteer(name, email):
    with open("data/volunteers.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, email])
    print("✅ Volunteer added successfully!")

# Add donation
def add_donation(name, amount):
    with open("data/donations.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, amount])
    print("💰 Donation recorded successfully!")

# View data
def view_data(file_type):
    file_path = f"data/{file_type}.csv"
    try:
        print(f"\n📄 Showing {file_type} data:\n")
        with open(file_path, "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("❌ No data found!")

# Search function
def search_data(keyword):
    found = False

    for file in ["volunteers.csv", "donations.csv"]:
        try:
            with open(f"data/{file}", "r") as f:
                for line in f:
                    if keyword.lower() in line.lower():
                        print(f"🔎 Found in {file}: {line.strip()}")
                        found = True
        except FileNotFoundError:
            pass

    if not found:
        print("❌ No matching records found.")