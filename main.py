balance = 0
transactions = []
while True:
    print("-" * 40)
    print("Personal Finance Tracker".center(40))
    print("-" * 40)
    print("Menu Options".center(40))
    print("-" * 40)
    print("1= Add Income")
    print("2= Add Expense")
    print("3= View Balance")
    print("4= View Transactions")
    print("5= Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        income = float(input("Enter income amount: "))
        if income <= 0:
            print("Income cannot be negative. Please enter a valid amount.")
            again = input("Do you want to see the menu again? (yes/no): ")
            if again.lower() != "yes":
               print("Thank you for using Personal Finance Tracker!")
               break
            continue
        else: 
            balance += income
            transactions.append(("Income", income))
            print(f"Income of Rs.{income:.2f} added.")
    elif choice == '2':
        expense = float(input("Enter expense amount: "))
        if expense <= 0:
            print("Expense cannot be negative. Please enter a valid amount.")
            again = input("Do you want to see the menu again? (yes/no): ")
            if again.lower() != "yes":
               print("Thank you for using Personal Finance Tracker!")
               break
            continue
        else:
            if expense>balance:
                print("Insufficient balance for this expense.")
                again = input("Do you want to see the menu again? (yes/no): ")
                if again.lower() != "yes":
                 print("Thank you for using Personal Finance Tracker!")
                 break
                continue
            else:
                balance-= expense
                transactions.append(("Expense", expense))
                print(f"Expense of Rs.{expense:.2f} added.")
    elif choice == '3':
        print(f"Current balance: Rs.{balance:.2f}")
    elif choice == '4':
        print("-" * 40)
        print("Transaction History:".center(40))
        print("-" * 40)
        if len(transactions) == 0:
            print("No transactions yet.")
        else:
            for transaction in transactions:
                 print(f"{transaction[0]} : Rs.{transaction[1]:.2f}")
    elif choice == '5':
        print("Thank you for using Personal Finance Tracker!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

    again = input("Do you want to see the menu again? (yes/no): ")
    if again.lower() != "yes":
        print("Thank you for using Personal Finance Tracker!")
        break