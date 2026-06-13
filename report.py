import csv

def generate_report():
    try:
        total_donations = 0
        count = 0

        with open("data/donations.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row:
                    total_donations += int(row[1])
                    count += 1

        print("\n📊 NayePankh Foundation Report")
        print("----------------------------")
        print(f"Total Donations: ₹{total_donations}")
        print(f"Number of Donations: {count}")

    except FileNotFoundError:
        print("❌ No donation data available.")
    except ValueError:
        print("⚠️ Error: Invalid data in donations file.")