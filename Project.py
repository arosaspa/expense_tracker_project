# expense tracker project

message = """\nWelcome the Expense Tracker Project\n 
        ======== MENU ======== 
        
        1. Add Expense
        2. View Expenses
        3. View Total Spending
        4. Exit
        ======================
                
        Please select an option (1-4):
    """

print(message)

option = int(input(">> "))

print(f"You selected option {option}.")

if option == 1:
    print("Adding expense...")
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Transport): ")
    amount = float(input("Enter amount: "))
    print(f"Expense added: {date}, {category}, ${amount:.2f}")

elif option == 2:
    print("Viewing expenses...")
    # Placeholder for viewing expenses logic
    print("No expenses to show.")

elif option == 3:
    print("Viewing total spending...")
    # Placeholder for total spending logic
    total_spending = 0.0
    print(f"Total spending: ${total_spending:.2f}")
