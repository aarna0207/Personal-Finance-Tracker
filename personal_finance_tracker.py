import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib import pyplot as plt
window=tk.Tk()
window.title("Personal Finance Tracker")
window.geometry("700x500")
window.configure(bg="#C6A2E0")
top_frame = tk.Frame(window)
top_frame.configure(bg="#C6A2E0")
top_frame.pack(pady=10)
middle_frame = tk.Frame(window)
middle_frame.configure(bg="#C6A2E0")
middle_frame.pack(pady=10)
bottom_frame = tk.Frame(window)
bottom_frame.configure(bg="#C6A2E0")
bottom_frame.pack(pady=10)
heading = tk.Label(
    top_frame,
    text="💰 Personal Finance Tracker",
    font=("Arial", 20, "bold"),
    bg="#C6A2E0"
)
heading.pack(pady=20)
balance_label = tk.Label(
    top_frame,
    text="Current Balance: Rs.0.00",
    font=("Arial", 16),
    bg="#C6A2E0"
)
balance_label.pack(pady=10)
balance = 0
transactions = []
try:
    with open("transactions.txt", "r") as file:
        transactions = file.readlines()
    transactions = [transaction.strip() for transaction in transactions]
except FileNotFoundError:
    pass
for transaction in transactions:
    parts = transaction.split()
    amount = float(parts[1].replace("Rs.", ""))
    if transaction.startswith("Income"):
        balance += amount
    elif transaction.startswith("Expense"):
        balance -= amount
def add_income():
    global balance
    try:
     income = float(income_entry.get())
    except ValueError:
     messagebox.showwarning(
            "Error",
            "Please enter a valid number."
        )
     return
    if income <= 0:
        messagebox.showwarning(
        "Error",
        "Income must be greater than zero."
    )
        return
    balance += income
    transactions.append(f"Income Rs.{income:.2f}")
    with open("transactions.txt", "a") as f:
        f.write(f"Income Rs.{income:.2f}\n")
    transaction_table.insert(
        "",
        tk.END,
        values=("Income", f"Rs.{income:.2f}")
    )
    balance_label.config(
        text=f"Current Balance: Rs.{balance:.2f}"
    )
    income_entry.delete(0, tk.END)
    messagebox.showinfo(
    "Success",
    "Income added successfully!"
)
def add_expense():
    global balance
    try:
        expense = float(expense_entry.get())
    except ValueError:
        messagebox.showwarning(
            "Error",
            "Please enter a valid number."
        )
        return
    if expense > balance:
        messagebox.showwarning("Insufficient Balance", "You have insufficient funds. Please enter a valid expense amount.")
        return
    if expense <= 0:
        messagebox.showwarning(
        "Error",
        "Expense must be greater than zero."
    )
        return
    balance -= expense
    transactions.append(f"Expense Rs.{expense:.2f}")
    with open("transactions.txt", "a") as file:
        file.write(f"Expense Rs.{expense:.2f}\n") 
    transaction_table.insert(
        "",
        tk.END,
        values=("Expense", f"Rs.{expense:.2f}")
    ) 
    balance_label.config(
        text=f"Current Balance: Rs.{balance:.2f}"
    ) 
    expense_entry.delete(0, tk.END)
    messagebox.showinfo(
        "Success",
        "Expense added successfully!"
    )
def clear_history():
    global balance
    answer = messagebox.askyesno(
        "Confirm",
        "Do you want to clear all transactions?"
    )
    if answer == False:
        return
    transactions.clear() 
    transaction_table.delete(*transaction_table.get_children())
    balance = 0 
    balance_label.config(
        text="Current Balance: Rs.0.00"
    )
    with open("transactions.txt", "w") as file:
        file.write("")
    messagebox.showinfo(
        "Success",
        "Transaction history cleared!"
    )
