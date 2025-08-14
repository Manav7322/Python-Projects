import csv
from datetime import datetime
import os

filename="expenses.csv"
fieldnames=["date", "category", "amount", "description"]
expenses=[]

def load_expenses():
    if not os.path.exists(filename):
        print("nothing yet added")
        return[]
    with open(filename,mode='r',newline="") as file:
        reader=csv.DictReader(file)
        return list(reader)
    

def save_expenses():
    with open(filename,mode='w',newline="") as file:
        writer=csv.DictWriter(file,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)


def edit_expense():
    view_expense()
    if not expenses:
        return
    try:
        index=int(input("Enter expense number to edit: "))-1
        if index < 0 or index >= len(expenses):
            print("Invalid Number")
            return 
        
        expense=expenses[index]
        print("Please enter to keep the current values.")
        new_date = input(f"Date [{expense['date']}]: ").strip() or expense['date']
        new_category = input(f"Category [{expense['category']}]: ").strip() or expense['category']
        new_amount = input(f"Amount [{expense['amount']}]: ").strip() or expense['amount']
        new_description = input(f"Description [{expense['description']}]: ").strip() or expense['description']

        expenses[index]={
            "date": new_date,
            "category": new_category,
            "amount": new_amount,
            "description": new_description
        }
        save_expenses()
        print("Expense updated successfully.")
    except ValueError:
        print("Please enter a valid number.")


def add_expense():
    date_str=input("Enter date (YYYY-MM-DD) or leave a blank for today: ").strip()
    if not date_str:
        date_str=datetime.today().strftime("%Y-%m-%d")
    category = input("Enter category (Food, Travel, etc.): ").strip()
    amount=float(input("Enter amount: "))
    description=input("Enter description: ").strip()

    expense={
        "date": date_str,
        "category": category,
        "amount": amount,
        "description": description
    }
    expenses.append(expense)
    save_expenses()
    print("Expense added and saved!")
def view_expense():
    if not expenses:
        print("No expense Found")
        return
    print("\n--- Expenses ---")
    for i,exp in enumerate(expenses,start=1):
        print(f"{i}.{exp['date']} | {exp['category']} | {exp['amount']} | {exp['description']}")


def delete_expense():
    view_expense()
    if not expenses:
        return 
    try:
        num = int(input("Enter expense number to delete: ").strip())
        if 1 <= num <= len(expenses):
            deleted = expenses.pop(num - 1)
            save_expenses()
            print(f"Deleted: {deleted['date']} | {deleted['category']} | {deleted['amount']} | {deleted['description']}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    global expenses
    expenses=load_expenses()
    while True:
        print("\nChoose an option")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Edit Expense")
        print("4. Delete Expense")
        print("5. Exit")

        choice=input("Enter choice: ").strip()

        match choice:
            case "1":
                add_expense()
            case "2":
                view_expense()
            case "3":
                edit_expense()
            case "4":
                delete_expense()
            case "5":
                print("Exiting... Goodbye!")
                break
            case _:
                print("invalid choice. Try again")


if __name__=="__main__":
    main()