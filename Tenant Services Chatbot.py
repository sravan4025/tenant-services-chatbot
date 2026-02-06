# Tenant Services Chatbot

def show_menu():
    print("\n--- Tenant Services Chatbot ---")
    print("1. Rent Information")
    print("2. Maintenance Request")
    print("3. Lease Details")
    print("4. Contact Support")
    print("5. Exit")


def rent_info():
    print("\n💰 Rent Information")
    print("Monthly Rent: ₹15,000")
    print("Due Date: 5th of every month")
    print("Late Fee: ₹500 after due date")


def maintenance_request():
    issue = input("\n🔧 Describe your maintenance issue: ")
    print("Thank you!")
    print(f"Your issue '{issue}' has been registered.")
    print("Our maintenance team will contact you within 24 hours.")


def lease_details():
    print("\n📄 Lease Details")
    print("Lease Duration: 11 Months")
    print("Security Deposit: ₹30,000")
    print("Notice Period: 1 Month")


def contact_support():
    print("\n📞 Contact Support")
    print("Phone: +91 98765 43210")
    print("Email: support@tenantservices.com")
    print("Office Hours: 9 AM – 6 PM")


def chatbot():
    print("Welcome to Tenant Services Chatbot 🤖")

    while True:
        show_menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            rent_info()
        elif choice == "2":
            maintenance_request()
        elif choice == "3":
            lease_details()
        elif choice == "4":
            contact_support()
        elif choice == "5":
            print("\nThank you for using Tenant Services Chatbot. Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Please try again.")


# Run chatbot
chatbot()