def financial_summary(): 
    total_income = 0
    total_expense = 0
    for transaction in transactions:
        parts = transaction.split()
        amount = float(parts[1].replace("Rs.", ""))
        if transaction.startswith("Income"):
            total_income += amount
        elif transaction.startswith("Expense"):
            total_expense += amount
    messagebox.showinfo(
        "Financial Summary",
        f"Total Income : Rs.{total_income:.2f}\n"
        f"Total Expense : Rs.{total_expense:.2f}\n"
        f"Current Balance : Rs.{balance:.2f}"
    )
def show_charts():
    total_income = 0
    total_expense = 0
    for transaction in transactions:
        parts = transaction.split()
        amount = float(parts[1].replace("Rs.", ""))
        if transaction.startswith("Income"):
            total_income += amount
        elif transaction.startswith("Expense"):
            total_expense += amount
    categories = ["Income", "Expense"]
    amounts = [total_income, total_expense]
    plt.figure(figsize=(6,4))
    plt.bar(categories, amounts)
    plt.title("Income vs Expense")
    plt.xlabel("Category")
    plt.ylabel("Amount (Rs.)")
    plt.show()
income_label = tk.Label(
    middle_frame,
    text="Enter Income:",
    font=("Arial", 12),
    bg="#C6A2E0"
)
income_label.grid(row=0, column=0, padx=10, pady=10)
income_entry = tk.Entry(
    middle_frame,
    font=("Arial", 12),
    width=20,
    bg="#C6A2E0"
)
income_entry.grid(row=0, column=1, padx=10, pady=10)
income_button = tk.Button(
    middle_frame,
    text="Add Income",
    font=("Arial", 12),
    width=15,
    command=add_income,
    bg="#D9C2EA"
)
income_button.grid(row=0, column=2, padx=10, pady=10)
expense_label = tk.Label(
    middle_frame,
    text="Enter Expense:",
    font=("Arial", 12),
    bg="#C6A2E0"
)
expense_label.grid(row=1, column=0, padx=10, pady=10)
expense_entry = tk.Entry(
    middle_frame,
    font=("Arial", 12),
    width=20,
    bg="#C6A2E0"
)
expense_entry.grid(row=1, column=1, padx=10, pady=10)
expense_button = tk.Button(
    middle_frame,
    text="Add Expense",
    font=("Arial", 12),
    width=15,
    command=add_expense,
    bg="#D9C2EA"
)
expense_button.grid(row=1, column=2, padx=10, pady=10)
history_label = tk.Label(
    bottom_frame,
    text="Transaction History",
    font=("Arial",14,"bold"),
    bg="#C6A2E0"
)
history_label.pack(pady=10)
transaction_table = ttk.Treeview(
    bottom_frame,
    columns=("Type", "Amount"),
    show="headings",
    height=8,
)
transaction_table.heading("Type", text="Type")
transaction_table.heading("Amount", text="Amount")
transaction_table.column("Type", width=150)
transaction_table.column("Amount", width=150)
transaction_table.pack()
for transaction in transactions:
    parts = transaction.split()
    transaction_type = parts[0]
    amount = parts[1]
    transaction_table.insert(
        "",
        tk.END,
        values=(transaction_type, amount)
    )

balance_label.config(
    text=f"Current Balance: Rs.{balance:.2f}"
)
history_button = tk.Button(
    bottom_frame,
    text="Clear History",
    font=("Arial", 12),
    width=15,
    command=clear_history,
    bg="#D9C2EA"
)
history_button.pack(pady=10)
summary_button = tk.Button(
    bottom_frame,
    text="Financial Summary",
    font=("Arial", 12),
    width=20,
    command=financial_summary,
    bg="#D9C2EA"
)
summary_button.pack(pady=10)
chart_button = tk.Button(
    bottom_frame,
    text="Graphical Representation",
    font=("Arial", 12),
    width=20,
    command=show_charts,
    bg="#D9C2EA"
)
chart_button.pack(pady=10)
income_entry.focus()
window.mainloop()
