expenses = []

# Function to record a new expense
def track_expenses(date, category, amount):
    extra_expense = {
        'date': date,
        'category': category,
        'amount': amount
    }
    expenses.append(extra_expense)

# Function to calculate the total balance
def calculate_balance():
    balance = 0
    for extra_expense in expenses:
        balance += extra_expense['amount']
    return balance

# Function to display transactions
def view_expenses():
    for i, extra_expense in enumerate(expenses, 1):
        print(f"{i}. Date: {extra_expense['date']}, Category: {extra_expense['category']}, Amount: Rupees{extra_expense['amount']}")

# Main program loop
while True:
    print("\n Student Personal Finance Tracker")
    print("1. Record a transaction")
    print("2. Calculate total amount")
    print("3. Display transactions")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        track_expenses(date, category, amount)
        print("Transaction recorded successfully!")

    elif choice == '2':
        balance = calculate_balance()
        print(f"Current Balance: {balance} Rupees only")

    elif choice == '3':
        view_expenses()

    elif choice =='4':
        quit

    else:
      print("Invalid choice.\nPlease choose a valid option.")
