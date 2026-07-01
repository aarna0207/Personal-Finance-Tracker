balance = 0
while True:
    print("-" * 40)
    print("Personal Finance Tracker".center(40))
    print("-" * 40)
    print("Menu Options".center(40))
    print("-" * 40)
    print("1= Add Income")
    print("2= Add Expense")
    print("3= View Balance")
    print("4= Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        income = float(input("Enter income amount: "))
        balance = balance + income
        print("Income of Rs.",income ,"added.")
    elif choice == '2':
        expense = float(input("Enter expense amount: "))
        balance = balance - expense
        print(f"Expense of Rs.{expense} added.")
    elif choice == '3':
        print(f"Current balance: Rs.{balance}")
    elif choice == '4':
        print("Thank you for using the Personal Finance Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
   
    again = input("Do you want to see the menu again? (yes/no): ")
    if again.lower() != "yes":
        print("Thank you for using Personal Finance Tracker!")
        break