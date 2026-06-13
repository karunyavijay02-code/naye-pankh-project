from utils import add_volunteer, add_donation, view_data, search_data
from report import generate_report

def menu():
    print("\n🌱 NayePankh Foundation Management System")
    print("1. Add Volunteer")
    print("2. Add Donation")
    print("3. View Volunteers")
    print("4. View Donations")
    print("5. Search Data")
    print("6. Generate Report")
    print("7. Exit")

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Volunteer Name: ")
        email = input("Enter Email: ")
        add_volunteer(name, email)

    elif choice == "2":
        name = input("Enter Donor Name: ")
        amount = input("Enter Amount: ")
        add_donation(name, amount)

    elif choice == "3":
        view_data("volunteers")

    elif choice == "4":
        view_data("donations")

    elif choice == "5":
        keyword = input("Enter name to search: ")
        search_data(keyword)

    elif choice == "6":
        generate_report()

    elif choice == "7":
        print("👋 Exiting... Thank you!")
        break

    else:
        print("❌ Invalid choice! Try again.")